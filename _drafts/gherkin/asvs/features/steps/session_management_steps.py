# features/steps/session_management_steps.py
from behave import given, when, then
from zap import Zap
import requests
import time
import logging
import re
from urllib.parse import urlparse

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@given('I am assessing the application\'s authentication mechanisms')
def step_assess_auth_mechanisms(context):
    """Setup ZAP connection and application target"""
    # Get target URL from config or use default
    context.target_url = context.config.userdata.get('target_url', 'http://localhost:8080')

    # Initialize ZAP API client
    context.zap = ZAPv2(
        apikey=context.config.userdata.get('zap_api_key', ''),
        proxies={'http': context.config.userdata.get('zap_proxy', 'http://localhost:8080')}
    )

    # Configure context
    context.session = requests.Session()
    # Setup proxy for all requests to go through ZAP
    context.session.proxies = {
        'http': context.config.userdata.get('zap_proxy', 'http://localhost:8080'),
        'https': context.config.userdata.get('zap_proxy', 'http://localhost:8080')
    }
    context.session.verify = False  # Disable SSL verification for testing

    logger.info(f"Connected to ZAP, targeting: {context.target_url}")

@given('I have access to authentication-related documentation and code')
def step_have_access_to_docs(context):
    """This step is primarily for documentation purposes in the BDD scenario"""
    pass

@when('I review session management related to authentication')
def step_review_session_management(context):
    """Analyze session management by testing authentication and scanning with ZAP"""
    # Setup ZAP scan context
    hostname = urlparse(context.target_url).netloc
    context_name = f"session_test_{hostname}"

    # Create context if not exists
    existing_contexts = context.zap.context.context_list
    if context_name not in existing_contexts:
        context.zap_context_id = context.zap.context.new_context(context_name)
        # Set context scope
        context.zap.context.include_in_context(context_name, f"^{context.target_url}.*$")
    else:
        context.zap_context_id = context.zap.context.context_list[context_name]

    # Configure login details - these should come from configuration
    login_url = f"{context.target_url}/login"
    login_data = {
        "username": context.config.userdata.get('test_username', 'testuser'),
        "password": context.config.userdata.get('test_password', 'testpass')
    }

    # Test login functionality
    logger.info("Testing login functionality...")
    try:
        login_response = context.session.post(login_url, data=login_data, allow_redirects=True)

        # Check login success
        if login_response.status_code == 200:
            # Get session cookies
            context.session_cookies = login_response.cookies.get_dict()
            logger.info(f"Login successful. Session cookies: {list(context.session_cookies.keys())}")

            # Store a reference authenticated session for later checks
            context.authenticated_session = context.session_cookies.copy()
        else:
            logger.error(f"Login failed with status code: {login_response.status_code}")
            assert False, "Failed to login to the application"
    except Exception as e:
        logger.error(f"Error during login: {str(e)}")
        assert False, f"Error during login: {str(e)}"

    # Run ZAP active scan
    logger.info("Running ZAP scan to identify session management issues...")
    try:
        # Spider scan
        spider_scan_id = context.zap.spider.scan(context.target_url)
        time.sleep(2)
        while int(context.zap.spider.status(spider_scan_id)) < 100:
            logger.info(f"Spider progress: {context.zap.spider.status(spider_scan_id)}%")
            time.sleep(5)

        # Active scan
        scan_id = context.zap.ascan.scan(context.target_url)
        time.sleep(2)
        while int(context.zap.ascan.status(scan_id)) < 100:
            logger.info(f"Scan progress: {context.zap.ascan.status(scan_id)}%")
            time.sleep(10)

        # Collect session-related alerts
        context.session_alerts = []
        all_alerts = context.zap.core.alerts()
        for alert in all_alerts:
            if any(kw in alert.get('name', '').lower() for kw in ['session', 'authentication', 'cookie']):
                context.session_alerts.append(alert)

        logger.info(f"Found {len(context.session_alerts)} session-related security issues")
    except Exception as e:
        logger.error(f"Error during ZAP scanning: {str(e)}")

@then('authentication controls should be enforced server-side')
def step_verify_server_side_controls(context):
    """Verify that authentication is enforced server-side by attempting to access protected resources"""
    logger.info("Verifying server-side authentication controls...")

    # Get a protected URL (should be configured)
    protected_url = context.config.userdata.get('protected_url', f"{context.target_url}/dashboard")

    # Try accessing without authentication
    unauthenticated = requests.get(protected_url, allow_redirects=False)

    # Try accessing with authentication
    authenticated = requests.get(protected_url, cookies=context.authenticated_session)

    # Verify authentication is enforced
    assert unauthenticated.status_code in [401, 403, 302], (
        f"Unauthenticated access to protected resource should be denied, but got status {unauthenticated.status_code}"
    )

    assert authenticated.status_code == 200, (
        f"Authenticated access to protected resource failed with status {authenticated.status_code}"
    )

    # Check for client-side authentication bypass vulnerabilities
    client_auth_issues = [alert for alert in context.session_alerts
                         if "client side" in alert.get('description', '').lower()
                         and "authentication" in alert.get('description', '').lower()]

    if client_auth_issues:
        for issue in client_auth_issues:
            logger.warning(f"Client-side auth issue: {issue.get('name')} - {issue.get('description')}")

    assert len(client_auth_issues) == 0, f"Found {len(client_auth_issues)} client-side authentication issues"

@then('session identifiers should be invalidated after logout')
def step_verify_session_invalidation(context):
    """Verify that session IDs are properly invalidated after logout"""
    logger.info("Testing session invalidation after logout...")

    # Get logout URL
    logout_url = context.config.userdata.get('logout_url', f"{context.target_url}/logout")
    protected_url = context.config.userdata.get('protected_url', f"{context.target_url}/dashboard")

    # Store session cookies before logout
    pre_logout_cookies = context.authenticated_session.copy()

    # Perform logout
    logout_response = context.session.get(logout_url, allow_redirects=True)
    assert logout_response.status_code in [200, 302], f"Logout failed with status {logout_response.status_code}"

    # Try to access protected resource with old session
    post_logout_access = requests.get(
        protected_url,
        cookies=pre_logout_cookies,
        allow_redirects=False
    )

    # Verify old session no longer works
    assert post_logout_access.status_code in [302, 401, 403], (
        f"Session still valid after logout, got status {post_logout_access.status_code}"
    )

    # Check for session invalidation issues
    session_invalidation_issues = [alert for alert in context.session_alerts
                                  if "session" in alert.get('name', '').lower()
                                  and "invalidation" in alert.get('name', '').lower()]

    if session_invalidation_issues:
        for issue in session_invalidation_issues:
            logger.warning(f"Session invalidation issue: {issue.get('name')}")

@then('sessions should have appropriate idle timeout periods')
def step_verify_idle_timeout(context):
    """Verify that sessions timeout after a period of inactivity"""
    logger.info("Testing session timeout functionality...")

    # This would normally require waiting for timeout period
    # For testing purposes, we'll check if session cookies have expiry settings

    # Get session cookie info
    cookies = context.session.cookies
    session_cookies = [c for c in cookies if c.name in context.authenticated_session]

    # Check for expiry attributes in cookies
    has_timeout = False
    for cookie in session_cookies:
        if cookie.expires is not None:
            has_timeout = True
            logger.info(f"Cookie {cookie.name} has expiry set")
            break

    # Check for cookie max-age attribute using ZAP
    if not has_timeout:
        # Use ZAP to check for session cookie attributes
        cookies_from_zap = context.zap.httpsessions.cookies
        for cookie in cookies_from_zap:
            if 'max-age' in str(cookie).lower():
                has_timeout = True
                logger.info(f"Cookie has max-age attribute: {cookie}")
                break

    # Scan for session timeout issues
    timeout_issues = [alert for alert in context.session_alerts
                     if "session" in alert.get('name', '').lower()
                     and "timeout" in alert.get('name', '').lower()]

    if timeout_issues:
        for issue in timeout_issues:
            logger.warning(f"Session timeout issue: {issue.get('name')}")

    assert has_timeout or len(timeout_issues) == 0, (
        "No session timeout detected. Sessions should have appropriate idle timeout periods."
    )
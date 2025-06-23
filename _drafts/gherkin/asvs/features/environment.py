# features/environment.py
import logging
import os
from zap import Zap
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Suppress SSL warnings for testing
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def before_all(context):
    """Set up global test environment"""
    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Load test configuration
    context.config.setup_logging()

    # Default configurations
    userdata = context.config.userdata
    context.zap_proxy = userdata.get('zap_proxy', 'http://localhost:8080')
    context.zap_api_key = userdata.get('zap_api_key', '')
    context.target_url = userdata.get('target_url', 'http://localhost:8080')

    # Connect to ZAP
    try:
        zap = ZAPv2(apikey=context.zap_api_key, proxies={'http': context.zap_proxy, 'https': context.zap_proxy})
        version = zap.core.version
        logging.info(f"Connected to ZAP version {version}")

        # Create a new ZAP session
        zap.core.new_session()
    except Exception as e:
        logging.error(f"Failed to connect to ZAP: {str(e)}")
        logging.error("Make sure ZAP is running and accessible")

def after_all(context):
    """Clean up and generate reports"""
    if hasattr(context, 'zap'):
        try:
            # Save ZAP session
            context.zap.core.save_session(
                name="session_management_test",
                overwrite=True
            )

            # Generate security report
            report_file = "session_management_security_report.html"
            with open(report_file, 'w') as f:
                f.write(context.zap.core.htmlreport())
            logging.info(f"ZAP security report saved to {report_file}")
        except Exception as e:
            logging.error(f"Error generating ZAP report: {str(e)}")

def before_scenario(context, scenario):
    """Set up scenario-specific test environment"""
    if 'ASVS-V2.13' in scenario.tags:
        logging.info("Running session management verification scenario")
        # You could set up specific test parameters based on the ASVS level
        context.security_level = [tag for tag in scenario.tags if tag.startswith('L')]
        logging.info(f"Security level: {context.security_level}")

def after_scenario(context, scenario):
    """Clean up after each scenario"""
    if hasattr(context, 'session'):
        # Try to logout if we're still logged in
        try:
            logout_url = context.config.userdata.get('logout_url', f"{context.target_url}/logout")
            context.session.get(logout_url, allow_redirects=False)
        except:
            pass
#!/bin/bash
# First, start OWASP ZAP in daemon mode
# Then run:
~/.venv/bin/behave features/authentication/session_management.feature \
  -D target_url=https://your-application-url \
  -D test_username=your_test_user \
  -D test_password=your_test_password \
  -D protected_url=https://your-application-url/protected-area \
  -D logout_url=https://your-application-url/logout \
  -D zap_proxy=http://localhost:8080 \
  -D zap_api_key=your-api-key
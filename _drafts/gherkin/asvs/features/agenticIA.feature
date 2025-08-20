---
layout: post
date: 2042-03-03
title: "OWASP Top 10 LLM10-2025 - 💥Consommation non limitée💥"
categories:
  - veille
  - CyberSec
  - Top10
  - OWASP
  - LLM

---


Feature: V2.13 Session Management Authentication Security Requirements
  As an application security professional
  I want to verify that our application meets OWASP ASVS v4 session management requirements
  So that user sessions remain secure and protected from common attacks

  Background:
    Given I am assessing the application's authentication mechanisms
    And I have access to authentication-related documentation and code

  @ASVS-V2.13.1 @L1 @L2 @L3
  Scenario: Verify server-side enforcement of authentication controls
    When I review session management related to authentication
    Then authentication controls should be enforced server-side
    And client-side authentication validation should only be used for user experience

  @ASVS-V2.13.2 @L1 @L2 @L3
  Scenario: Verify session tokens use secure algorithms
    When I analyze the session token generation mechanism
    Then session tokens should use approved cryptographic algorithms
    And session tokens should have sufficient entropy
    And session tokens should not be predictable

  @ASVS-V2.13.3 @L1 @L2 @L3
  Scenario: Verify session invalidation after logout
    When I perform a logout operation
    Then session identifiers should be invalidated after logout
    And subsequent requests with the invalidated session should be rejected

  @ASVS-V2.13.4 @L1 @L2 @L3
  Scenario: Verify session timeout after inactivity
    When a user session remains idle for the configured timeout period
    Then sessions should have appropriate idle timeout periods
    And the user should be required to re-authenticate after timeout

  @ASVS-V2.13.5 @L1 @L2 @L3
  Scenario: Verify absolute session timeout
    When a user session exceeds the maximum allowed lifetime
    Then the session should be terminated
    And the user should be required to re-authenticate

  @ASVS-V2.13.6 @L1 @L2 @L3
  Scenario: Verify session refresh on authentication
    When a user successfully authenticates to the application
    Then any existing session identifiers should be invalidated
    And a new session identifier should be generated

  @ASVS-V2.13.7 @L1 @L2 @L3
  Scenario: Verify consistent session management controls
    When I examine the session management implementation across the application
    Then the same session management controls should be used throughout the application
    And all authentication-protected pages should enforce equal session management

  @ASVS-V2.13.8 @L2 @L3
  Scenario: Verify session cookie security attributes
    When I examine session cookie configuration
    Then session cookies should have the 'Secure' attribute set
    And session cookies should have the 'HttpOnly' attribute set
    And session cookies should have the 'SameSite' attribute configured appropriately

  @ASVS-V2.13.9 @L1 @L2 @L3
  Scenario: Verify session cookie renewal after successful login
    When a user completes authentication successfully
    Then the session cookie value should be changed
    And the previous session cookie should no longer be valid
###
### Prompt :
###   Based on ASVS 4, I want you to generate all the elements for the file 'asvs2_authentication.feature'
###

Feature: V2 Authentication Verification Requirements
  As an application security professional
  I want to verify that our application meets OWASP ASVS v4 Authentication requirements
  So that we can ensure secure authentication controls

  Background:
    Given I am assessing the application's authentication mechanisms
    And I have access to authentication-related documentation and code

  @ASVS-V2.1 @L1 @L2 @L3
  Scenario: Verify password security requirements
    When I review the password policy implementation
    Then passwords should be stored with sufficient cryptographic protection
    And passwords should have at least 12 characters minimum length
    And passwords should enforce complexity requirements
    And passwords should be checked against common password lists

  @ASVS-V2.2 @L1 @L2 @L3
  Scenario: Verify password recovery and account recovery mechanisms
    When I test the password recovery process
    Then the system should not reveal account existence during recovery
    And the system should use secure reset mechanisms
    And the system should not send original passwords in recovery emails
    And recovery links should have limited validity period

  @ASVS-V2.3 @L1 @L2 @L3
  Scenario: Verify authenticator and verifier requirements
    When I review the authenticator implementation
    Then only approved cryptographic algorithms should be used
    And authentication credentials should be stored securely
    And authentication secrets should be protected in transit
    And passwords should be hashed using strong algorithms

  @ASVS-V2.4 @L2 @L3
  Scenario: Verify credential storage
    When I review how credentials are stored
    Then passwords should be salted and hashed with approved algorithms
    And the system should use a sufficient work factor for hashing
    And salts should be unique for each credential
    And key stretching or adaptive hashing should be used

  @ASVS-V2.5 @L1 @L2 @L3
  Scenario: Verify credential retrieval
    When I test credential retrieval processes
    Then the system should enforce secure password policies
    And no default, weak, or well-known passwords should be allowed
    And the system should validate password strength

  @ASVS-V2.6 @L2 @L3
  Scenario: Verify look-up secret verifier
    When I review look-up secret verification
    Then look-up secrets should be protected as authentication credentials
    And look-up secrets should be limited use or single-use
    And look-up secrets should be generated using secure random number generators

  @ASVS-V2.7 @L2 @L3
  Scenario: Verify out-of-band verifier
    When I test out-of-band authentication mechanisms
    Then the system should protect against man-in-the-middle attacks
    And out-of-band authenticators should expire after 10 minutes
    And out-of-band tokens should be unique per session

  @ASVS-V2.8 @L2 @L3
  Scenario: Verify single or multi-factor one-time verifier
    When I test one-time verification mechanisms
    Then OTP authenticators should use approved cryptographic algorithms
    And TOTP tokens should use at least 6 digits
    And OTP codes should be valid for a limited time

  @ASVS-V2.9 @L2 @L3
  Scenario: Verify cryptographic verifier
    When I review cryptographic authentication mechanisms
    Then strong cryptographic authenticators should be used
    And private keys should be stored securely
    And cryptographic implementations should use approved algorithms

  @ASVS-V2.10 @L1 @L2 @L3
  Scenario: Verify service authentication
    When I review service-to-service authentication
    Then integrations between services should use unique credentials
    And API keys should have limited privileges
    And service accounts should have strong authentication requirements

  @ASVS-V2.11 @MFA @L3
  Scenario: Verify multi-factor authentication
    When I test multi-factor authentication implementation
    Then at least two independent authentication factors should be required
    And MFA should be enforced for all administrative access
    And MFA should be required for high-value transactions

  @ASVS-V2.12 @L1 @L2
  Scenario: Verify re-authentication
    When I test re-authentication mechanisms
    Then critical operations should require re-authentication
    And sessions should have appropriate timeout periods
    And changing password should require current password verification

  @ASVS-V2.13 @L1 @L2 @L3
  Scenario: Verify session management for authentication
    When I review session management related to authentication
    Then authentication controls should be enforced server-side
    And session identifiers should be invalidated after logout
    And sessions should have appropriate idle timeout periods

  @ASVS-V2.14 @L1 @L2 @L3
  Scenario: Verify defenses against authentication attacks
    When I test authentication security controls
    Then the system should have brute force protection
    And the system should have rate limiting for failed attempts
    And the system should implement account lockout mechanisms
    And the system should protect against credential stuffing attacks
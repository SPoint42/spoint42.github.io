###
### Prompt :
### You are an application and cloud security expert and also an QA engineer.
### Based on the OWASP ASVS 4 I want you to generate an global gherkin file to cover each
### of the OWASP ASVS chapter as a global file. I want to have also one file per
### ASVS item and link every file to the global file.
###

Feature: OWASP ASVS v4 Compliance Verification
  As an application security professional
  I want to verify that our application complies with OWASP ASVS v4 requirements
  So that we can ensure the security of our application

  # Chapter V1: Architecture, Design and Threat Modeling
  @ASVS-V1 @Architecture
  Scenario: Verify Architecture, Design and Threat Modeling compliance
    Given the system has documented architecture and design
    When I review the security architecture documentation
    Then all requirements from ASVS V1 should be fulfilled
    And detailed verifications are in "asvs1_architecture.feature"

  # Chapter V2: Authentication
  @ASVS-V2 @Authentication
  Scenario: Verify Authentication compliance
    Given the system implements authentication controls
    When I review the authentication mechanisms
    Then all requirements from ASVS V2 should be fulfilled
    And detailed verifications are in "asvs2_authentication.feature"

  # Chapter V3: Session Management
  @ASVS-V3 @SessionManagement
  Scenario: Verify Session Management compliance
    Given the system implements session management
    When I review the session handling mechanisms
    Then all requirements from ASVS V3 should be fulfilled
    And detailed verifications are in "asvs3_session_management.feature"

  # Chapter V4: Access Control
  @ASVS-V4 @AccessControl
  Scenario: Verify Access Control compliance
    Given the system implements access control
    When I review the authorization mechanisms
    Then all requirements from ASVS V4 should be fulfilled
    And detailed verifications are in "asvs4_access_control.feature"

  # Chapter V5: Validation, Sanitization and Encoding
  @ASVS-V5 @InputValidation
  Scenario: Verify Validation, Sanitization and Encoding compliance
    Given the system processes user inputs
    When I review input handling mechanisms
    Then all requirements from ASVS V5 should be fulfilled
    And detailed verifications are in "asvs5_validation.feature"

  # Chapter V6: Stored Cryptography
  @ASVS-V6 @Cryptography
  Scenario: Verify Cryptography compliance
    Given the system uses cryptographic functions
    When I review the cryptographic implementations
    Then all requirements from ASVS V6 should be fulfilled
    And detailed verifications are in "asvs6_cryptography.feature"

  # Chapter V7: Error Handling and Logging
  @ASVS-V7 @ErrorHandling @Logging
  Scenario: Verify Error Handling and Logging compliance
    Given the system implements error handling and logging
    When I review the error handling and logging mechanisms
    Then all requirements from ASVS V7 should be fulfilled
    And detailed verifications are in "asvs7_error_logging.feature"

  # Chapter V8: Data Protection
  @ASVS-V8 @DataProtection
  Scenario: Verify Data Protection compliance
    Given the system stores and processes sensitive data
    When I review the data protection mechanisms
    Then all requirements from ASVS V8 should be fulfilled
    And detailed verifications are in "asvs8_data_protection.feature"

  # Chapter V9: Communications
  @ASVS-V9 @Communications
  Scenario: Verify Communications compliance
    Given the system communicates over networks
    When I review the communication security mechanisms
    Then all requirements from ASVS V9 should be fulfilled
    And detailed verifications are in "asvs9_communications.feature"

  # Chapter V10: Malicious Code
  @ASVS-V10 @MaliciousCode
  Scenario: Verify Malicious Code compliance
    Given the system has code security controls
    When I review the code security mechanisms
    Then all requirements from ASVS V10 should be fulfilled
    And detailed verifications are in "asvs10_malicious_code.feature"

  # Chapter V11: Business Logic
  @ASVS-V11 @BusinessLogic
  Scenario: Verify Business Logic compliance
    Given the system implements business logic
    When I review the business logic implementation
    Then all requirements from ASVS V11 should be fulfilled
    And detailed verifications are in "asvs11_business_logic.feature"

  # Chapter V12: Files and Resources
  @ASVS-V12 @FilesAndResources
  Scenario: Verify Files and Resources compliance
    Given the system handles files and resources
    When I review the file handling mechanisms
    Then all requirements from ASVS V12 should be fulfilled
    And detailed verifications are in "asvs12_files_resources.feature"

  # Chapter V13: API and Web Service
  @ASVS-V13 @API @WebService
  Scenario: Verify API and Web Service compliance
    Given the system exposes APIs or web services
    When I review the API security mechanisms
    Then all requirements from ASVS V13 should be fulfilled
    And detailed verifications are in "asvs13_api_webservice.feature"

  # Chapter V14: Configuration
  @ASVS-V14 @Configuration
  Scenario: Verify Configuration compliance
    Given the system has configurable components
    When I review the configuration security controls
    Then all requirements from ASVS V14 should be fulfilled
    And detailed verifications are in "asvs14_configuration.feature"
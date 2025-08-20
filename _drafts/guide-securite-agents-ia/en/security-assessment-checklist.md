# Security Assessment Checklist for AI Agents

## General Information

**Project**: ______________________ **Version**: ______________  
**Assessment Date**: ______________ **Assessor**: ______________________  
**Security Classification**: [ ] Critical [ ] High [ ] Medium [ ] Low

## Instructions
Use this checklist during code reviews, testing phases, or as a self-assessment guide during AI agent development. For each item, indicate the status:
- ✅ Implemented and tested 
- ⚠️ Partially implemented
- ❌ Not implemented 
- N/A Not applicable

## 1. Protection Against Persistent Prompt Injection

### Input Validation
- [ ] Implementation of an input validator that filters malicious instruction sequences
- [ ] Analysis of inputs to detect agent manipulation attempts
- [ ] Restriction of allowed character sets in input if applicable
- [ ] Normalization of user inputs before processing by the agent

### Context Isolation
- [ ] Clear separation between system instructions and user inputs
- [ ] Implementation of a mechanism to prevent overwriting of system instructions
- [ ] Isolation of conversation history context 
- [ ] Mechanism for regular conversation context reset

### Monitoring and Detection
- [ ] Logging of prompt injection attempts
- [ ] Alerts configured for suspicious prompt patterns
- [ ] Detection of anomalies in agent behavior
- [ ] Periodic review of agent activity logs

## 2. Protection Against Tool Hijacking

### Tool Access Control
- [ ] Whitelist of tools accessible to the agent
- [ ] Implementation of role-based access controls (RBAC)
- [ ] Granular restrictions on resources accessible by each tool
- [ ] Specific authentication for sensitive tools

### Tool Call Validation
- [ ] Syntactic and semantic validation of tool call parameters
- [ ] Filtering of sensitive commands and arguments
- [ ] Detection of abnormal tool call sequences
- [ ] Limitation of the number of tool calls in a session

### Approval Mechanisms
- [ ] Implementation of human validation workflow for sensitive actions
- [ ] Clear confirmation interface for critical operations
- [ ] Timeout mechanism for approval requests
- [ ] Logging of all approvals and rejections

## 3. Protection Against Data Exfiltration

### Output Control
- [ ] Output filtering to detect sensitive data
- [ ] Automatic masking of personally identifiable information (PII)
- [ ] Limitation of data volume that can be returned by the agent
- [ ] Output validation before transmission to user

### Data Access Management
- [ ] Implementation of least privilege principle for data access
- [ ] Isolation of sensitive data access environments
- [ ] Encryption of sensitive data during storage and transit
- [ ] Data access revocation mechanisms

### Audit and Traceability
- [ ] Complete logging of sensitive data access
- [ ] Data transfer traceability
- [ ] Audit log retention for required period
- [ ] Alerts on suspicious data access patterns

## 4. Prevention of Autonomous Malicious Actions

### Behavioral Limits
- [ ] Clear definition of agent action boundaries
- [ ] Implementation of behavioral guardrails
- [ ] Restrictions on automatically chained actions
- [ ] "Kill switch" mechanisms to interrupt agent actions

### Supervision and Control
- [ ] Real-time monitoring of action sequences
- [ ] Validation mechanisms for high-risk actions
- [ ] Ability to cancel or rollback executed actions
- [ ] Administrative interfaces for agent supervision

### Testing and Simulation
- [ ] Test scenarios simulating malicious actions
- [ ] Regular evaluation of security boundaries
- [ ] Incident response exercises involving AI agents
- [ ] AI agent-specific red team tests

## 5. Code Execution Security

### Isolation and Sandboxing
- [ ] Code execution in an isolated environment (sandbox)
- [ ] Restrictions on accessible system resources (CPU, memory, network)
- [ ] Execution privilege isolation
- [ ] Expiration mechanisms for code execution sessions

### Code Validation and Analysis
- [ ] Static analysis of generated code before execution
- [ ] Validation of potentially dangerous code patterns
- [ ] Restriction of accessible libraries and functions
- [ ] Secure compilation/transpilation mechanisms

### Execution Monitoring
- [ ] Real-time monitoring of code execution
- [ ] Metrics on resource usage
- [ ] Detection of abnormal behaviors during execution
- [ ] Detailed logging of code execution operations

## 6. General Application Security

### Authentication and Authorization
- [ ] Robust authentication mechanisms for users
- [ ] Fine-grained authorization management for agent interaction
- [ ] Password policies compliant with best practices
- [ ] Implementation of multi-factor authentication when appropriate

### Communication Security
- [ ] Encryption of communications between agent and external services
- [ ] SSL/TLS certificate validation
- [ ] Protection against Man-in-the-Middle attacks
- [ ] Securing agent API endpoints

### Logging and Audit
- [ ] Complete logging of agent interactions
- [ ] Secure log storage
- [ ] Log anti-tampering mechanisms
- [ ] Post-incident forensic analysis capabilities

### Secret Management
- [ ] Securing API keys and AI model access tokens
- [ ] Regular secret rotation
- [ ] Secure storage of credentials
- [ ] Periodic access review for secrets

## Risk Assessment and Compliance

### Risk Classification
- [ ] Assessment of overall AI agent risk level
- [ ] Classification according to sensitivity of handled data
- [ ] Impact analysis in case of compromise
- [ ] Treatment plan for identified risks

### Regulatory Compliance
- [ ] Compliance with data protection regulations (GDPR, etc.)
- [ ] Documentation of technical and organizational measures
- [ ] Data breach procedures
- [ ] Alignment with applicable security standards (e.g., NIST AI RMF)

### AI Governance
- [ ] Definition of roles and responsibilities for agent security
- [ ] Review and approval process for agent modifications
- [ ] Continuous monitoring and improvement procedures
- [ ] Team training on AI agent-specific risks

## Assessment Results

### Summary by Section

| Section | Implemented | Partial | Not Implemented | N/A | Score |
|---------|------------|---------|----------------|-----|-------|
| 1. Protection Against Prompt Injection | | | | | |
| 2. Protection Against Tool Hijacking | | | | | |
| 3. Protection Against Data Exfiltration | | | | | |
| 4. Prevention of Autonomous Malicious Actions | | | | | |
| 5. Code Execution Security | | | | | |
| 6. General Application Security | | | | | |
| **TOTAL** | | | | | |

**Global Security Score**: ___ / 100

### Priority Recommendations
1. 
2. 
3. 

### Validation

**Assessed by**: ________________________ **Date**: August 20, 2025  
**Validated by**: ________________________ **Date**: ______________  
**Next Scheduled Assessment**: ______________

---

## Checklist Usage Guide

### Assessment Method
- **✅ Implemented (I)**: The measure is fully implemented and tested
- **⚠️ Partial (P)**: The measure is partially implemented or in progress
- **❌ Not Implemented (N)**: The measure is not implemented
- **N/A Not Applicable**: The measure does not apply to the context

### Score Calculation
1. For each section, calculate the percentage of compliant measures (C)
2. Weight each section according to its relative importance
3. Calculate the global score out of 100

### Recommended Actions by Score
- **90-100**: Excellence in security, maintain and continuously improve
- **70-89**: Good level, resolve identified gaps
- **50-69**: Average level, action required on identified priorities
- **0-49**: Insufficient level, immediate action necessary

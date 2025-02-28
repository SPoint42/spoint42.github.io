---
title:  "🗺️ OWASP ASVS / SOC2 mapping"
date:   2025-02-25 11:00:00 +0100
categories: 
 - security 
 - OWASP 
 - SOC2
 - OWASP ASVS
lang : french
layout: post
last_modified_at: 2025-02-28
---

Dans le cadre des développements autour d'applications modernes vous avez surement vu passer les références à des normes de 
sécurité telles que [SOC2](https://www.aicpa.org/interestareas/frc/assuranceadvisoryservices/aicpasoc2report.html) (bien 
que SOC2 ne soit pas une réelle norme de sécurité ) et [ISO27000](https://www.iso.org/fr/isoiec-27001-information-security.html). 


<div style="border: 2px solid #ddd; padding: 15px; border-radius: 5px;">
  💡 <B>SOC 2</B> est une norme de sécurité des informations qui évalue les contrôles de sécurité d'une organisation en fonction de cinq critères :
<ul>
<li>sécurité, </li>
<li>disponibilité, </li>
<li>intégrité du traitement, </li>
<li>confidentialité</li>
<li>vie privée.</li>
</ul>
 Elle est proposée par <a href="https://www.aicpa.org">l'American Institute of Certified Public Accountants (AICPA)</a>et est souvent utilisée pour évaluer la sécurité des fournisseurs de services cloud et des entreprises technologiques.
</div>

Ces normes sont de plus en plus demandées par les clients pour garantir la sécurité des données et des systèmes.
 A ce titre, il est intéressant de vous proposer un mapping entre le guide
[OWASP ASVS (Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)) et les 
contrôles de sécurité SOC 2 que j'ai pu établir rapidement récemment. 

Cela permet de mieux comprendre comment les bonnes pratiques de sécurité d'OWASP peuvent être mises en œuvre pour répondre aux exigences de SOC 2.


### 🚧 Mapping is  currently under construction. Please check back later for updates! 🚧

|--------------------|-------------------------------------|---------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| **Category**       | **SOC 2 Control**                   | **Description**                                                                 | **OWASP ASVS Requirement**                                                                                                                          | **OWASP ressources**                                                                                                              |
|--------------------|-------------------------------------|---------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| **Security**       | Logical Access Controls (CC6.1)     | Restrict access to systems and data to authorized users.                       | [ASVS-2 Authentication](https://github.com/OWASP/ASVS/blob/master/4.0/en/0x11-V2-Authentication.md)                                                 | [Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)                      |
|                    | System Security Settings (CC6.2)    | Implement security settings to protect against unauthorized access.            | [ASVS-14 Security Configuration](https://github.com/OWASP/ASVS/blob/master/4.0/en/0x22-V14-Config.md)                                               |                                                                                                                                   |
|                    | Access Monitoring (CC6.3)           | Monitor and log access to detect unauthorized activities.                      | [ASVS-7 Logging and Monitoring](https://github.com/OWASP/ASVS/blob/master/4.0/en/0x15-V7-Error-Logging.md)                                          | [Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)                                    |
|                    | Intrusion Detection (CC6.4)         | Detect and respond to intrusions.                                              | [ASVS-14 Security Configuration](https://github.com/OWASP/ASVS/blob/master/4.0/en/0x22-V14-Config.md)                                               |                                                                                                                                   |
|                    | Firewall Configuration (CC6.5)      | Use firewalls to protect the network perimeter.                                | [ASVS-1.14.1  Network Security](https://github.com/OWASP/ASVS/blob/master/4.0/en/0x10-V1-Architecture.md#v114-configuration-architecture)           | [Attack Surface Analysis Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html)    |
|                    | Vulnerability Management (CC6.6)    | Regularly scan for and remediate vulnerabilities.                              | [ASVS-14.1.1 Vulnerability Scanning, ASVS-14.3 Unintended Security Disclosure](https://github.com/OWASP/ASVS/blob/master/4.0/en/0x22-V14-Config.md) | [Vulnerability Disclosure](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerability_Disclosure_Cheat_Sheet.html   )           |
|                    | Security Incident Response (CC6.7)  | Plan and respond to security incidents.                                        | [ASVS-14.3 Unintended Security Disclosure](https://github.com/OWASP/ASVS/blob/master/4.0/en/0x22-V14-Config.md)                                     | [Vulnerability Disclosure](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerability_Disclosure_Cheat_Sheet.html   )           |
| **Availability**   | Business Continuity Plan (CC7.1)    | Ensure business continuity during disruptions.                                 |                                                                                                                                                     |                                                                                                                                   |
|                    | Disaster Recovery Plan (CC7.2)      | Restore services quickly after disruptions.                                    |                                                                                                                                                     |                                                                                                                                   |
|                    | Performance Monitoring (CC7.3)      | Monitor system performance to ensure availability.                             | [ASVS-7 Logging and Monitoring](https://github.com/OWASP/ASVS/blob/master/4.0/en/0x15-V7-Error-Logging.md)                                          | [Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)                                    |
| **Confidentiality**| Data Encryption (CC8.1)             | Encrypt sensitive data at rest and in transit.                                 | [ASVS-9  Communication](https://github.com/OWASP/ASVS/blob/master/4.0/en/0x17-V9-Communications.md)                                                 | [Transport Layer Security  Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html) |
|                    | Key Management (CC8.2)              | Manage cryptographic keys securely.                                            | [ASVS-6.4  Key Management](https://github.com/OWASP/ASVS/blob/master/4.0/en/0x14-V6-Cryptography.md)                                                | [Key Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html)                      |
| **Processing Integrity** | Input Validation (CC9.1)         | Validate inputs to prevent injection attacks and other vulnerabilities.        | [ASVS-5  Input Validation](https://github.com/OWASP/ASVS/blob/master/4.0/en/0x13-V5-Validation-Sanitization-Encoding.md)                            | [Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)                  |
|                    | Version Control (CC9.2)             | Manage changes to code and configurations.                                     | [ASVS-14.1  Build & Deploy](https://github.com/OWASP/ASVS/blob/master/4.0/en/0x22-V14-Config.md)                                                    |                                                                                                                                   |
| **Privacy**        | Personal Data Protection (CC10.1)   | Protect personal data according to privacy policies.                          |                                                                                                                                                     |                                                                                                                                   |
|                    | Security Awareness Training (CC10.2)| Provide regular security awareness training to employees.                     |                                                                                                                                                     |      [OWASP Top10](https://www.owasp.org/Top10)                                                                                                                             |
|                    | Data Minimization (CC10.3)          | Collect and store only necessary personal data.                                |                                                                                                                                                     |                                                                                                                                   |
|                    | Data Retention and Disposal (CC10.4)| Implement policies for data retention and secure disposal.                    |                                                                                                                                                     |                                                                                                                                   |

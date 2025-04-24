---
layout: post
title: "Veille automatisée du 2025-04-24 via Gemini gemini-2.0-flash"
date: 2025-04-24
categories:
    - veille
    - vulnérabilités
    - sécurité
---

# ⚠️Important Security Alerts (CVSS > 7.5)⚠️
🚨 Critical Commvault Command Center Flaw Enables Attackers to Execute Code Remotely
🚨 Vulnérabilité dans Oracle Weblogic (16 avril 2025)

## Table of Contents

*   [🚨 Critical Commvault Command Center Flaw Enables Attackers to Execute Code Remotely](#-critical-commvault-command-center-flaw-enables-attackers-to-execute-code-remotely)
*   [🛡️ Linux io_uring PoC Rootkit Bypasses System Call-Based Threat Detection Tools](#️-linux-io_uring-poc-rootkit-bypasses-system-call-based-threat-detection-tools)
*   [🏥 Automating Zero Trust in Healthcare: From Risk Scoring to Dynamic Policy Enforcement Without Network Redesign](#-automating-zero-trust-in-healthcare-from-risk-scoring-to-dynamic-policy-enforcement-without-network-redesign)
*   [🔥 159 CVEs Exploited in Q1 2025 — 28.3% Within 24 Hours of Disclosure](#-159-cves-exploited-in-q1-2025--283-within-24-hours-of-disclosure)
*   [🎣 Darcula Adds GenAI to Phishing Toolkit, Lowering the Barrier for Cybercriminals](#-darcula-adds-genai-to-phishing-toolkit-lowering-the-barrier-for-cybercriminals)
*   [💬 WhatsApp Adds Advanced Chat Privacy to Blocks Chat Exports and Auto-Downloads](#-whatsapp-adds-advanced-chat-privacy-to-blocks-chat-exports-and-auto-downloads)
*   [💰 DPRK Hackers Steal $137M from TRON Users in Single-Day Phishing Attack](#-dprk-hackers-steal-137m-from-tron-users-in-single-day-phishing-attack)
*   [🇮🇷 Iran-Linked Hackers Target Israel with MURKYTOUR Malware via Fake Job Campaign](#-iran-linked-hackers-target-israel-with-murkytour-malware-via-fake-job-campaign)
*   [📱 Android Spyware Disguised as Alpine Quest App Targets Russian Military Devices](#-android-spyware-disguised-as-alpine-quest-app-targets-russian-military-devices)
*   [🌐 Three Reasons Why the Browser is Best for Stopping Phishing Attacks](#-three-reasons-why-the-browser-is-best-for-stopping-phishing-attacks)
*   [⚠️ Multiples vulnérabilités dans Mattermost Server (18 mars 2025)](#-multiples-vulnrabilit%C3%A9s-dans-mattermost-server-18-mars-2025)
*   [⚠️ Vulnérabilité dans Mattermost Server (19 mars 2025)](#-vulnrabilit%C3%A9-dans-mattermost-server-19-mars-2025)
*   [⚠️ Multiples vulnérabilités dans les produits Mattermost (15 avril 2025)](#-multiples-vulnrabilit%C3%A9s-dans-les-produits-mattermost-15-avril-2025)
*   [⚠️ Vulnérabilité dans SolarWinds Serv-U (15 avril 2025)](#-vulnrabilit%C3%A9-dans-solarwinds-serv-u-15-avril-2025)
*   [⚠️ Multiples vulnérabilités dans Oracle MySQL (16 avril 2025)](#-multiples-vulnrabilit%C3%A9s-dans-oracle-mysql-16-avril-2025)
*   [⚠️ Multiples vulnérabilités dans Oracle Java SE (16 avril 2025)](#-multiples-vulnrabilit%C3%A9s-dans-oracle-java-se-16-avril-2025)
*   [⚠️ Multiples vulnérabilités dans Oracle Virtualization (16 avril 2025)](#-multiples-vulnrabilit%C3%A9s-dans-oracle-virtualization-16-avril-2025)
*   [🚨 Vulnérabilité dans Oracle Weblogic (16 avril 2025)](#-vulnrabilit%C3%A9-dans-oracle-weblogic-16-avril-2025)
*   [⚠️ Multiples vulnérabilités dans Oracle PeopleSoft (16 avril 2025)](#-multiples-vulnrabilit%C3%A9s-dans-oracle-peoplesoft-16-avril-2025)
*   [⚠️ Multiples vulnérabilités dans Google Chrome (16 avril 2025)](#-multiples-vulnrabilit%C3%A9s-dans-google-chrome-16-avril-2025)
*   [⚠️ Multiples vulnérabilités dans les produits Atlassian (16 avril 2025)](#-multiples-vulnrabilit%C3%A9s-dans-les-produits-atlassian-16-avril-2025)
*   [⚠️ Multiples vulnérabilités dans Oracle Systems (16 avril 2025)](#-multiples-vulnrabilit%C3%A9s-dans-oracle-systems-16-avril-2025)
*   [⚠️ Multiples vulnérabilités dans Oracle Database Server (16 avril 2025)](#-multiples-vulnrabilit%C3%A9s-dans-oracle-database-server-16-avril-2025)
*   [⚠️ Multiples vulnérabilités dans les produits Mozilla (16 avril 2025)](#-multiples-vulnrabilit%C3%A9s-dans-les-produits-mozilla-16-avril-2025)
*   [⚠️ Vulnérabilité dans les produits Microsoft (16 avril 2025)](#-vulnrabilit%C3%A9-dans-les-produits-microsoft-16-avril-2025)
*   [🚌 Transports urbains - État de la menace informatique (17 avril 2025)](#-transports-urbains---%C3%A9tat-de-la-menace-informatique-17-avril-2025)
*   [⚠️ Vulnérabilité dans SonicWall Connect Tunnel (17 avril 2025)](#-vulnrabilit%C3%A9-dans-sonicwall-connect-tunnel-17-avril-2025)
*   [⚠️ Multiples vulnérabilités dans Tenable Security Center (17 avril 2025)](#-multiples-vulnrabilit%C3%A9s-dans-tenable-security-center-17-avril-2025)
*   [⚠️ Vulnérabilité dans Cisco Webex App (17 avril 2025)](#-vulnrabilit%C3%A9-dans-cisco-webex-app-17-avril-2025)
*   [🐛 CVE-2025-3857 - Infinite loop condition in Amazon.IonDotnet](#cve-2025-3857---infinite-loop-condition-in-amazoniondotnet)
*   [🛠️ Issue with AWS SAM CLI (CVE-2025-3047, CVE-2025-3048)](#️-issue-with-aws-sam-cli-cve-2025-3047-cve-2025-3048)
*   [🇰🇵 Lazarus Hits 6 South Korean Firms via Cross EX, Innorix Flaws and ThreatNeedle Malware](#-lazarus-hits-6-south-korean-firms-via-cross-ex-innorix-flaws-and-threatneedle-malware)
        
## 🚨 Critical Commvault Command Center Flaw Enables Attackers to Execute Code Remotely
Une faille de sécurité critique a été découverte dans Commvault Command Center, permettant l'exécution de code arbitraire à distance sur les installations affectées. La vulnérabilité, référencée CVE-2025-34028, a un score CVSS de 9.0 sur 10.0.

*   🐛 CVE : [CVE-2025-34028](https://www.cve.org/CVERecord?id=CVE-2025-34028)
*   ⭐ CVSS : 9.0

## 🛡️ Linux io_uring PoC Rootkit Bypasses System Call-Based Threat Detection Tools
Des chercheurs en cybersécurité ont démontré un proof-of-concept (PoC) de rootkit appelé Curing qui exploite un mécanisme d'E/S asynchrone Linux appelé io_uring pour contourner la surveillance traditionnelle des appels système. ARMO a déclaré que cela provoque un "angle mort majeur dans les outils de sécurité d'exécution Linux". "Ce mécanisme permet à une application utilisateur d'effectuer diverses actions sans utiliser les appels système", a déclaré la société.

## 🏥 Automating Zero Trust in Healthcare: From Risk Scoring to Dynamic Policy Enforcement Without Network Redesign
Les organisations de soins de santé sont confrontées à des défis de cybersécurité sans précédent en 2025. Avec des environnements de technologie opérationnelle (OT) de plus en plus ciblés et la convergence des systèmes informatiques et médicaux créant une surface d'attaque élargie, les approches de sécurité traditionnelles s'avèrent inadéquates. Selon des statistiques récentes, le secteur de la santé.

## 🔥 159 CVEs Exploited in Q1 2025 — 28.3% Within 24 Hours of Disclosure
Pas moins de 159 identifiants CVE ont été signalés comme exploités dans la nature au premier trimestre de 2025, contre 151 au quatrième trimestre de 2024. "Nous continuons de voir des vulnérabilités exploitées à un rythme rapide, 28,3 % des vulnérabilités étant exploitées dans les 24 heures suivant leur divulgation CVE", a déclaré VulnCheck dans un rapport partagé avec The Hacker News. Cela se traduit par 45 failles de sécurité qui ont été militarisées.

## 🎣 Darcula Adds GenAI to Phishing Toolkit, Lowering the Barrier for Cybercriminals
Les acteurs de la menace derrière la plateforme de phishing-as-a-service (PhaaS) Darcula ont publié de nouvelles mises à jour de leur suite de cybercriminalité avec des capacités d'intelligence artificielle générative (GenAI). "Cet ajout abaisse la barrière technique à la création de pages de phishing, permettant aux criminels moins avertis en technologie de déployer des escroqueries personnalisées en quelques minutes", a déclaré Netcraft dans un nouveau rapport partagé avec The Hacker News.

## 💬 WhatsApp Adds Advanced Chat Privacy to Blocks Chat Exports and Auto-Downloads
WhatsApp a introduit une couche supplémentaire de confidentialité appelée Advanced Chat Privacy qui permet aux utilisateurs d'empêcher les participants de partager le contenu d'une conversation dans les chats et groupes traditionnels. "Ce nouveau paramètre disponible dans les chats et les groupes aide à empêcher les autres de sortir du contenu de WhatsApp lorsque vous souhaitez une confidentialité supplémentaire", a déclaré WhatsApp dans un communiqué. La fonctionnalité optionnelle.

## 💰 DPRK Hackers Steal $137M from TRON Users in Single-Day Phishing Attack
Plusieurs groupes d'activités de menace liés à la Corée du Nord (ou République populaire démocratique de Corée ou RPDC) ont été liés à des attaques ciblant des organisations et des individus dans l'espace Web3 et des crypto-monnaies. "L'accent mis sur Web3 et les crypto-monnaies semble être principalement motivé financièrement en raison des lourdes sanctions qui ont été imposées à la Corée du Nord", a déclaré Mandiant, propriété de Google.

## 🇮🇷 Iran-Linked Hackers Target Israel with MURKYTOUR Malware via Fake Job Campaign
L'acteur de menace lié à l'Iran connu sous le nom d'UNC2428 a été observé en train de livrer une backdoor connue sous le nom de MURKYTOUR dans le cadre d'une campagne d'ingénierie sociale sur le thème de l'emploi ciblant Israël en octobre 2024. Mandiant, propriété de Google, a décrit UNC2428 comme un acteur de menace aligné sur l'Iran qui se livre à des opérations liées à l'espionnage cybernétique. On dit que l'ensemble d'intrusion a distribué le malware via un "complexe.

## 📱 Android Spyware Disguised as Alpine Quest App Targets Russian Military Devices
Des chercheurs en cybersécurité ont révélé que le personnel militaire russe est la cible d'une nouvelle campagne malveillante qui distribue des logiciels espions Android sous le couvert du logiciel de cartographie Alpine Quest. "Les attaquants cachent ce cheval de Troie à l'intérieur d'un logiciel de cartographie Alpine Quest modifié et le distribuent de diverses manières, notamment via l'un des catalogues d'applications Android russes", a déclaré Doctor Web dans un.

## 🌐 Three Reasons Why the Browser is Best for Stopping Phishing Attacks
Les attaques de phishing restent un énorme défi pour les organisations en 2025. En fait, avec des attaquants de plus en plus.

## ⚠️ Multiples vulnérabilités dans Mattermost Server (18 mars 2025)
De multiples vulnérabilités ont été découvertes dans Mattermost Server. Elles permettent à un attaquant de provoquer un problème de sécurité non spécifié par l'éditeur.

## ⚠️ Vulnérabilité dans Mattermost Server (19 mars 2025)
Une vulnérabilité a été découverte dans Mattermost Server. Elle permet à un attaquant de provoquer un problème de sécurité non spécifié par l'éditeur.

## ⚠️ Multiples vulnérabilités dans les produits Mattermost (15 avril 2025)
De multiples vulnérabilités ont été découvertes dans les produits Mattermost. Elle permet à un attaquant de provoquer un problème de sécurité non spécifié par l'éditeur.

## ⚠️ Vulnérabilité dans SolarWinds Serv-U (15 avril 2025)
Une vulnérabilité a été découverte dans SolarWinds Serv-U. Elle permet à un attaquant de provoquer une injection de code indirecte à distance (XSS).

## ⚠️ Multiples vulnérabilités dans Oracle MySQL (16 avril 2025)
De multiples vulnérabilités ont été découvertes dans Oracle MySQL. Elles permettent à un attaquant de provoquer un déni de service à distance, une atteinte à la confidentialité des données et une atteinte à l'intégrité des données.

## ⚠️ Multiples vulnérabilités dans Oracle Java SE (16 avril 2025)
De multiples vulnérabilités ont été découvertes dans Oracle Java SE. Certaines d'entre elles permettent à un attaquant de provoquer une exécution de code arbitraire à distance, un déni de service à distance et une atteinte à la confidentialité des données.

## ⚠️ Multiples vulnérabilités dans Oracle Virtualization (16 avril 2025)
De multiples vulnérabilités ont été découvertes dans Oracle Virtualization. Elles permettent à un attaquant de provoquer une atteinte à la confidentialité des données, une atteinte à l'intégrité des données et un déni de service.

## 🚨 Vulnérabilité dans Oracle Weblogic (16 avril 2025)
Une vulnérabilité a été découverte dans Oracle Weblogic. Elle permet à un attaquant de provoquer une exécution de code arbitraire à distance.

## ⚠️ Multiples vulnérabilités dans Oracle PeopleSoft (16 avril 2025)
De multiples vulnérabilités ont été découvertes dans Oracle PeopleSoft. Elles permettent à un attaquant de provoquer un déni de service à distance, une atteinte à la confidentialité des données et une atteinte à l'intégrité des données.

## ⚠️ Multiples vulnérabilités dans Google Chrome (16 avril 2025)
De multiples vulnérabilités ont été découvertes dans Google Chrome. Elles permettent à un attaquant de provoquer un problème de sécurité non spécifié par l'éditeur.

## ⚠️ Multiples vulnérabilités dans les produits Atlassian (16 avril 2025)
De multiples vulnérabilités ont été découvertes dans les produits Atlassian. Elles permettent à un attaquant de provoquer un déni de service à distance et un contournement de la politique de sécurité.

## ⚠️ Multiples vulnérabilités dans Oracle Systems (16 avril 2025)
De multiples vulnérabilités ont été découvertes dans Oracle Systems. Elles permettent à un attaquant de provoquer une exécution de code arbitraire, une atteinte à la confidentialité des données et une atteinte à l'intégrité des données.

## ⚠️ Multiples vulnérabilités dans Oracle Database Server (16 avril 2025)
De multiples vulnérabilités ont été découvertes dans Oracle Database Server. Elles permettent à un attaquant de provoquer un déni de service à distance, une atteinte à la confidentialité des données et une atteinte à l'intégrité des données.

## ⚠️ Multiples vulnérabilités dans les produits Mozilla (16 avril 2025)
De multiples vulnérabilités ont été découvertes dans les produits Mozilla. Elles permettent à un attaquant de provoquer une atteinte à la confidentialité des données, un contournement de la politique de sécurité et un problème de sécurité non spécifié par l'éditeur.

## ⚠️ Vulnérabilité dans les produits Microsoft (16 avril 2025)
Une vulnérabilité a été découverte dans les produits Microsoft. Elle permet à un attaquant de provoquer une atteinte à la confidentialité des données.

## 🚌 Transports urbains - État de la menace informatique (17 avril 2025)
La menace à l’encontre des entités des transports urbains cible des entreprises de toutes les tailles dans le monde entier qui opèrent différents modes de transport. La convergence de technologies industrielles et bureautique, l’interconnexion de réseaux informatiques de grande taille composés...

## ⚠️ Vulnérabilité dans SonicWall Connect Tunnel (17 avril 2025)
Une vulnérabilité a été découverte dans SonicWall Connect Tunnel. Elle permet à un attaquant de provoquer une atteinte à l'intégrité des données.

## ⚠️ Multiples vulnérabilités dans Tenable Security Center (17 avril 2025)
De multiples vulnérabilités ont été découvertes dans Tenable Security Center. Certaines d'entre elles permettent à un attaquant de provoquer une exécution de code arbitraire à distance, un déni de service à distance et une atteinte à la confidentialité des données.

## ⚠️ Vulnérabilité dans Cisco Webex App (17 avril 2025)
Une vulnérabilité a été découverte dans C

## 🐛 CVE-2025-3857 - Infinite loop condition in Amazon.IonDotnet
Une condition de boucle infinie a été identifiée dans Amazon.IonDotnet. Lors de la lecture de données Ion binaires via cette bibliothèque à l'aide de la classe RawBinaryReader, Amazon.IonDotnet ne vérifie pas le nombre d'octets lus à partir du flux sous-jacent lors de la désérialisation du format binaire. Si les données Ion sont malformées ou tronquées, cela déclenche une condition de boucle infinie qui pourrait potentiellement entraîner un déni de service. La correction est incluse dans la version 1.3.1.

*   🐛 CVE : [CVE-2025-3857](https://www.cve.org/CVERecord?id=CVE-2025-3857)

## 🛠️ Issue with AWS SAM CLI (CVE-2025-3047, CVE-2025-3048)
Des problèmes ont été identifiés dans AWS SAM CLI. Une correction a été publiée et il est recommandé de mettre à niveau vers la dernière version.
* CVE-2025-3047: Lors de l'exécution du processus de build AWS SAM CLI avec Docker et que des liens symboliques sont inclus dans les fichiers de build, l'environnement de conteneur permet à un utilisateur d'accéder aux fichiers privilégiés sur l'hôte en tirant parti des autorisations élevées accordées à l'outil.
* CVE-2025-3048: Après avoir terminé une build avec AWS SAM CLI qui inclut des liens symboliques, le contenu de ces liens symboliques est copié dans le cache de l'espace de travail local en tant que fichiers ou répertoires réguliers.

*   🐛 CVE : [CVE-2025-3047](https://www.cve.org/CVERecord?id=CVE-2025-3047), [CVE-2025-3048](https://www.cve.org/CVERecord?id=CVE-2025-3048)

## 🇰🇵 Lazarus Hits 6 South Korean Firms via Cross EX, Innorix Flaws and ThreatNeedle Malware
Au moins six organisations en Corée du Sud ont été ciblées par le prolifique groupe Lazarus lié à la Corée du Nord dans le cadre d'une campagne baptisée Operation SyncHole. L'activité a ciblé les industries sud-coréennes des logiciels, de l'informatique, de la finance, de la fabrication de semi-conducteurs et des télécommunications, selon un rapport de Kaspersky publié aujourd'hui. La première preuve de compromission a été détectée pour la première fois dans

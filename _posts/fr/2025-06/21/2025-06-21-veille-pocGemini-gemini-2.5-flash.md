---
layout: post
title: "Veille automatisée du 2025-06-21 pour pocGemini via Gemini gemini-2.5-flash"
date: 2025-06-21
categories:
    - veille
    - vulnérabilités
    - sécurité
    - pocGemini
    - gemini-2.5-flash
---
# ⚠️Alertes de Sécurité Importantes (CVSS > 7.5)⚠️
🚨 Vulnérabilité critique de Veeam CVE-2025-23121 avec un score CVSS de 9.9

## Table des Matières

*   [🚨 Vulnérabilités multiples dans les produits IBM (20 juin 2025)](#vulnérabilités-multiples-dans-les-produits-ibm-20-juin-2025)
*   [🚨 Multiples vulnérabilités dans Microsoft Edge (20 juin 2025)](#multiples-vulnérabilités-dans-microsoft-edge-20-juin-2025)
*   [🚨 Multiples vulnérabilités dans le noyau Linux de SUSE (20 juin 2025)](#multiples-vulnérabilités-dans-le-noyau-linux-de-suse-20-juin-2025)
*   [🚨 Vulnérabilité dans les produits Microsoft (20 juin 2025)](#vulnérabilité-dans-les-produits-microsoft-20-juin-2025)
*   [🚨 Multiples vulnérabilités dans les produits Citrix (20 juin 2025)](#multiples-vulnérabilités-dans-les-produits-citrix-20-juin-2025)
*   [🚨 Vulnérabilité d'exécution de code à distance dans les fichiers de raccourci Internet CVE-2025-33053](#vulnérabilité-d'exécution-de-code-à-distance-dans-les-fichiers-de-raccourci-internet-cve-2025-33053)
*   [🚨 Nouvelles failles Linux permettent un accès Root complet via PAM et Udisks](#nouvelles-failles-linux-permettent-un-accès-root-complet-via-pam-et-udisks)
*   [🚨 Multiples vulnérabilités dans Mattermost Server (19 juin 2025)](#multiples-vulnérabilités-dans-mattermost-server-19-juin-2025)
*   [🚨 Multiples vulnérabilités dans VMware Tanzu (19 juin 2025)](#multiples-vulnérabilités-dans-vmware-tanzu-19-juin-2025)
*   [🚨 Vulnérabilité dans Cisco Meraki MX (19 juin 2025)](#vulnérabilité-dans-cisco-meraki-mx-19-juin-2025)
*   [🚨 Multiples vulnérabilités dans ClamAV (19 juin 2025)](#multiples-vulnérabilités-dans-clamav-19-juin-2025)
*   [🚨 Veeam corrige CVE-2025-23121: Vulnérabilité RCE critique évaluée à 9.9 CVSS](#veeam-corrige-cve-2025-23121-vulnérabilité-rce-critique-évaluée-à-99-cvss)
*   [🚨 La CISA alerte sur l'exploitation active d'une vulnérabilité d'escalade de privilèges du noyau Linux](#la-cisa-alerte-sur-l'exploitation-active-d'une-vulnérabilité-d'escalade-de-privilèges-du-noyau-linux)
*   [🚨 Multiples vulnérabilités dans les produits Veeam (18 juin 2025)](#multiples-vulnérabilités-dans-les-produits-veeam-18-juin-2025)
*   [🚨 Multiples vulnérabilités dans Moodle (18 juin 2025)](#multiples-vulnérabilités-dans-moodle-18-juin-2025)
*   [🚨 Multiples vulnérabilités dans Synacor Zimbra Collaboration (18 juin 2025)](#multiples-vulnérabilités-dans-synacor-zimbra-collaboration-18-juin-2025)
*   [🚨 Multiples vulnérabilités dans les produits Atlassian (18 juin 2025)](#multiples-vulnérabilités-dans-les-produits-atlassian-18-juin-2025)
*   [🚨 Multiples vulnérabilités dans Google Chrome (18 juin 2025)](#multiples-vulnérabilités-dans-google-chrome-18-juin-2025)
*   [🚨 Google Chrome Zero-Day CVE-2025-2783 exploité par TaxOff pour déployer le backdoor Trinper](#google-chrome-zero-day-cve-2025-2783-exploité-par-taxoff-pour-déployer-le-backdoor-trinper)
*   [🚨 Une faille LangSmith pourrait exposer les clés OpenAI et les données utilisateur via des agents malveillants](#une-faille-langsmith-pourrait-exposer-les-clés-openai-et-les-données-utilisateur-via-des-agents-malveillants)
*   [🚨 Des hackers exploitent une faille critique de Langflow pour lancer le Botnet Flodrix](#des-hackers-exploitent-une-faille-critique-de-langflow-pour-lancer-le-botnet-flodrix)
*   [🚨 Nouvelle variante du botnet Flodrix exploite une faille RCE du serveur Langflow AI pour lancer des attaques DDoS](#nouvelle-variante-du-botnet-flodrix-exploite-une-faille-rce-du-serveur-langflow-ai-pour-lancer-des-attaques-ddos)
*   [🚨 La faille CVE-2023-33538 du routeur TP-Link sous exploitation active, la CISA émet une alerte immédiate](#la-faille-cve-2023-33538-du-routeur-tp-link-sous-exploitation-active-la-cisa-émet-une-alerte-immédiate)
*   [🚨 Mot de passe "b" codé en dur dans Sitecore XP provoque un risque RCE majeur](#mot-de-passe-"b"-codé-en-dur-dans-sitecore-xp-provoque-un-risque-rce-majeur)
*   [🚨 Vulnérabilité de divulgation d'informations M365 Copilot CVE-2025-32711](#vulnérabilité-de-divulgation-d'informations-m365-copilot-cve-2025-32711)
*   [🚨 Vulnérabilité de contournement de fonctionnalité de sécurité Visual Studio Code CVE-2025-21264](#vulnérabilité-de-contournement-de-fonctionnalité-de-sécurité-visual-studio-code-cve-2025-21264)

---

### 🚨 Vulnérabilités multiples dans les produits IBM (20 juin 2025)
De multiples vulnérabilités ont été découvertes dans les produits IBM. Certaines d'entre elles permettent à un attaquant d'exécuter du code arbitraire, de provoquer un déni de service ou d'obtenir des informations sensibles.
*   🐞 CVE: CERTFR-2025-AVI-0530 ([https://www.cert.ssi.gouv.fr/avis/CERTFR-2025-AVI-0530/](https://www.cert.ssi.gouv.fr/avis/CERTFR-2025-AVI-0530/))
*   📅 PubDate: Fri, 20 Jun 2025 00:00:00

### 🚨 Multiples vulnérabilités dans Microsoft Edge (20 juin 2025)
De multiples vulnérabilités ont été découvertes dans Microsoft Edge. Elles permettent à un attaquant d'exécuter du code arbitraire, de provoquer un déni de service ou d'obtenir des informations sensibles.
*   🐞 CVE: CERTFR-2025-AVI-0526 ([https://www.cert.ssi.gouv.fr/avis/CERTFR-2025-AVI-0526/](https://www.cert.ssi.gouv.fr/avis/CERTFR-2025-AVI-0526/))
*   📅 PubDate: Fri, 20 Jun 2025 00:00:00

### 🚨 Multiples vulnérabilités dans le noyau Linux de SUSE (20 juin 2025)
De multiples vulnérabilités ont été découvertes dans le noyau Linux de SUSE. Certaines d'entre elles permettent à un attaquant d'exécuter du code arbitraire ou de provoquer un déni de service.
*   🐞 CVE: CERTFR-2025-AVI-0529 ([https://www.cert.ssi.gouv.fr/avis/CERTFR-2025-AVI-0529/](https://www.cert.ssi.gouv.fr/avis/CERTFR-2025-AVI-0529/))
*   📅 PubDate: Fri, 20 Jun 2025 00:00:00

### 🚨 Vulnérabilité dans les produits Microsoft (20 juin 2025)
Une vulnérabilité a été découverte dans les produits Microsoft. Elle permet à un attaquant de provoquer un déni de service.
*   🐞 CVE: CERTFR-2025-AVI-0527 ([https://www.cert.ssi.gouv.fr/avis/CERTFR-2025-AVI-0527/](https://www.cert.ssi.gouv.fr/avis/CERTFR-2025-AVI-0527/))
*   📅 PubDate: Fri, 20 Jun 2025 00:00:00

### 🚨 Multiples vulnérabilités dans les produits Citrix (20 juin 2025)
De multiples vulnérabilités ont été découvertes dans les produits Citrix. Elles permettent à un attaquant d'exécuter du code arbitraire, de provoquer un déni de service ou d'obtenir des informations sensibles.
*   🐞 CVE: CERTFR-2025-AVI-0528 ([https://www.cert.ssi.gouv.fr/avis/CERTFR-2025-AVI-0528/](https://www.cert.ssi.gouv.fr/avis/CERTFR-2025-AVI-0528/))
*   📅 PubDate: Fri, 20 Jun 2025 00:00:00

### 🚨 Vulnérabilité d'exécution de code à distance dans les fichiers de raccourci Internet CVE-2025-33053
Correction de la description et du titre de la CVE. Ceci est un changement d'information uniquement.
*   🐞 CVE: CVE-2025-33053 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33053](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33053))
*   📅 PubDate: Thu, 19 Jun 2025 07:00:00

### 🚨 Nouvelles failles Linux permettent un accès Root complet via PAM et Udisks
Les chercheurs en cybersécurité ont découvert deux failles d'escalade de privilèges locales (LPE) qui pourraient être exploitées pour obtenir un accès root complet sur les principales distributions Linux.
*   📅 PubDate: Thu, 19 Jun 2025 03:33:00

### 🚨 Multiples vulnérabilités dans Mattermost Server (19 juin 2025)
De multiples vulnérabilités ont été découvertes dans Mattermost Server. Elles permettent à un attaquant d'exécuter du code arbitraire ou d'obtenir des informations sensibles.
*   🐞 CVE: CERTFR-2025-AVI-0525 ([https://www.cert.ssi.gouv.fr/avis/CERTFR-2025-AVI-0525/](https://www.cert.ssi.gouv.fr/avis/CERTFR-2025-AVI-0525/))
*   📅 PubDate: Thu, 19 Jun 2025 00:00:00

### 🚨 Multiples vulnérabilités dans VMware Tanzu (19 juin 2025)
De multiples vulnérabilités ont été découvertes dans VMware Tanzu. Elles permettent à un attaquant de provoquer un déni de service ou d'obtenir des informations sensibles.
*   🐞 CVE: CERTFR-2025-AVI-0524 ([https://www.cert.ssi.gouv.fr/avis/CERTFR-2025-AVI-0524/](https://www.cert.ssi.gouv.fr/avis/CERTFR-2025-AVI-0524/))
*   📅 PubDate: Thu, 19 Jun 2025 00:00:00

### 🚨 Vulnérabilité dans Cisco Meraki MX (19 juin 2025)
Une vulnérabilité a été découverte dans Cisco Meraki MX. Elle permet à un attaquant de provoquer un déni de service.
*   🐞 CVE: CERTFR-2025-AVI-0523 ([https://www.cert.ssi.gouv.fr/avis/CERTFR-2025-AVI-0523/](https://www.cert.ssi.gouv.fr/avis/CERTFR-2025-AVI-0523/))
*   📅 PubDate: Thu, 19 Jun 2025 00:00:00

### 🚨 Multiples vulnérabilités dans ClamAV (19 juin 2025)
De multiples vulnérabilités ont été découvertes dans ClamAV. Certaines d'entre elles permettent à un attaquant d'exécuter du code arbitraire ou de provoquer un déni de service.
*   🐞 CVE: CERTFR-2025-AVI-0522 ([https://www.cert.ssi.gouv.fr/avis/CERTFR-2025-AVI-0522/](https://www.cert.ssi.gouv.fr/avis/CERTFR-2025-AVI-0522/))
*   📅 PubDate: Thu, 19 Jun 2025 00:00:00

### 🚨 Veeam corrige CVE-2025-23121: Vulnérabilité RCE critique évaluée à 9.9 CVSS
Veeam a déployé des correctifs pour contenir une faille de sécurité critique impactant son produit Backup & Replication.
*   🐞 CVE: CVE-2025-23121 ([https://thehackernews.com/2025/06/veeam-patches-cve-2025-23121-critical.html](https://thehackernews.com/2025/06/veeam-patches-cve-2025-23121-critical.html))
*   💯 CVSS: 9.9
*   📅 PubDate: Wed, 18 Jun 2025 05:49:00

### 🚨 La CISA alerte sur l'exploitation active d'une vulnérabilité d'escalade de privilèges du noyau Linux
L'agence américaine de cybersécurité et de sécurité des infrastructures (CISA) a ajouté mardi une faille de sécurité activement exploitée au catalogue.
*   📅 PubDate: Wed, 18 Jun 2025 06:43:00

### 🚨 Multiples vulnérabilités dans les produits Veeam (18 juin 2025)
De multiples vulnérabilités ont été découvertes dans les produits Veeam. Elles permettent à un attaquant d'exécuter du code arbitraire, de provoquer un déni de service ou d'obtenir des informations sensibles.
*   🐞 CVE: CERTFR-2025-AVI-0517 ([https://www.cert.ssi.gouv.fr/avis/CERTFR-2025-AVI-0517/](https://www.cert.ssi.gouv.fr/avis/CERTFR-2025-AVI-0517/))
*   📅 PubDate: Wed, 18 Jun 2025 00:00:00

### 🚨 Multiples vulnérabilités dans Moodle (18 juin 2025)
De multiples vulnérabilités ont été découvertes dans Moodle. Certaines d'entre elles permettent à un attaquant d'exécuter du code arbitraire ou d'obtenir des informations sensibles.
*   🐞 CVE: CERTFR-2025-AVI-0519 ([https://www.cert.ssi.gouv.fr/avis/CERTFR-2025-AVI-0519/](https://www.cert.ssi.gouv.fr/avis/CERTFR-2025-AVI-0519/))
*   📅 PubDate: Wed, 18 Jun 2025 00:00:00

### 🚨 Multiples vulnérabilités dans Synacor Zimbra Collaboration (18 juin 2025)
De multiples vulnérabilités ont été découvertes dans Synacor Zimbra Collaboration. Elles permettent à un attaquant d'exécuter du code arbitraire, de provoquer un déni de service ou d'obtenir des informations sensibles.
*   🐞 CVE: CERTFR-2025-AVI-0521 ([https://www.cert.ssi.gouv.fr/avis/CERTFR-2025-AVI-0521/](https://www.cert.ssi.gouv.fr/avis/CERTFR-2025-AVI-0521/))
*   📅 PubDate: Wed, 18 Jun 2025 00:00:00

### 🚨 Multiples vulnérabilités dans les produits Atlassian (18 juin 2025)
De multiples vulnérabilités ont été découvertes dans les produits Atlassian. Elles permettent à un attaquant d'exécuter du code arbitraire, de provoquer un déni de service ou d'obtenir des informations sensibles.
*   🐞 CVE: CERTFR-2025-AVI-0520 ([https://www.cert.ssi.gouv.fr/avis/CERTFR-2025-AVI-0520/](https://www.cert.ssi.gouv.fr/avis/CERTFR-2025-AVI-0520/))
*   📅 PubDate: Wed, 18 Jun 2025 00:00:00

### 🚨 Multiples vulnérabilités dans Google Chrome (18 juin 2025)
De multiples vulnérabilités ont été découvertes dans Google Chrome. Elles permettent à un attaquant d'exécuter du code arbitraire ou de provoquer un déni de service.
*   🐞 CVE: CERTFR-2025-AVI-0518 ([https://www.cert.ssi.gouv.fr/avis/CERTFR-2025-AVI-0518/](https://www.cert.ssi.gouv.fr/avis/CERTFR-2025-AVI-0518/))
*   📅 PubDate: Wed, 18 Jun 2025 00:00:00

### 🚨 Google Chrome Zero-Day CVE-2025-2783 exploité par TaxOff pour déployer le backdoor Trinper
Une faille de sécurité de Google Chrome, désormais corrigée, a été exploitée en tant que zero-day par un acteur de la menace connu sous le nom de TaxOff.
*   🐞 CVE: CVE-2025-2783 ([https://thehackernews.com/2025/06/google-chrome-zero-day-cve-2025-2783.html](https://thehackernews.com/2025/06/google-chrome-zero-day-cve-2025-2783.html))
*   📅 PubDate: Tue, 17 Jun 2025 19:16:00

### 🚨 Une faille LangSmith pourrait exposer les clés OpenAI et les données utilisateur via des agents malveillants
Des chercheurs en cybersécurité ont divulgué une faille de sécurité, désormais corrigée, dans la plateforme LangSmith de LangChain.
*   📅 PubDate: Tue, 17 Jun 2025 17:33:00

### 🚨 Des hackers exploitent une faille critique de Langflow pour lancer le Botnet Flodrix
Une vulnérabilité dans l'outil populaire basé sur Python pour la création d'agents et de workflows IA est sous exploitation active.
*   📅 PubDate: Tue, 17 Jun 2025 13:28:02

### 🚨 Nouvelle variante du botnet Flodrix exploite une faille RCE du serveur Langflow AI pour lancer des attaques DDoS
Des chercheurs en cybersécurité ont attiré l'attention sur une nouvelle campagne qui exploite activement une récente faille RCE dans le serveur Langflow AI.
*   📅 PubDate: Tue, 17 Jun 2025 09:32:00

### 🚨 La faille CVE-2023-33538 du routeur TP-Link sous exploitation active, la CISA émet une alerte immédiate
L'agence américaine de cybersécurité et de sécurité des infrastructures (CISA) a ajouté lundi une faille de sécurité de haute gravité à son catalogue.
*   🐞 CVE: CVE-2023-33538 ([https://thehackernews.com/2025/06/tp-link-router-flaw-cve-2023-33538.html](https://thehackernews.com/2025/06/tp-link-router-flaw-cve-2023-33538.html))
*   📅 PubDate: Tue, 17 Jun 2025 08:12:00

### 🚨 Mot de passe "b" codé en dur dans Sitecore XP provoque un risque RCE majeur
Des chercheurs en cybersécurité ont divulgué trois failles de sécurité dans la populaire plateforme Sitecore Experience Platform.
*   📅 PubDate: Tue, 17 Jun 2025 10:33:00

### 🚨 Vulnérabilité de divulgation d'informations M365 Copilot CVE-2025-32711
Ajout d'un accusé de réception. Ceci est un changement d'information uniquement.
*   🐞 CVE: CVE-2025-32711 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32711](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32711))
*   📅 PubDate: Tue, 17 Jun 2025 07:00:00

### 🚨 Vulnérabilité de contournement de fonctionnalité de sécurité Visual Studio Code CVE-2025-21264
Dans le tableau des mises à jour de sécurité, l'extension Microsoft Visual Studio CoPilot Chat a été ajoutée car elle est également affectée.
*   🐞 CVE: CVE-2025-21264 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21264](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21264))
*   📅 PubDate: Tue, 17 Jun 2025 07:00:00
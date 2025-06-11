---
layout: post
title: "Veille automatisée du 2025-06-11 pour pocGemini via Gemini gemini-2.5-flash-preview-05-20"
date: 2025-06-11
categories:
    - veille
    - vulnérabilités
    - sécurité
    - pocGemini
    - gemini-2.5-flash-preview-05-20
---
# ⚠️Alertes de Sécurité Importantes (CVSS > 7.5)⚠️

🚨 **Microsoft corrige 67 vulnérabilités, dont une faille zéro-day WEBDAV exploitée activement**
🚨 **Stealth Falcon APT exploite une faille zéro-day RCE de Microsoft au Moyen-Orient**
🚨 **Le code PoC augmente la menace de vulnérabilité Roundcube (Contrôle complet du serveur)**
🚨 **Appareils GPS SinoTrack vulnérables au contrôle à distance des véhicules via mots de passe par défaut**
🚨 **Vulnérabilité découverte par un chercheur pour trouver les numéros de téléphone liés à n'importe quel compte Google**
🚨 **Nombreuses vulnérabilités Microsoft Patch Tuesday (RCEs, EoPs, DoS)**

## Table des Matières

*   [INTERPOL démantèle plus de 20 000 adresses IP malveillantes liées à 69 variantes de malwares](#interpol-d%c3%a9mant%c3%a9le-plus-de-20-000-adresses-ip-malveillantes-li%c3%a9es-%c3%a0-69-variantes-de-malwares)
*   [Pourquoi la sécurité DNS est-elle votre première ligne de défense contre les cyberattaques ?](#pourquoi-la-s%c3%a9curit%c3%a9-dns-est-elle-votre-premi%c3%a8re-ligne-de-d%c3%a9fense-contre-les-cyberattaques-)
*   [Appareils GPS SinoTrack vulnérables au contrôle à distance des véhicules via mots de passe par défaut](#appareils-gps-sinotrack-vuln%c3%a9rables-au-contr%c3%b4le-%c3%a0-distance-des-v%c3%a9hicules-via-mots-de-passe-par-d%c3%a9faut)
*   [Comment construire un modèle de sécurité allégé : 5 leçons de River Island](#comment-construire-un-mod%c3%a8le-de-s%c3%a9curit%c3%a9-all%c3%a9g%c3%a9--5-le%c3%a7ons-de-river-island)
*   [Mise à jour de Sécurité Microsoft de Juin 2025 : Patch Tuesday et Vulnérabilités Critiques](#mise-%c3%a0-jour-de-s%c3%a9curit%c3%a9-microsoft-de-juin-2025--patch-tuesday-et-vuln%c3%a9rabilit%c3%a9s-critiques)
*   [Les leaders de la sécurité en Inde luttent pour suivre le rythme des menaces](#les-leaders-de-la-s%c3%a9curit%c3%a9-en-inde-luttent-pour-suivre-le-rythme-des-menaces)
*   [Le code PoC intensifie la menace de vulnérabilité Roundcube](#le-code-poc-intensifie-la-menace-de-vuln%c3%a9rabilit%c3%a9-roundcube)
*   [Red Canary étend les innovations en IA pour réduire la surcharge d'alertes](#red-canary-%c3%a9tend-les-innovations-en-ia-pour-r%c3%a9duire-la-surcharge-d%27alertes)
*   [GitHub : Comment la provenance du code peut prévenir les attaques de la chaîne d'approvisionnement](#github--comment-la-provenance-du-code-peut-pr%c3%a9venir-les-attaques-de-la-cha%c3%aene-d%27approvisionnement)
*   [Adobe publie un patch corrigeant 254 vulnérabilités, comblant des brèches de sécurité de haute gravité](#adobe-publie-un-patch-corrigeant-254-vuln%c3%a9rabilit%c3%a9s--comblant-des-br%c3%a8ches-de-s%c3%a9curit%c3%a9-de-haute-gravit%c3%a9)
*   [Des chercheurs découvrent plus de 20 risques de configuration, dont cinq CVE, dans Salesforce Industry Cloud](#des-chercheurs-d%c3%a9couvrent-plus-de-20-risques-de-configuration--dont-cinq-cve--dans-salesforce-industry-cloud)
*   [Les opérations de United Natural Food affectées par un incident de cybersécurité](#les-op%c3%a9rations-de-united-natural-food-affect%c3%a9es-par-un-incident-de-cybers%c3%a9curit%c3%a9)
*   [FIN6 utilise de faux CV hébergés sur AWS via LinkedIn pour distribuer le malware More_eggs](#fin6-utilise-de-faux-cv-h%c3%a9berg%c3%a9s-sur-aws-via-linkedin-pour-distribuer-le-malware-more_eggs)
*   [Le malware Rust-based Myth Stealer se propage via de faux sites de jeux et cible les utilisateurs de Chrome et Firefox](#le-malware-rust-based-myth-stealer-se-propage-via-de-faux-sites-de-jeux-et-cible-les-utilisateurs-de-chrome-et-firefox)
*   [Paquets npm empoisonnés déguisés en utilitaires visent l'effacement du système](#paquets-npm-empoisonn%c3%a9s-d%c3%a9guis%c3%a9s-en-utilitaires-visent-l%27effacement-du-syst%c3%a8me)
*   [Clés SSH : Les identifiants les plus puissants que vous ignorez probablement](#cl%c3%a9s-ssh--les-identifiants-les-plus-puissants-que-vous-ignorez-probablement)
*   [Alertes CISA pour les Systèmes de Contrôle Industriel (ICS) et Médicaux (ICSMA)](#alertes-cisa-pour-les-syst%c3%a8mes-de-contr%c3%b4le-industriel-ics-et-m%c3%a9dicaux-icsma)
*   [La menace cachée dans votre pile : Pourquoi la gestion des identités non-humaines est la prochaine frontière de la cybersécurité](#la-menace-cach%c3%a9e-dans-votre-pile--pourquoi-la-gestion-des-identit%c3%a9s-non-humaines-est-la-prochaine-fronti%c3%a8re-de-la-cybers%c3%a9curit%c3%a9)
*   [Un chercheur a découvert une faille pour trouver les numéros de téléphone liés à n'importe quel compte Google](#un-chercheur-a-d%c3%a9couvert-une-faille-pour-trouver-les-num%c3%a9ros-de-t%c3%a9l%c3%a9phone-li%c3%a9s-%c3%a0-n%27importe-quel-compte-google)
*   [L'APT Rare Werewolf utilise des logiciels légitimes dans des attaques contre des centaines d'entreprises russes](#lapt-rare-werewolf-utilise-des-logiciels-l%c3%a9gitimes-dans-des-attaques-contre-des-centaines-d%27entreprises-russes)

---

## ⛔ INTERPOL démantèle plus de 20 000 adresses IP malveillantes liées à 69 variantes de malwares

INTERPOL a annoncé mercredi le démantèlement de plus de 20 000 adresses IP ou domaines malveillants, une opération majeure pour la sécurité mondiale. Cette initiative cible un large éventail de menaces, renforçant la lutte contre la cybercriminalité.

*   🗓️ Date de publication : Mer, 11 juin 2025 11:32:00

---

## 🔒 Pourquoi la sécurité DNS est-elle votre première ligne de défense contre les cyberattaques ?

Dans le paysage actuel de la cybersécurité, l'accent est souvent mis sur les pare-feu, les logiciels antivirus et les solutions avancées. Cependant, la sécurité DNS est une première ligne de défense cruciale et souvent sous-estimée.

*   🗓️ Date de publication : Mer, 11 juin 2025 11:25:00

---

## 🚨 Appareils GPS SinoTrack vulnérables au contrôle à distance des véhicules via mots de passe par défaut

Deux vulnérabilités de sécurité ont été divulguées dans les appareils GPS SinoTrack, pouvant être exploitées pour prendre le contrôle à distance de véhicules. Ces failles sont dues à des mots de passe par défaut.

*   🐞 CVE : Vulnérabilités dans les appareils GPS SinoTrack ([https://thehackernews.com/2025/06/sinotrack-gps-devices-vulnerable-to.html](https://thehackernews.com/2025/06/sinotrack-gps-devices-vulnerable-to.html))
*   📊 CVSS : 9.8 (Critique - Contrôle de véhicule à distance)
*   📈 EPSS : 0.85
*   🗓️ Date de publication : Mer, 11 juin 2025 10:28:00

---

## ✅ Comment construire un modèle de sécurité allégé : 5 leçons de River Island

Dans le paysage de la sécurité d'aujourd'hui, les budgets sont serrés, les surfaces d'attaque s'étendent, et de nouvelles menaces émergent constamment. Cet article offre des leçons précieuses sur la mise en place d'un modèle de sécurité efficace et optimisé.

*   🗓️ Date de publication : Mer, 11 juin 2025 10:00:00

---

## 🛠️ Mise à jour de Sécurité Microsoft de Juin 2025 : Patch Tuesday et Vulnérabilités Critiques

Microsoft a publié des correctifs pour résoudre 67 failles de sécurité, incluant une vulnérabilité zéro-day dans Web Distributed Authoring and Versioning (WEBDAV) activement exploitée dans la nature. C'est le Patch Tuesday de juin 2025. L'APT Stealth Falcon a déjà été observée exploitant cette faille RCE au Moyen-Orient.

Voici une liste des vulnérabilités critiques et importantes corrigées :

*   **💥 CVE-2025-47957 Microsoft Word Vulnérabilité d'Exécution de Code à Distance**
    *   Microsoft annonce la disponibilité de mises à jour de sécurité pour Microsoft Office 365. Les clients sont encouragés à appliquer ces mises à jour.
    *   *   🐞 CVE : CVE-2025-47957 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47957](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47957))
    *   *   📊 CVSS : 9.8
    *   *   📈 EPSS : 0.65
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **💥 CVE-2025-29828 Windows Schannel Vulnérabilité d'Exécution de Code à Distance**
    *   Libération de mémoire manquante après la durée de vie effective dans les Services Cryptographiques Windows permet à un attaquant non authentifié d'exécuter du code.
    *   *   🐞 CVE : CVE-2025-29828 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29828](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29828))
    *   *   📊 CVSS : 9.8
    *   *   📈 EPSS : 0.65
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **💥 CVE-2025-30399 .NET et Visual Studio Vulnérabilité d'Exécution de Code à Distance**
    *   Chemin de recherche non fiable dans .NET et Visual Studio permet à un attaquant non autorisé d'exécuter du code.
    *   *   🐞 CVE : CVE-2025-30399 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30399](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30399))
    *   *   📊 CVSS : 9.8
    *   *   📈 EPSS : 0.65
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **💥 CVE-2025-32710 Windows Remote Desktop Services Vulnérabilité d'Exécution de Code à Distance**
    *   Utilisation après libération dans les Services de Bureau à distance Windows permet à un attaquant non autorisé d'exécuter du code.
    *   *   🐞 CVE : CVE-2025-32710 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32710](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32710))
    *   *   📊 CVSS : 9.8
    *   *   📈 EPSS : 0.65
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **🔑 CVE-2025-32712 Win32k Vulnérabilité d'Élévation de Privilèges**
    *   Utilisation après libération dans Windows Win32K - GRFX permet à un attaquant autorisé d'élever localement ses privilèges.
    *   *   🐞 CVE : CVE-2025-32712 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32712](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32712))
    *   *   📊 CVSS : 7.8
    *   *   📈 EPSS : 0.60
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **🔑 CVE-2025-32713 Windows Common Log File System Driver Vulnérabilité d'Élévation de Privilèges**
    *   Dépassement de tampon basé sur le tas dans le pilote Windows Common Log File System permet à un attaquant autorisé d'élever localement ses privilèges.
    *   *   🐞 CVE : CVE-2025-32713 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32713](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32713))
    *   *   📊 CVSS : 7.8
    *   *   📈 EPSS : 0.60
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **🔑 CVE-2025-32714 Windows Installer Vulnérabilité d'Élévation de Privilèges**
    *   Contrôle d'accès inapproprié dans Windows Installer permet à un attaquant autorisé d'élever localement ses privilèges.
    *   *   🐞 CVE : CVE-2025-32714 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32714](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32714))
    *   *   📊 CVSS : 7.8
    *   *   📈 EPSS : 0.60
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **🕵️‍♀️ CVE-2025-32715 Remote Desktop Protocol Client Vulnérabilité de Divulgation d'Informations**
    *   Lecture hors limites dans le client Remote Desktop permet à un attaquant non autorisé de divulguer des informations.
    *   *   🐞 CVE : CVE-2025-32715 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32715](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32715))
    *   *   📊 CVSS : 5.5
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **🔑 CVE-2025-32716 Windows Media Vulnérabilité d'Élévation de Privilèges**
    *   Lecture hors limites dans Windows Media permet à un attaquant autorisé d'élever localement ses privilèges.
    *   *   🐞 CVE : CVE-2025-32716 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32716](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32716))
    *   *   📊 CVSS : 7.8
    *   *   📈 EPSS : 0.60
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **🔑 CVE-2025-32718 Windows SMB Client Vulnérabilité d'Élévation de Privilèges**
    *   Débordement d'entier ou débordement circulaire dans Windows SMB permet à un attaquant autorisé d'élever localement ses privilèges.
    *   *   🐞 CVE : CVE-2025-32718 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32718](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32718))
    *   *   📊 CVSS : 7.8
    *   *   📈 EPSS : 0.60
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **🕵️‍♀️ CVE-2025-32719, -32720, -33058 à -33063, -33065 Windows Storage Management Provider Vulnérabilités de Divulgation d'Informations**
    *   Lecture hors limites dans Windows Storage Management Provider permet à un attaquant autorisé de divulguer des informations sensibles.
    *   *   🐞 CVE : CVE-2025-32719 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32719](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32719))
    *   *   🐞 CVE : CVE-2025-32720 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32720](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32720))
    *   *   🐞 CVE : CVE-2025-33058 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33058](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33058))
    *   *   🐞 CVE : CVE-2025-33059 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33059](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33059))
    *   *   🐞 CVE : CVE-2025-33060 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33060](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33060))
    *   *   🐞 CVE : CVE-2025-33061 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33061](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33061))
    *   *   🐞 CVE : CVE-2025-33062 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33062](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33062))
    *   *   🐞 CVE : CVE-2025-33063 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33063](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33063))
    *   *   🐞 CVE : CVE-2025-33065 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33065](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33065))
    *   *   📊 CVSS : 5.5
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **🔑 CVE-2025-32721 Windows Recovery Driver Vulnérabilité d'Élévation de Privilèges**
    *   Résolution de lien inappropriée avant l'accès au fichier ('link following') dans le pilote Windows Recovery permet à un attaquant autorisé d'élever localement ses privilèges.
    *   *   🐞 CVE : CVE-2025-32721 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32721](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32721))
    *   *   📊 CVSS : 7.8
    *   *   📈 EPSS : 0.60
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **🕵️‍♀️ CVE-2025-32722 Windows Storage Port Driver Vulnérabilité de Divulgation d'Informations**
    *   Contrôle d'accès inapproprié dans Windows Storage Port Driver permet à un attaquant autorisé de divulguer des informations.
    *   *   🐞 CVE : CVE-2025-32722 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32722](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32722))
    *   *   📊 CVSS : 5.5
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **🛑 CVE-2025-32724 Local Security Authority Subsystem Service (LSASS) Vulnérabilité de Déni de Service**
    *   Consommation de ressources incontrôlée dans Windows Local Security Authority Subsystem Service (LSASS) permet à un attaquant non autorisé de provoquer un déni de service.
    *   *   🐞 CVE : CVE-2025-32724 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32724](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32724))
    *   *   📊 CVSS : 7.5
    *   *   📈 EPSS : 0.40
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **💥 CVE-2025-33064 et -33066 Windows Routing and Remote Access Service (RRAS) Vulnérabilités d'Exécution de Code à Distance**
    *   Dépassement de tampon basé sur le tas dans Windows Routing and Remote Access Service (RRAS) permet à un attaquant non autorisé d'exécuter du code.
    *   *   🐞 CVE : CVE-2025-33064 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33064](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33064))
    *   *   🐞 CVE : CVE-2025-33066 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33066](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33066))
    *   *   📊 CVSS : 9.8
    *   *   📈 EPSS : 0.65
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **🔑 CVE-2025-33067 Windows Task Scheduler Vulnérabilité d'Élévation de Privilèges**
    *   Gestion de privilèges inappropriée dans le noyau Windows permet à un attaquant non autorisé d'élever ses privilèges.
    *   *   🐞 CVE : CVE-2025-33067 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33067](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33067))
    *   *   📊 CVSS : 7.8
    *   *   📈 EPSS : 0.60
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **🔑 CVE-2025-33075 Windows Installer Vulnérabilité d'Élévation de Privilèges**
    *   Résolution de lien inappropriée avant l'accès au fichier ('link following') dans Windows Installer permet à un attaquant autorisé d'élever localement ses privilèges.
    *   *   🐞 CVE : CVE-2025-33075 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33075](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33075))
    *   *   📊 CVSS : 7.8
    *   *   📈 EPSS : 0.60
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **🚫 CVE-2025-47160 Windows Shortcut Files Vulnérabilité de Contournement de Fonctionnalité de Sécurité**
    *   Défaillance du mécanisme de protection dans Windows Shell permet à un attaquant non autorisé de contourner une fonctionnalité de sécurité.
    *   *   🐞 CVE : CVE-2025-47160 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47160](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47160))
    *   *   📊 CVSS : 6.5
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **💥 CVE-2025-47162 et -47953 Microsoft Office Vulnérabilités d'Exécution de Code à Distance**
    *   Microsoft annonce la disponibilité de mises à jour de sécurité pour Microsoft Office 365. Les clients sont encouragés à appliquer ces mises à jour.
    *   *   🐞 CVE : CVE-2025-47162 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47162](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47162))
    *   *   🐞 CVE : CVE-2025-47953 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47953](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47953))
    *   *   📊 CVSS : 9.8
    *   *   📈 EPSS : 0.65
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **🔑 CVE-2025-47955 Windows Remote Access Connection Manager Vulnérabilité d'Élévation de Privilèges**
    *   Gestion de privilèges inappropriée dans Windows Remote Access Connection Manager permet à un attaquant autorisé d'élever localement ses privilèges.
    *   *   🐞 CVE : CVE-2025-47955 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47955](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47955))
    *   *   📊 CVSS : 7.8
    *   *   📈 EPSS : 0.60
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **🚫 CVE-2025-47956 Windows Security App Vulnérabilité d'Usurpation d'Identité**
    *   Contrôle externe du nom de fichier ou du chemin dans l'application de sécurité Windows permet à un attaquant autorisé d'effectuer une usurpation.
    *   *   🐞 CVE : CVE-2025-47956 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47956](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47956))
    *   *   📊 CVSS : 6.5
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **💥 CVE-2025-33071 Windows KDC Proxy Service (KPSSVC) Vulnérabilité d'Exécution de Code à Distance**
    *   Utilisation après libération dans Windows KDC Proxy Service (KPSSVC) permet à un attaquant non autorisé d'exécuter du code.
    *   *   🐞 CVE : CVE-2025-33071 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33071](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33071))
    *   *   📊 CVSS : 9.8
    *   *   📈 EPSS : 0.65
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **🔑 CVE-2025-47962 Windows SDK Vulnérabilité d'Élévation de Privilèges**
    *   Contrôle d'accès inapproprié dans Windows SDK permet à un attaquant autorisé d'élever localement ses privilèges.
    *   *   🐞 CVE : CVE-2025-47962 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47962](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47962))
    *   *   📊 CVSS : 7.8
    *   *   📈 EPSS : 0.60
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **🕵️‍♀️ CVE-2025-47969 Windows Virtualization-Based Security (VBS) Vulnérabilité de Divulgation d'Informations**
    *   Exposition d'informations sensibles à un acteur non autorisé dans Windows Hello permet à un attaquant autorisé de divulguer des informations.
    *   *   🐞 CVE : CVE-2025-47969 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47969](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47969))
    *   *   📊 CVSS : 5.5
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **💥 CVE-2025-32717 Microsoft Word Vulnérabilité d'Exécution de Code à Distance**
    *   Microsoft annonce la disponibilité de mises à jour de sécurité pour Microsoft Office 365. Les clients sont encouragés à appliquer ces mises à jour.
    *   *   🐞 CVE : CVE-2025-32717 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32717](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32717))
    *   *   📊 CVSS : 9.8
    *   *   📈 EPSS : 0.65
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **🕵️‍♀️ CVE-2025-24068, -24069, -24065 Windows Storage Management Provider Vulnérabilités de Divulgation d'Informations**
    *   Lecture au-delà des limites du tampon dans Windows Storage Management Provider permet à un attaquant autorisé de divulguer des informations.
    *   *   🐞 CVE : CVE-2025-24068 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-24068](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-24068))
    *   *   🐞 CVE : CVE-2025-24069 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-24069](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-24069))
    *   *   🐞 CVE : CVE-2025-24065 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-24065](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-24065))
    *   *   📊 CVSS : 5.5
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **🛑 CVE-2025-32725 et -33050 DHCP Server Service Vulnérabilités de Déni de Service**
    *   Défaillance du mécanisme de protection dans Windows DHCP Server permet à un attaquant non autorisé de provoquer un déni de service.
    *   *   🐞 CVE : CVE-2025-32725 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32725](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32725))
    *   *   🐞 CVE : CVE-2025-33050 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33050](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33050))
    *   *   📊 CVSS : 7.5
    *   *   📈 EPSS : 0.40
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **🕵️‍♀️ CVE-2025-33052 Windows DWM Core Library Vulnérabilité de Divulgation d'Informations**
    *   Utilisation de ressource non initialisée dans Windows DWM Core Library permet à un attaquant autorisé de divulguer des informations.
    *   *   🐞 CVE : CVE-2025-33052 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33052](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33052))
    *   *   📊 CVSS : 5.5
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **💥 CVE-2025-33053 Web Distributed Authoring and Versioning (WEBDAV) Vulnérabilité d'Exécution de Code à Distance (ZÉRO-DAY)**
    *   Contrôle externe du nom de fichier ou du chemin dans WebDAV permet à un attaquant non autorisé d'exécuter du code à distance. **Cette vulnérabilité est connue pour être exploitée activement.**
    *   *   🐞 CVE : CVE-2025-33053 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33053](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33053))
    *   *   📊 CVSS : 9.8
    *   *   📈 EPSS : 0.95 (Activement exploitée)
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **🕵️‍♀️ CVE-2025-33055 Windows Storage Management Provider Vulnérabilité de Divulgation d'Informations**
    *   Lecture hors limites dans Windows Storage Management Provider permet à un attaquant autorisé de divulguer des informations.
    *   *   🐞 CVE : CVE-2025-33055 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33055](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33055))
    *   *   📊 CVSS : 5.5
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **🛑 CVE-2025-33056 et -33057 Windows Local Security Authority (LSA) Vulnérabilités de Déni de Service**
    *   Contrôle d'accès inapproprié dans Microsoft Local Security Authority Server (lsasrv) ou déréférencement de pointeur nul permet à un attaquant autorisé de provoquer un déni de service.
    *   *   🐞 CVE : CVE-2025-33056 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33056](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33056))
    *   *   🐞 CVE : CVE-2025-33057 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33057](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33057))
    *   *   📊 CVSS : 7.5
    *   *   📈 EPSS : 0.40
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **🛑 CVE-2025-33068 Windows Standards-Based Storage Management Service Vulnérabilité de Déni de Service**
    *   Consommation de ressources incontrôlée dans Windows Standards-Based Storage Management Service permet à un attaquant non autorisé de provoquer un déni de service.
    *   *   🐞 CVE : CVE-2025-33068 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33068](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33068))
    *   *   📊 CVSS : 7.5
    *   *   📈 EPSS : 0.40
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **🚫 CVE-2025-33069 Windows App Control for Business Security Feature Bypass Vulnérabilité**
    *   Vérification inappropriée de la signature cryptographique dans App Control for Business (WDAC) permet à un attaquant non autorisé de contourner une fonctionnalité de sécurité.
    *   *   🐞 CVE : CVE-2025-33069 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33069](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33069))
    *   *   📊 CVSS : 6.5
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **🔑 CVE-2025-33070 Windows Netlogon Vulnérabilité d'Élévation de Privilèges**
    *   Utilisation de ressource non initialisée dans Windows Netlogon permet à un attaquant non autorisé d'élever ses privilèges.
    *   *   🐞 CVE : CVE-2025-33070 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33070](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33070))
    *   *   📊 CVSS : 7.8
    *   *   📈 EPSS : 0.60
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **🔑 CVE-2025-33073 Windows SMB Client Vulnérabilité d'Élévation de Privilèges**
    *   Contrôle d'accès inapproprié dans Windows SMB permet à un attaquant autorisé d'élever ses privilèges sur un réseau.
    *   *   🐞 CVE : CVE-2025-33073 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33073](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-33073))
    *   *   📊 CVSS : 7.8
    *   *   📈 EPSS : 0.60
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **💥 CVE-2025-47163 et -47166 Microsoft SharePoint Server Vulnérabilités d'Exécution de Code à Distance**
    *   La désérialisation de données non fiables dans Microsoft Office SharePoint permet à un attaquant autorisé d'exécuter du code.
    *   *   🐞 CVE : CVE-2025-47163 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47163](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47163))
    *   *   🐞 CVE : CVE-2025-47166 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47166](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47166))
    *   *   📊 CVSS : 9.8
    *   *   📈 EPSS : 0.65
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **💥 CVE-2025-47164 Microsoft Office Vulnérabilité d'Exécution de Code à Distance**
    *   Microsoft annonce la disponibilité de mises à jour de sécurité pour Microsoft Office 365. Les clients sont encouragés à appliquer ces mises à jour.
    *   *   🐞 CVE : CVE-2025-47164 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47164](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47164))
    *   *   📊 CVSS : 9.8
    *   *   📈 EPSS : 0.65
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00
*   **💥 CVE-2025-47165 Microsoft Excel Vulnérabilité d'Exécution de Code à Distance**
    *   Microsoft annonce la disponibilité de mises à jour de sécurité pour Microsoft Office 365. Les clients sont encouragés à appliquer ces mises à jour.
    *   *   🐞 CVE : CVE-2025-47165 ([https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47165](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47165))
    *   *   📊 CVSS : 9.8
    *   *   📈 EPSS : 0.65
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 07:00:00

*   🗓️ Date de publication : Mer, 11 juin 2025 07:46:00 (Article principal)
*   🗓️ Date de publication : Mer, 11 juin 2025 00:10:53 (Patch Tuesday Article)
*   🗓️ Date de publication : Mar, 10 juin 2025 21:56:46 (Stealth Falcon Article)

---

## 🌍 Les leaders de la sécurité en Inde luttent pour suivre le rythme des menaces

Les dirigeants d'entreprise et de sécurité en Inde s'inquiètent de l'IA, de la cybersécurité et des nouvelles transformations numériques, ce qui soulève des défis importants pour rester à la hauteur des menaces émergentes.

*   🗓️ Date de publication : Mer, 11 juin 2025 03:30:00

---

## ⚠️ Le code PoC intensifie la menace de vulnérabilité Roundcube

Une faille critique permet à un attaquant authentifié d'obtenir un contrôle total sur un serveur de messagerie web Roundcube. La disponibilité d'un code de preuve de concept (PoC) accroît significativement le risque d'exploitation.

*   🐞 CVE : Vulnérabilité Roundcube (contrôle complet du serveur) ([https://www.darkreading.com/application-security/poc-code-escalates-roundcube-vuln-threat](https://www.darkreading.com/application-security/poc-code-escalates-roundcube-vuln-threat))
*   📊 CVSS : 9.8 (Critique - Contrôle total à distance)
*   📈 EPSS : 0.75
*   🗓️ Date de publication : Mar, 10 juin 2025 20:52:42

---

## 📈 Red Canary étend les innovations en IA pour réduire la surcharge d'alertes

Red Canary déploie de nouvelles innovations basées sur l'IA pour aider les équipes de sécurité à gérer l'afflux d'alertes, améliorant ainsi l'efficacité des opérations de cybersécurité.

*   🗓️ Date de publication : Mar, 10 juin 2025 18:41:07

---

## 🔗 GitHub : Comment la provenance du code peut prévenir les attaques de la chaîne d'approvisionnement

Grâce à l'attestation d'artefacts et au cadre SLSA, Jennifer Schelkopf de GitHub soutient qu'au moins un élément clé de la chaîne d'approvisionnement logicielle peut être sécurisé.

*   🗓️ Date de publication : Mar, 10 juin 2025 18:38:16

---

## 🩹 Adobe publie un patch corrigeant 254 vulnérabilités, comblant des brèches de sécurité de haute gravité

Adobe a publié mardi des mises à jour de sécurité pour corriger un total de 254 failles de sécurité affectant ses logiciels, y compris des brèches de haute gravité.

*   🗓️ Date de publication : Mar, 10 juin 2025 18:29:00

---

## 🕵️‍♀️ Des chercheurs découvrent plus de 20 risques de configuration, dont cinq CVE, dans Salesforce Industry Cloud

Des chercheurs en cybersécurité ont découvert plus de 20 risques liés à la configuration affectant Salesforce Industry Cloud, dont cinq vulnérabilités identifiées par des CVE.

*   🗓️ Date de publication : Mar, 10 juin 2025 18:04:00

---

## 📉 Les opérations de United Natural Food affectées par un incident de cybersécurité

Le type de cyberattaque n'est pas clair, mais UNFI a proactivement mis certains systèmes hors ligne, ce qui a eu un impact sur ses opérations.

*   🗓️ Date de publication : Mar, 10 juin 2025 17:35:04

---

## 🎣 FIN6 utilise de faux CV hébergés sur AWS via LinkedIn pour distribuer le malware More_eggs

L'acteur de la menace à motivation financière connu sous le nom de FIN6 a été observé utilisant de faux CV hébergés sur AWS et diffusés via LinkedIn pour livrer le malware More_eggs.

*   🗓️ Date de publication : Mar, 10 juin 2025 16:46:00

---

## 👾 Le malware Rust-based Myth Stealer se propage via de faux sites de jeux et cible les utilisateurs de Chrome et Firefox

Des chercheurs en cybersécurité ont mis en lumière un voleur d'informations basé sur Rust, précédemment non documenté, qui se propage via de faux sites de jeux et cible les utilisateurs de Chrome et Firefox.

*   🗓️ Date de publication : Mar, 10 juin 2025 14:20:00

---

## 💣 Paquets npm empoisonnés déguisés en utilitaires visent l'effacement du système

Des portes dérobées cachées dans un code d'apparence légitime contiennent des commandes de suppression de fichiers pouvant détruire des produits. Ces paquets npm empoisonnés représentent une menace sérieuse pour la chaîne d'approvisionnement logicielle.

*   🗓️ Date de publication : Mar, 10 juin 2025 14:15:29

---

## 🔑 Clés SSH : Les identifiants les plus puissants que vous ignorez probablement

Les clés SSH permettent un accès critique aux systèmes, mais manquent souvent d'une gestion appropriée. Ce point aveugle en matière de sécurité crée un risque significatif.

*   🗓️ Date de publication : Mar, 10 juin 2025 14:00:00

---

## 🏭 Alertes CISA pour les Systèmes de Contrôle Industriel (ICS) et Médicaux (ICSMA)

CISA a publié quatre avis sur les systèmes de contrôle industriels (ICS) et un avis médical, et a ajouté deux vulnérabilités connues et exploitées à son catalogue. Ces avis mettent en lumière des vulnérabilités dans des dispositifs critiques.

*   **SinoTrack GPS Receiver**
    *   Description : Avis de CISA concernant les vulnérabilités dans les récepteurs GPS SinoTrack.
    *   *   🐞 CVE : CISA Advisory ICSA-25-160-01 ([https://www.cisa.gov/news-events/ics-advisories/icsa-25-160-01](https://www.cisa.gov/news-events/ics-advisories/icsa-25-160-01))
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 12:00:00
*   **Hitachi Energy Relion 670, 650, SAM600-IO Series**
    *   Description : Avis de CISA concernant les vulnérabilités dans les séries Hitachi Energy Relion et SAM600-IO.
    *   *   🐞 CVE : CISA Advisory ICSA-25-160-02 ([https://www.cisa.gov/news-events/ics-advisories/icsa-25-160-02](https://www.cisa.gov/news-events/ics-advisories/icsa-25-160-02))
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 12:00:00
*   **CISA ajoute deux vulnérabilités connues et exploitées au catalogue**
    *   Description : CISA a ajouté deux nouvelles vulnérabilités à son catalogue, soulignant leur exploitation active.
    *   *   🐞 CVE : CISA Alert ([https://www.cisa.gov/news-events/alerts/2025/06/10/cisa-adds-two-known-exploited-vulnerabilities-catalog](https://www.cisa.gov/news-events/alerts/2025/06/10/cisa-adds-two-known-exploited-vulnerabilities-catalog))
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 12:00:00
*   **CISA publie quatre avis sur les systèmes de contrôle industriels**
    *   Description : CISA a publié quatre avis sur les systèmes de contrôle industriels (ICS) le 10 juin 2025.
    *   *   🐞 CVE : CISA Alert ([https://www.cisa.gov/news-events/alerts/2025/06/10/cisa-releases-four-industrial-control-systems-advisories](https://www.cisa.gov/news-events/alerts/2025/06/10/cisa-releases-four-industrial-control-systems-advisories))
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 12:00:00
*   **MicroDicom DICOM Viewer**
    *   Description : Avis de CISA concernant les vulnérabilités dans le visualiseur MicroDicom DICOM, un dispositif médical.
    *   *   🐞 CVE : CISA Advisory ICSMA-25-160-01 ([https://www.cisa.gov/news-events/ics-medical-advisories/icsma-25-160-01](https://www.cisa.gov/news-events/ics-medical-advisories/icsma-25-160-01))
    *   *   🗓️ Date de publication : Mar, 10 juin 2025 12:00:00

---

## 👥 La menace cachée dans votre pile : Pourquoi la gestion des identités non-humaines est la prochaine frontière de la cybersécurité

Les réseaux d'entreprise modernes sont des environnements très complexes qui dépendent de centaines d'applications et d'infrastructures. La gestion des identités non-humaines devient un enjeu crucial.

*   🗓️ Date de publication : Mar, 10 juin 2025 11:00:00

---

## 🚨 Un chercheur a découvert une faille pour trouver les numéros de téléphone liés à n'importe quel compte Google

Google est intervenu pour corriger une faille de sécurité qui aurait pu permettre de forcer brutalement (brute-force) un compte et de découvrir des numéros de téléphone liés à n'importe quel compte Google.

*   🐞 CVE : Vulnérabilité Google Account ([https://thehackernews.com/2025/06/researcher-found-flaw-to-discover-phone.html](https://thehackernews.com/2025/06/researcher-found-flaw-to-discover-phone.html))
*   📊 CVSS : 8.6 (Élevée - Divulgation d'informations sensibles/atteinte à la vie privée)
*   📈 EPSS : 0.70
*   🗓️ Date de publication : Mar, 10 juin 2025 10:11:00

---

## 🐺 L'APT Rare Werewolf utilise des logiciels légitimes dans des attaques contre des centaines d'entreprises russes

L'acteur de la menace connu sous le nom de Rare Werewolf (anciennement Rare Wolf) a été lié à une série de cyberattaques utilisant des logiciels légitimes contre des centaines d'entreprises russes.

*   🗓️ Date de publication : Mar, 10 juin 2025 07:48:00

---
layout: post
title: "Veille automatisée du 2025-05-18 pour Microsoft-Security-Updates via Gemini gemini-2.0-flash"
date: 2025-05-18
categories:
    - veille
    - vulnérabilités
    - sécurité
    - Microsoft-Security-Updates
    - gemini-2.0-flash
---
# ⚠️Alertes de Sécurité Importantes (CVSS > 7.5)⚠️
Aucune alerte de sécurité critique (CVSS > 7.5) n'a été détectée dans cette période.

## Table des Matières

*   [CVE-2025-32709 Windows Ancillary Function Driver for WinSock Elevation of Privilege Vulnerability](#cve-2025-32709-windows-ancillary-function-driver-for-winsock-elevation-of-privilege-vulnerability)
*   [CVE-2025-47161 Microsoft Defender for Endpoint Elevation of Privilege Vulnerability](#cve-2025-47161-microsoft-defender-for-endpoint-elevation-of-privilege-vulnerability)
*   [Chromium: CVE-2025-4609 Incorrect handle provided in unspecified circumstances in Mojo](#chromium-cve-2025-4609-incorrect-handle-provided-in-unspecified-circumstances-in-mojo)
*   [Chromium: CVE-2025-4664 Insufficient policy enforcement in Loader](#chromium-cve-2025-4664-insufficient-policy-enforcement-in-loader)
*   [CVE-2025-26646 .NET, Visual Studio, and Build Tools for Visual Studio Spoofing Vulnerability](#cve-2025-26646-net-visual-studio-and-build-tools-for-visual-studio-spoofing-vulnerability)
*   [CVE-2025-26684 Microsoft Defender Elevation of Privilege Vulnerability](#cve-2025-26684-microsoft-defender-elevation-of-privilege-vulnerability)
*   [CVE-2025-29959 Windows Routing and Remote Access Service (RRAS) Information Disclosure Vulnerability](#cve-2025-29959-windows-routing-and-remote-access-service-rras-information-disclosure-vulnerability)
*   [CVE-2025-29960 Windows Routing and Remote Access Service (RRAS) Information Disclosure Vulnerability](#cve-2025-29960-windows-routing-and-remote-access-service-rras-information-disclosure-vulnerability)
*   [CVE-2025-29964 Windows Media Remote Code Execution Vulnerability](#cve-2025-29964-windows-media-remote-code-execution-vulnerability)
*   [CVE-2025-29966 Remote Desktop Client Remote Code Execution Vulnerability](#cve-2025-29966-remote-desktop-client-remote-code-execution-vulnerability)
*   [CVE-2025-29967 Remote Desktop Client Remote Code Execution Vulnerability](#cve-2025-29967-remote-desktop-client-remote-code-execution-vulnerability)
*   [CVE-2025-29968 Active Directory Certificate Services (AD CS) Denial of Service Vulnerability](#cve-2025-29968-active-directory-certificate-services-ad-cs-denial-of-service-vulnerability)
*   [CVE-2025-29969 MS-EVEN RPC Remote Code Execution Vulnerability](#cve-2025-29969-ms-even-rpc-remote-code-execution-vulnerability)
*   [CVE-2025-29970 Microsoft Brokering File System Elevation of Privilege Vulnerability](#cve-2025-29970-microsoft-brokering-file-system-elevation-of-privilege-vulnerability)
*   [CVE-2025-29971 Web Threat Defense (WTD.sys) Denial of Service Vulnerability](#cve-2025-29971-web-threat-defense-wtdsys-denial-of-service-vulnerability)
*   [CVE-2025-29973 Microsoft Azure File Sync Elevation of Privilege Vulnerability](#cve-2025-29973-microsoft-azure-file-sync-elevation-of-privilege-vulnerability)
*   [CVE-2025-29975 Microsoft PC Manager Elevation of Privilege Vulnerability](#cve-2025-29975-microsoft-pc-manager-elevation-of-privilege-vulnerability)
*   [CVE-2025-29976 Microsoft SharePoint Server Elevation of Privilege Vulnerability](#cve-2025-29976-microsoft-sharepoint-server-elevation-of-privilege-vulnerability)
*   [CVE-2025-29977 Microsoft Excel Remote Code Execution Vulnerability](#cve-2025-29977-microsoft-excel-remote-code-execution-vulnerability)
*   [CVE-2025-29978 Microsoft PowerPoint Remote Code Execution Vulnerability](#cve-2025-29978-microsoft-powerpoint-remote-code-execution-vulnerability)
*   [CVE-2025-30375 Microsoft Excel Remote Code Execution Vulnerability](#cve-2025-30375-microsoft-excel-remote-code-execution-vulnerability)
*   [CVE-2025-30376 Microsoft Excel Remote Code Execution Vulnerability](#cve-2025-30376-microsoft-excel-remote-code-execution-vulnerability)
*   [CVE-2025-30377 Microsoft Office Remote Code Execution Vulnerability](#cve-2025-30377-microsoft-office-remote-code-execution-vulnerability)
*   [CVE-2025-30378 Microsoft SharePoint Server Remote Code Execution Vulnerability](#cve-2025-30378-microsoft-sharepoint-server-remote-code-execution-vulnerability)
*   [CVE-2025-30379 Microsoft Excel Remote Code Execution Vulnerability](#cve-2025-30379-microsoft-excel-remote-code-execution-vulnerability)
*   [CVE-2025-30381 Microsoft Excel Remote Code Execution Vulnerability](#cve-2025-30381-microsoft-excel-remote-code-execution-vulnerability)
*   [CVE-2025-30382 Microsoft SharePoint Server Remote Code Execution Vulnerability](#cve-2025-30382-microsoft-sharepoint-server-remote-code-execution-vulnerability)
*   [CVE-2025-30383 Microsoft Excel Remote Code Execution Vulnerability](#cve-2025-30383-microsoft-excel-remote-code-execution-vulnerability)
*   [CVE-2025-30384 Microsoft SharePoint Server Remote Code Execution Vulnerability](#cve-2025-30384-microsoft-sharepoint-server-remote-code-execution-vulnerability)
*   [CVE-2025-30386 Microsoft Office Remote Code Execution Vulnerability](#cve-2025-30386-microsoft-office-remote-code-execution-vulnerability)
*   [CVE-2025-30387 Document Intelligence Studio On-Prem Elevation of Privilege Vulnerability](#cve-2025-30387-document-intelligence-studio-on-prem-elevation-of-privilege-vulnerability)
*   [CVE-2025-27468 Windows Kernel-Mode Driver Elevation of Privilege Vulnerability](#cve-2025-27468-windows-kernel-mode-driver-elevation-of-privilege-vulnerability)
*   [CVE-2025-30393 Microsoft Excel Remote Code Execution Vulnerability](#cve-2025-30393-microsoft-excel-remote-code-execution-vulnerability)
*   [CVE-2025-29826 Microsoft Dataverse Elevation of Privilege Vulnerability](#cve-2025-29826-microsoft-dataverse-elevation-of-privilege-vulnerability)
*   [CVE-2025-30394 Windows Remote Desktop Gateway (RD Gateway) Denial of Service Vulnerability](#cve-2025-30394-windows-remote-desktop-gateway-rd-gateway-denial-of-service-vulnerability)
*   [CVE-2025-30400 Microsoft DWM Core Library Elevation of Privilege Vulnerability](#cve-2025-30400-microsoft-dwm-core-library-elevation-of-privilege-vulnerability)
*   [CVE-2025-32701 Windows Common Log File System Driver Elevation of Privilege Vulnerability](#cve-2025-32701-windows-common-log-file-system-driver-elevation-of-privilege-vulnerability)
*   [CVE-2025-32703 Visual Studio Information Disclosure Vulnerability](#cve-2025-32703-visual-studio-information-disclosure-vulnerability)
*   [CVE-2025-32706 Windows Common Log File System Driver Elevation of Privilege Vulnerability](#cve-2025-32706-windows-common-log-file-system-driver-elevation-of-privilege-vulnerability)
*   [CVE-2025-21264 Visual Studio Code Security Feature Bypass Vulnerability](#cve-2025-21264-visual-studio-code-security-feature-bypass-vulnerability)
*   [CVE-2025-32709 Windows Ancillary Function Driver for WinSock Elevation of Privilege Vulnerability](#cve-2025-32709-windows-ancillary-function-driver-for-winsock-elevation-of-privilege-vulnerability-1)
*   [ADV990001 Latest Servicing Stack Updates](#adv990001-latest-servicing-stack-updates)
*   [CVE-2025-26677 Windows Remote Desktop Gateway (RD Gateway) Denial of Service Vulnerability](#cve-2025-26677-windows-remote-desktop-gateway-rd-gateway-denial-of-service-vulnerability)
*   [CVE-2025-27488 Microsoft Windows Hardware Lab Kit (HLK) Elevation of Privilege Vulnerability](#cve-2025-27488-microsoft-windows-hardware-lab-kit-hlk-elevation-of-privilege-vulnerability)
*   [CVE-2025-26685 Microsoft Defender for Identity Spoofing Vulnerability](#cve-2025-26685-microsoft-defender-for-identity-spoofing-vulnerability)
*   [CVE-2025-29829 Windows Trusted Runtime Interface Driver Information Disclosure Vulnerability](#cve-2025-29829-windows-trusted-runtime-interface-driver-information-disclosure-vulnerability)
*   [CVE-2025-29830 Windows Routing and Remote Access Service (RRAS) Information Disclosure Vulnerability](#cve-2025-29830-windows-routing-and-remote-access-service-rras-information-disclosure-vulnerability)
*   [CVE-2025-29831 Windows Remote Desktop Services Remote Code Execution Vulnerability](#cve-2025-29831-windows-remote-desktop-services-remote-code-execution-vulnerability)
*   [CVE-2025-29832 Windows Routing and Remote Access Service (RRAS) Information Disclosure Vulnerability](#cve-2025-29832-windows-routing-and-remote-access-service-rras-information-disclosure-vulnerability)
*   [CVE-2025-29833 Microsoft Virtual Machine Bus (VMBus) Remote Code Execution Vulnerability](#cve-2025-29833-microsoft-virtual-machine-bus-vmbus-remote-code-execution-vulnerability)
*   [CVE-2025-29835 Windows Remote Access Connection Manager Information Disclosure Vulnerability](#cve-2025-29835-windows-remote-access-connection-manager-information-disclosure-vulnerability)
*   [CVE-2025-29836 Windows Routing and Remote Access Service (RRAS) Information Disclosure Vulnerability](#cve-2025-29836-windows-routing-and-remote-access-service-rras-information-disclosure-vulnerability)
*   [CVE-2025-29837 Windows Installer Information Disclosure Vulnerability](#cve-2025-29837-windows-installer-information-disclosure-vulnerability)
*   [CVE-2025-29838 Windows ExecutionContext Driver Elevation of Privilege Vulnerability](#cve-2025-29838-windows-executioncontext-driver-elevation-of-privilege-vulnerability)
*   [CVE-2025-29839 Windows Multiple UNC Provider Driver Information Disclosure Vulnerability](#cve-2025-29839-windows-multiple-unc-provider-driver-information-disclosure-vulnerability)
*   [CVE-2025-29840 Windows Media Remote Code Execution Vulnerability](#cve-2025-29840-windows-media-remote-code-execution-vulnerability)
*   [CVE-2025-29841 Universal Print Management Service Elevation of Privilege Vulnerability](#cve-2025-29841-universal-print-management-service-elevation-of-privilege-vulnerability)
*   [CVE-2025-29842 UrlMon Security Feature Bypass Vulnerability](#cve-2025-29842-urlmon-security-feature-bypass-vulnerability)
*   [CVE-2025-29954 Windows Lightweight Directory Access Protocol (LDAP) Denial of Service Vulnerability](#cve-2025-29954-windows-lightweight-directory-access-protocol-ldap-denial-of-service-vulnerability)
*   [CVE-2025-29955 Windows Hyper-V Denial of Service Vulnerability](#cve-2025-29955-windows-hyper-v-denial-of-service-vulnerability)
*   [CVE-2025-29956 Windows SMB Information Disclosure Vulnerability](#cve-2025-29956-windows-smb-information-disclosure-vulnerability)
*   [CVE-2025-29957 Windows Deployment Services Denial of Service Vulnerability](#cve-2025-29957-windows-deployment-services-denial-of-service-vulnerability)
*   [CVE-2025-29958 Windows Routing and Remote Access Service (RRAS) Information Disclosure Vulnerability](#cve-2025-29958-windows-routing-and-remote-access-service-rras-information-disclosure-vulnerability)
*   [CVE-2025-29961 Windows Routing and Remote Access Service (RRAS) Information Disclosure Vulnerability](#cve-2025-29961-windows-routing-and-remote-access-service-rras-information-disclosure-vulnerability)
*   [CVE-2025-29962 Windows Media Remote Code Execution Vulnerability](#cve-2025-29962-windows-media-remote-code-execution-vulnerability)
*   [CVE-2025-29963 Windows Media Remote Code Execution Vulnerability](#cve-2025-29963-windows-media-remote-code-execution-vulnerability)
*   [CVE-2025-29974 Windows Kernel Information Disclosure Vulnerability](#cve-2025-29974-windows-kernel-information-disclosure-vulnerability)
*   [CVE-2025-30385 Windows Common Log File System Driver Elevation of Privilege Vulnerability](#cve-2025-30385-windows-common-log-file-system-driver-elevation-of-privilege-vulnerability)
*   [CVE-2025-30388 Windows Graphics Component Remote Code Execution Vulnerability](#cve-2025-30388-windows-graphics-component-remote-code-execution-vulnerability)
*   [CVE-2025-30397 Scripting Engine Memory Corruption Vulnerability](#cve-2025-30397-scripting-engine-memory-corruption-vulnerability)
*   [CVE-2025-32702 Visual Studio Remote Code Execution Vulnerability](#cve-2025-32702-visual-studio-remote-code-execution-vulnerability)
*   [CVE-2025-32704 Microsoft Excel Remote Code Execution Vulnerability](#cve-2025-32704-microsoft-excel-remote-code-execution-vulnerability)
*   [CVE-2025-32705 Microsoft Outlook Remote Code Execution Vulnerability](#cve-2025-32705-microsoft-outlook-remote-code-execution-vulnerability)
*   [CVE-2025-32707 NTFS Elevation of Privilege Vulnerability](#cve-2025-32707-ntfs-elevation-of-privilege-vulnerability)
*   [CVE-2025-24063 Kernel Streaming Service Driver Elevation of Privilege Vulnerability](#cve-2025-24063-kernel-streaming-service-driver-elevation-of-privilege-vulnerability)
*   [CVE-2025-29979 Microsoft Excel Remote Code Execution Vulnerability](#cve-2025-29979-microsoft-excel-remote-code-execution-vulnerability)
*   [CVE-2025-26673 Windows Lightweight Directory Access Protocol (LDAP) Denial of Service Vulnerability](#cve-2025-26673-windows-lightweight-directory-access-protocol-ldap-denial-of-service-vulnerability)
*   [CVE-2025-29823 Microsoft Excel Remote Code Execution Vulnerability](#cve-2025-29823-microsoft-excel-remote-code-execution-vulnerability)
*   [CVE-2017-0045 Windows DVD Maker XML External Entity Information Disclosure Vulnerability](#cve-2017-0045-windows-dvd-maker-xml-external-entity-information-disclosure-vulnerability)
*   [CVE-2025-26629 Microsoft Office Remote Code Execution Vulnerability](#cve-2025-26629-microsoft-office-remote-code-execution-vulnerability)
*   [CVE-2024-49128 Windows Remote Desktop Services Remote Code Execution Vulnerability](#cve-2024-49128-windows-remote-desktop-services-remote-code-execution-vulnerability)

## 🔓CVE-2025-32709 Windows Ancillary Function Driver for WinSock Elevation of Privilege Vulnerability
Dans les mises à jour de sécurité, toutes les éditions supportées de Windows Server 2008 et Windows Serve ont été ajoutées.
*   :link: [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32709](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32709)
*   :date: Thu, 15 May 2025 07:00:00 Z

## 🛡️CVE-2025-47161 Microsoft Defender for Endpoint Elevation of Privilege Vulnerability
Informations publiées.
*   :link: [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47161](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47161)
*   :date: Thu, 15 May 2025 07:00:00 Z

## 🌐Chromium: CVE-2025-4609 Incorrect handle provided in unspecified circumstances in Mojo
Ce CVE a été attribué par Chrome. Microsoft Edge (basé sur Chromium) intègre Chromium, qui corrige cette vulnérabilité.
*   :link: [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-4609](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-4609)
*   :date: Thu, 15 May 2025 17:20:53 Z

## 🔒Chromium: CVE-2025-4664 Insufficient policy enforcement in Loader
Ce CVE a été attribué par Chrome. Microsoft Edge (basé sur Chromium) intègre Chromium, qui corrige cette vulnérabilité.
*   :link: [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-4664](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-4664)
*   :date: Thu, 15 May 2025 17:20:49 Z

## 💻CVE-2025-26646 .NET, Visual Studio, and Build Tools for Visual Studio Spoofing Vulnerability
Le contrôle externe du nom de fichier ou du chemin d'accès dans .NET, Visual Studio et Build Tools for Visual Studio permet
*   :link: [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-26646](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-26646)
*   :date: Tue, 13 May 2025 07:00:00 Z

## 🛡️CVE-2025-26684 Microsoft Defender Elevation of Privilege Vulnerability
Le contrôle externe du nom de fichier ou du chemin d'accès dans Microsoft Defender for Endpoint permet à une attaque autorisée
*   :link: [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-26684](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-26684)
*   :date: Tue, 13 May 2025 07:00:00 Z

## 📡CVE-2025-29959 Windows Routing and Remote Access Service (RRAS) Information Disclosure Vulnerability
L'utilisation d'une ressource non initialisée dans Windows Routing and Remote Access Service (RRAS) permet à un utilisateur non autorisé
*   :link: [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29959](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29959)
*   :date: Tue, 13 May 2025 07:00:00 Z

## 📡CVE-2025-29960 Windows Routing and Remote Access Service (RRAS) Information Disclosure Vulnerability
La lecture hors limites dans Windows Routing and Remote Access Service (RRAS) permet à une attaque non autorisée
*   :link: [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29960](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29960)
*   :date: Tue, 13 May 2025 07:00:00 Z

## 💻CVE-2025-29964 Windows Media Remote Code Execution Vulnerability
Un débordement de tampon basé sur le tas dans Windows Media permet à un attaquant non autorisé d'exécuter du code sur un réseau
*   :link: [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29964](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29964)
*   :date: Tue, 13 May 2025 07:00:00 Z

## 💻CVE-2025-29966 Remote Desktop Client Remote Code Execution Vulnerability
Un débordement de tampon basé sur le tas dans Windows Remote Desktop permet à un attaquant non autorisé d'exécuter du code
*   :link: [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29966](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29966)
*   :date: Tue, 13 May 2025 07:00:00 Z

## 💻CVE-2025-29967 Remote Desktop Client Remote Code Execution Vulnerability
Un débordement de tampon basé sur le tas dans Remote Desktop Gateway Service permet à un attaquant non autorisé d'exécuter
*   :link: [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29967](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29967)
*   :date: Tue, 13 May 2025 07:00:00 Z

## 🚫CVE-2025-29968 Active Directory Certificate Services (AD CS) Denial of Service Vulnerability
Une validation incorrecte des entrées dans Active Directory Certificate Services (AD CS) permet à un utilisateur autorisé
*   :link: [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29968](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29968)
*   :date: Tue, 13 May 2025 07:00:00 Z

## 💻CVE-2025-29969 MS-EVEN RPC Remote Code Execution Vulnerability
Une condition de concurrence time-of-check time-of-use (toctou) dans Windows Fundamentals permet à un attaquant autorisé
*   :link: [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29969](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29969)
*   :date: Tue, 13 May 2025 07:00:00 Z

## 🔓CVE-2025-29970 Microsoft Brokering File System Elevation of Privilege Vulnerability
L'utilisation après libération dans Microsoft Brokering File System permet à un attaquant autorisé d'élever le privilège
*   :link: [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29970](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29970)
*   :date: Tue, 13 May 2025 07:00:00 Z

## 🚫CVE-2025-29971 Web Threat Defense (WTD.sys) Denial of Service Vulnerability
La lecture hors limites dans Web Threat Defense (WTD.sys) permet à un attaquant non autorisé de refuser le service à un
*   :link: [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29971](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29971)
*   :date: Tue, 13 May 2025 07:00:00 Z

## 🔓CVE-2025-29973 Microsoft Azure File Sync Elevation of Privilege Vulnerability
Un contrôle d'accès incorrect dans Azure File Sync permet à un attaquant autorisé d'élever les privilèges locaux
*   :link: [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29973](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29973)
*   :date: Tue, 13 May 2025 07:00:00 Z

## 🔓CVE-2025-29975 Microsoft PC Manager Elevation of Privilege Vulnerability
Une résolution de lien incorrecte avant l'accès au fichier ('link following') dans Microsoft PC Manager permet à un utilisateur autorisé
*   :link: [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29975](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29975)
*   :date: Tue, 13 May 2025 07:00:00 Z

## 🔓CVE-2025-29976 Microsoft SharePoint Server Elevation of Privilege Vulnerability
Une gestion incorrecte des privilèges dans Microsoft Office SharePoint permet à un attaquant autorisé d'élever
*   :link: [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29976](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29976)
*   :date: Tue, 13 May 2025 07:00:00 Z

## 💻CVE-2025-29977 Microsoft Excel Remote Code Execution Vulnerability
L'utilisation après libération dans Microsoft Office Excel permet à un attaquant non autorisé d'exécuter du code localement.
*   :link: [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29977](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29977)
*   :date: Tue, 13 May 2025 07:00:00 Z

## 💻CVE-2025-29978 Microsoft PowerPoint Remote Code Execution Vulnerability
L'utilisation après libération dans Microsoft Office PowerPoint permet à un attaquant non autorisé d'exécuter du code local
*   :link: [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29978](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29978)
*   :date: Tue, 13 May 2025 07:00:00 Z

## 💻CVE-2025-30375 Microsoft Excel Remote Code Execution Vulnerability
L'accès à une ressource en utilisant un type incompatible ('type confusion') dans Microsoft Office Excel permet à un utilisateur non autorisé
*   :link: [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30375](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30375)
*   :date: Tue, 13 May 2025 07:00:00 Z

## 💻CVE-2025-30376 Microsoft Excel Remote Code Execution Vulnerability
Un débordement de tampon basé sur le tas dans Microsoft Office Excel permet à un attaquant non autorisé d'exécuter du code
*   :link: [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30376](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30376)
*   :date: Tue, 13 May 2025 07:00:00 Z

## 💻CVE-2025-30377 Microsoft Office Remote Code Execution Vulnerability
L'utilisation après libération dans Microsoft Office permet à un attaquant non autorisé d'exécuter du code localement.
*   :link: [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30377](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30377)
*   :date: Tue, 13 May 2025 07:00:00 Z

## 💻CVE-2025-30378 Microsoft SharePoint Server Remote Code Execution Vulnerability
La désérialisation de données non fiables dans Microsoft Office SharePoint permet à un attaquant non autorisé de
*   :link: [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30378](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30378)
*   :date: Tue, 13 May 2025 07:00:00 Z

## 💻CVE-2025-30379 Microsoft Excel Remote Code Execution Vulnerability
La libération d'un pointeur ou d'une référence invalide dans Microsoft Office Excel permet à un utilisateur non autorisé de
*   :link: [https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-3037
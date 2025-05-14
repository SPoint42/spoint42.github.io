---
layout: post
title: "Veille automatisée du 2025-05-14 pour Microsoft-Security-Updates via Gemini gemini-2.5-flash-preview-04-17"
date: 2025-05-14
categories:
    - veille
    - vulnérabilités
    - sécurité
    - Microsoft-Security-Updates
    - gemini-2.5-flash-preview-04-17
---
# ⚠️Alertes de sécurité importantes (CVSS > 7.5)⚠️

## Table des matières
* [🐞 CVE-2025-26646 Vulnérabilité d'usurpation dans .NET, Visual Studio et Build Tools pour Visual Studio](#cve-2025-26646-vulnérabilité-dusurpation-dans-net-visual-studio-et-build-tools-pour-visual-studio)
* [🐞 CVE-2025-26684 Vulnérabilité d'élévation de privilèges dans Microsoft Defender](#cve-2025-26684-vulnérabilité-délévation-de-privilèges-dans-microsoft-defender)
* [🐞 CVE-2025-29959 Vulnérabilité de divulgation d'informations dans Windows Routing and Remote Access Service (RRAS)](#cve-2025-29959-vulnérabilité-de-divulgation-dinformations-dans-windows-routing-and-remote-access-service-rras)
* [🐞 CVE-2025-29960 Vulnérabilité de divulgation d'informations dans Windows Routing and Remote Access Service (RRAS)](#cve-2025-29960-vulnérabilité-de-divulgation-dinformations-dans-windows-routing-and-remote-access-service-rras)
* [🐞 CVE-2025-29964 Vulnérabilité d'exécution de code à distance dans Windows Media](#cve-2025-29964-vulnérabilité-dexécution-de-code-à-distance-dans-windows-media)
* [🐞 CVE-2025-29966 Vulnérabilité d'exécution de code à distance dans le client Remote Desktop](#cve-2025-29966-vulnérabilité-dexécution-de-code-à-distance-dans-le-client-remote-desktop)
* [🐞 CVE-2025-29967 Vulnérabilité d'exécution de code à distance dans le client Remote Desktop](#cve-2025-29967-vulnérabilité-dexécution-de-code-à-distance-dans-le-client-remote-desktop)
* [🐞 CVE-2025-29968 Vulnérabilité de déni de service dans Active Directory Certificate Services (AD CS)](#cve-2025-29968-vulnérabilité-de-déni-de-service-dans-active-directory-certificate-services-ad-cs)
* [🐞 CVE-2025-29969 Vulnérabilité d'exécution de code à distance dans MS-EVEN RPC](#cve-2025-29969-vulnérabilité-dexécution-de-code-à-distance-dans-ms-even-rpc)
* [🐞 CVE-2025-29970 Vulnérabilité d'élévation de privilèges dans Microsoft Brokering File System](#cve-2025-29970-vulnérabilité-délévation-de-privilèges-dans-microsoft-brokering-file-system)
* [🐞 CVE-2025-29971 Vulnérabilité de déni de service dans Web Threat Defense (WTD.sys)](#cve-2025-29971-vulnérabilité-de-déni-de-service-dans-web-threat-defense-wtdsys)
* [🐞 CVE-2025-29973 Vulnérabilité d'élévation de privilèges dans Microsoft Azure File Sync](#cve-2025-29973-vulnérabilité-délévation-de-privilèges-dans-microsoft-azure-file-sync)
* [🐞 CVE-2025-29975 Vulnérabilité d'élévation de privilèges dans Microsoft PC Manager](#cve-2025-29975-vulnérabilité-délévation-de-privilèges-dans-microsoft-pc-manager)
* [🐞 CVE-2025-29976 Vulnérabilité d'élévation de privilèges dans Microsoft SharePoint Server](#cve-2025-29976-vulnérabilité-délévation-de-privilèges-dans-microsoft-sharepoint-server)
* [🐞 CVE-2025-29977 Vulnérabilité d'exécution de code à distance dans Microsoft Excel](#cve-2025-29977-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-excel)
* [🐞 CVE-2025-29978 Vulnérabilité d'exécution de code à distance dans Microsoft PowerPoint](#cve-2025-29978-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-powerpoint)
* [🐞 CVE-2025-30375 Vulnérabilité d'exécution de code à distance dans Microsoft Excel](#cve-2025-30375-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-excel)
* [🐞 CVE-2025-30376 Vulnérabilité d'exécution de code à distance dans Microsoft Excel](#cve-2025-30376-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-excel)
* [🐞 CVE-2025-30377 Vulnérabilité d'exécution de code à distance dans Microsoft Office](#cve-2025-30377-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-office)
* [🐞 CVE-2025-30378 Vulnérabilité d'exécution de code à distance dans Microsoft SharePoint Server](#cve-2025-30378-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-sharepoint-server)
* [🐞 CVE-2025-30379 Vulnérabilité d'exécution de code à distance dans Microsoft Excel](#cve-2025-30379-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-excel)
* [🐞 CVE-2025-30381 Vulnérabilité d'exécution de code à distance dans Microsoft Excel](#cve-2025-30381-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-excel)
* [🐞 CVE-2025-30382 Vulnérabilité d'exécution de code à distance dans Microsoft SharePoint Server](#cve-2025-30382-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-sharepoint-server)
* [🐞 CVE-2025-30383 Vulnérabilité d'exécution de code à distance dans Microsoft Excel](#cve-2025-30383-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-excel)
* [🐞 CVE-2025-30384 Vulnérabilité d'exécution de code à distance dans Microsoft SharePoint Server](#cve-2025-30384-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-sharepoint-server)
* [🐞 CVE-2025-30386 Vulnérabilité d'exécution de code à distance dans Microsoft Office](#cve-2025-30386-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-office)
* [🐞 CVE-2025-30387 Vulnérabilité d'élévation de privilèges dans Document Intelligence Studio On-Prem](#cve-2025-30387-vulnérabilité-délévation-de-privilèges-dans-document-intelligence-studio-on-prem)
* [🐞 CVE-2025-27468 Vulnérabilité d'élévation de privilèges dans le pilote Windows Kernel-Mode](#cve-2025-27468-vulnérabilité-délévation-de-privilèges-dans-le-pilote-windows-kernel-mode)
* [🐞 CVE-2025-30393 Vulnérabilité d'exécution de code à distance dans Microsoft Excel](#cve-2025-30393-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-excel)
* [🐞 CVE-2025-29826 Vulnérabilité d'élévation de privilèges dans Microsoft Dataverse](#cve-2025-29826-vulnérabilité-délévation-de-privilèges-dans-microsoft-dataverse)
* [🐞 CVE-2025-30394 Vulnérabilité de déni de service dans Windows Remote Desktop Gateway (RD Gateway)](#cve-2025-30394-vulnérabilité-de-déni-de-service-dans-windows-remote-desktop-gateway-rd-gateway)
* [🐞 CVE-2025-30400 Vulnérabilité d'élévation de privilèges dans Microsoft DWM Core Library](#cve-2025-30400-vulnérabilité-délévation-de-privilèges-dans-microsoft-dwm-core-library)
* [🐞 CVE-2025-32701 Vulnérabilité d'élévation de privilèges dans le pilote Windows Common Log File System](#cve-2025-32701-vulnérabilité-délévation-de-privilèges-dans-le-pilote-windows-common-log-file-system)
* [🐞 CVE-2025-32703 Vulnérabilité de divulgation d'informations dans Visual Studio](#cve-2025-32703-vulnérabilité-de-divulgation-dinformations-dans-visual-studio)
* [🐞 CVE-2025-32706 Vulnérabilité d'élévation de privilèges dans le pilote Windows Common Log File System](#cve-2025-32706-vulnérabilité-délévation-de-privilèges-dans-le-pilote-windows-common-log-file-system)
* [🐞 CVE-2025-21264 Vulnérabilité de contournement de fonctionnalité de sécurité dans Visual Studio Code](#cve-2025-21264-vulnérabilité-de-contournement-de-fonctionnalité-de-sécurité-dans-visual-studio-code)
* [🐞 CVE-2025-32709 Vulnérabilité d'élévation de privilèges dans le pilote Windows Ancillary Function Driver pour WinSock](#cve-2025-32709-vulnérabilité-délévation-de-privilèges-dans-le-pilote-windows-ancillary-function-driver-pour-winsock)
* [🐞 CVE-2025-26677 Vulnérabilité de déni de service dans Windows Remote Desktop Gateway (RD Gateway)](#cve-2025-26677-vulnérabilité-de-déni-de-service-dans-windows-remote-desktop-gateway-rd-gateway)
* [🐞 CVE-2025-27488 Vulnérabilité d'élévation de privilèges dans Microsoft Windows Hardware Lab Kit (HLK)](#cve-2025-27488-vulnérabilité-délévation-de-privilèges-dans-microsoft-windows-hardware-lab-kit-hlk)
* [🐞 CVE-2025-26685 Vulnérabilité d'usurpation dans Microsoft Defender for Identity](#cve-2025-26685-vulnérabilité-dusurpation-dans-microsoft-defender-for-identity)
* [🐞 CVE-2025-29829 Vulnérabilité de divulgation d'informations dans Windows Trusted Runtime Interface Driver](#cve-2025-29829-vulnérabilité-de-divulgation-dinformations-dans-windows-trusted-runtime-interface-driver)
* [🐞 CVE-2025-29830 Vulnérabilité de divulgation d'informations dans Windows Routing and Remote Access Service (RRAS)](#cve-2025-29830-vulnérabilité-de-divulgation-dinformations-dans-windows-routing-and-remote-access-service-rras)
* [🐞 CVE-2025-29831 Vulnérabilité d'exécution de code à distance dans Windows Remote Desktop Services](#cve-2025-29831-vulnérabilité-dexécution-de-code-à-distance-dans-windows-remote-desktop-services)
* [🐞 CVE-2025-29832 Vulnérabilité de divulgation d'informations dans Windows Routing and Remote Access Service (RRAS)](#cve-2025-29832-vulnérabilité-de-divulgation-dinformations-dans-windows-routing-and-remote-access-service-rras)
* [🐞 CVE-2025-29833 Vulnérabilité d'exécution de code à distance dans Microsoft Virtual Machine Bus (VMBus)](#cve-2025-29833-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-virtual-machine-bus-vmbus)
* [🐞 CVE-2025-29835 Vulnérabilité de divulgation d'informations dans Windows Remote Access Connection Manager](#cve-2025-29835-vulnérabilité-de-divulgation-dinformations-dans-windows-remote-access-connection-manager)
* [🐞 CVE-2025-29836 Vulnérabilité de divulgation d'informations dans Windows Routing and Remote Access Service (RRAS)](#cve-2025-29836-vulnérabilité-de-divulgation-dinformations-dans-windows-routing-and-remote-access-service-rras)
* [🐞 CVE-2025-29837 Vulnérabilité de divulgation d'informations dans Windows Installer](#cve-2025-29837-vulnérabilité-de-divulgation-dinformations-dans-windows-installer)
* [🐞 CVE-2025-29838 Vulnérabilité d'élévation de privilèges dans Windows ExecutionContext Driver](#cve-2025-29838-vulnérabilité-délévation-de-privilèges-dans-windows-executioncontext-driver)
* [🐞 CVE-2025-29839 Vulnérabilité de divulgation d'informations dans Windows Multiple UNC Provider Driver](#cve-2025-29839-vulnérabilité-de-divulgation-dinformations-dans-windows-multiple-unc-provider-driver)
* [🐞 CVE-2025-29840 Vulnérabilité d'exécution de code à distance dans Windows Media](#cve-2025-29840-vulnérabilité-dexécution-de-code-à-distance-dans-windows-media)
* [🐞 CVE-2025-29841 Vulnérabilité d'élévation de privilèges dans Universal Print Management Service](#cve-2025-29841-vulnérabilité-délévation-de-privilèges-dans-universal-print-management-service)
* [🐞 CVE-2025-29842 Vulnérabilité de contournement de fonctionnalité de sécurité dans UrlMon](#cve-2025-29842-vulnérabilité-de-contournement-de-fonctionnalité-de-sécurité-dans-urlmon)
* [🐞 CVE-2025-29954 Vulnérabilité de déni de service dans Windows Lightweight Directory Access Protocol (LDAP)](#cve-2025-29954-vulnérabilité-de-déni-de-service-dans-windows-lightweight-directory-access-protocol-ldap)
* [🐞 CVE-2025-29955 Vulnérabilité de déni de service dans Windows Hyper-V](#cve-2025-29955-vulnérabilité-de-déni-de-service-dans-windows-hyper-v)
* [🐞 CVE-2025-29956 Vulnérabilité de divulgation d'informations dans Windows SMB](#cve-2025-29956-vulnérabilité-de-divulgation-dinformations-dans-windows-smb)
* [🐞 CVE-2025-29957 Vulnérabilité de déni de service dans Windows Deployment Services](#cve-2025-29957-vulnérabilité-de-déni-de-service-dans-windows-deployment-services)
* [🐞 CVE-2025-29958 Vulnérabilité de divulgation d'informations dans Windows Routing and Remote Access Service (RRAS)](#cve-2025-29958-vulnérabilité-de-divulgation-dinformations-dans-windows-routing-and-remote-access-service-rras)
* [🐞 CVE-2025-29961 Vulnérabilité de divulgation d'informations dans Windows Routing and Remote Access Service (RRAS)](#cve-2025-29961-vulnérabilité-de-divulgation-dinformations-dans-windows-routing-and-remote-access-service-rras)
* [🐞 CVE-2025-29962 Vulnérabilité d'exécution de code à distance dans Windows Media](#cve-2025-29962-vulnérabilité-dexécution-de-code-à-distance-dans-windows-media)
* [🐞 CVE-2025-29963 Vulnérabilité d'exécution de code à distance dans Windows Media](#cve-2025-29963-vulnérabilité-dexécution-de-code-à-distance-dans-windows-media)
* [🐞 CVE-2025-29974 Vulnérabilité de divulgation d'informations dans Windows Kernel](#cve-2025-29974-vulnérabilité-de-divulgation-dinformations-dans-windows-kernel)
* [🐞 CVE-2025-30385 Vulnérabilité d'élévation de privilèges dans le pilote Windows Common Log File System](#cve-2025-30385-vulnérabilité-délévation-de-privilèges-dans-le-pilote-windows-common-log-file-system)
* [🐞 CVE-2025-30388 Vulnérabilité d'exécution de code à distance dans Windows Graphics Component](#cve-2025-30388-vulnérabilité-dexécution-de-code-à-distance-dans-windows-graphics-component)
* [🐞 CVE-2025-30397 Vulnérabilité de corruption de mémoire dans le moteur de script](#cve-2025-30397-vulnérabilité-de-corruption-de-mémoire-dans-le-moteur-de-script)
* [🐞 CVE-2025-32702 Vulnérabilité d'exécution de code à distance dans Visual Studio](#cve-2025-32702-vulnérabilité-dexécution-de-code-à-distance-dans-visual-studio)
* [🐞 CVE-2025-32704 Vulnérabilité d'exécution de code à distance dans Microsoft Excel](#cve-2025-32704-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-excel)
* [🐞 CVE-2025-32705 Vulnérabilité d'exécution de code à distance dans Microsoft Outlook](#cve-2025-32705-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-outlook)
* [🐞 CVE-2025-32707 Vulnérabilité d'élévation de privilèges dans NTFS](#cve-2025-32707-vulnérabilité-délévation-de-privilèges-dans-ntfs)
* [🐞 CVE-2025-24063 Vulnérabilité d'élévation de privilèges dans le pilote Kernel Streaming Service](#cve-2025-24063-vulnérabilité-délévation-de-privilèges-dans-le-pilote-kernel-streaming-service)
* [🐞 CVE-2025-29979 Vulnérabilité d'exécution de code à distance dans Microsoft Excel](#cve-2025-29979-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-excel)
* [🐞 CVE-2025-26629 Vulnérabilité d'exécution de code à distance dans Microsoft Office](#cve-2025-26629-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-office)


<a name="cve-2025-26646-vulnérabilité-dusurpation-dans-net-visual-studio-et-build-tools-pour-visual-studio"></a>
## 🐞 CVE-2025-26646 Vulnérabilité d'usurpation dans .NET, Visual Studio et Build Tools pour Visual Studio
Le contrôle externe du nom ou du chemin de fichier dans .NET, Visual Studio et Build Tools pour Visual Studio allo
* 🐞 CVE : CVE-2025-26646 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-26646)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-26684-vulnérabilité-délévation-de-privilèges-dans-microsoft-defender"></a>
## 🐞 CVE-2025-26684 Vulnérabilité d'élévation de privilèges dans Microsoft Defender
Le contrôle externe du nom ou du chemin de fichier dans Microsoft Defender for Endpoint permet à un attaquant autorisé
* 🐞 CVE : CVE-2025-26684 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-26684)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29959-vulnérabilité-de-divulgation-dinformations-dans-windows-routing-and-remote-access-service-rras"></a>
## 🐞 CVE-2025-29959 Vulnérabilité de divulgation d'informations dans Windows Routing and Remote Access Service (RRAS)
L'utilisation d'une ressource non initialisée dans Windows Routing and Remote Access Service (RRAS) permet à un attaquant non autorisé
* 🐞 CVE : CVE-2025-29959 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29959)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29960-vulnérabilité-de-divulgation-dinformations-dans-windows-routing-and-remote-access-service-rras"></a>
## 🐞 CVE-2025-29960 Vulnérabilité de divulgation d'informations dans Windows Routing and Remote Access Service (RRAS)
Une lecture hors limites dans Windows Routing and Remote Access Service (RRAS) permet à un attaquant non autorisé
* 🐞 CVE : CVE-2025-29960 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29960)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29964-vulnérabilité-dexécution-de-code-à-distance-dans-windows-media"></a>
## 🐞 CVE-2025-29964 Vulnérabilité d'exécution de code à distance dans Windows Media
Un débordement de tampon basé sur le tas dans Windows Media permet à un attaquant non autorisé d'exécuter du code sur un r
* 🐞 CVE : CVE-2025-29964 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29964)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29966-vulnérabilité-dexécution-de-code-à-distance-dans-le-client-remote-desktop"></a>
## 🐞 CVE-2025-29966 Vulnérabilité d'exécution de code à distance dans le client Remote Desktop
Un débordement de tampon basé sur le tas dans Windows Remote Desktop permet à un attaquant non autorisé d'exécuter du code
* 🐞 CVE : CVE-2025-29966 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29966)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29967-vulnérabilité-dexécution-de-code-à-distance-dans-le-client-remote-desktop"></a>
## 🐞 CVE-2025-29967 Vulnérabilité d'exécution de code à distance dans le client Remote Desktop
Un débordement de tampon basé sur le tas dans Remote Desktop Gateway Service permet à un attaquant non autorisé d'exécuter
* 🐞 CVE : CVE-2025-29967 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29967)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29968-vulnérabilité-de-déni-de-service-dans-active-directory-certificate-services-ad-cs"></a>
## 🐞 CVE-2025-29968 Vulnérabilité de déni de service dans Active Directory Certificate Services (AD CS)
Une validation d'entrée incorrecte dans Active Directory Certificate Services (AD CS) permet à un attaquant autorisé d'atta
* 🐞 CVE : CVE-2025-29968 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29968)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29969-vulnérabilité-dexécution-de-code-à-distance-dans-ms-even-rpc"></a>
## 🐞 CVE-2025-29969 Vulnérabilité d'exécution de code à distance dans MS-EVEN RPC
Une condition de concurrence "time-of-check time-of-use" (toctou) dans Windows Fundamentals permet à un attaquant autorisé
* 🐞 CVE : CVE-2025-29969 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29969)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29970-vulnérabilité-délévation-de-privilèges-dans-microsoft-brokering-file-system"></a>
## 🐞 CVE-2025-29970 Vulnérabilité d'élévation de privilèges dans Microsoft Brokering File System
L'utilisation après libération dans Microsoft Brokering File System permet à un attaquant autorisé d'élever des privilège
* 🐞 CVE : CVE-2025-29970 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29970)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29971-vulnérabilité-de-déni-de-service-dans-web-threat-defense-wtdsys"></a>
## 🐞 CVE-2025-29971 Vulnérabilité de déni de service dans Web Threat Defense (WTD.sys)
Une lecture hors limites dans Web Threat Defense (WTD.sys) permet à un attaquant non autorisé de refuser le service
* 🐞 CVE : CVE-2025-29971 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29971)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29973-vulnérabilité-délévation-de-privilèges-dans-microsoft-azure-file-sync"></a>
## 🐞 CVE-2025-29973 Vulnérabilité d'élévation de privilèges dans Microsoft Azure File Sync
Un contrôle d'accès incorrect dans Azure File Sync permet à un attaquant autorisé d'élever des privilèges local
* 🐞 CVE : CVE-2025-29973 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29973)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29975-vulnérabilité-délévation-de-privilèges-dans-microsoft-pc-manager"></a>
## 🐞 CVE-2025-29975 Vulnérabilité d'élévation de privilèges dans Microsoft PC Manager
Résolution de lien incorrecte avant l'accès au fichier ('link following') dans Microsoft PC Manager permet à un attaquant autorisé
* 🐞 CVE : CVE-2025-29975 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29975)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29976-vulnérabilité-délévation-de-privilèges-dans-microsoft-sharepoint-server"></a>
## 🐞 CVE-2025-29976 Vulnérabilité d'élévation de privilèges dans Microsoft SharePoint Server
Gestion incorrecte des privilèges dans Microsoft Office SharePoint permet à un attaquant autorisé d'élever
* 🐞 CVE : CVE-2025-29976 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29976)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29977-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-excel"></a>
## 🐞 CVE-2025-29977 Vulnérabilité d'exécution de code à distance dans Microsoft Excel
L'utilisation après libération dans Microsoft Office Excel permet à un attaquant non autorisé d'exécuter du code localement.
* 🐞 CVE : CVE-2025-29977 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29977)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29978-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-powerpoint"></a>
## 🐞 CVE-2025-29978 Vulnérabilité d'exécution de code à distance dans Microsoft PowerPoint
L'utilisation après libération dans Microsoft Office PowerPoint permet à un attaquant non autorisé d'exécuter du code locall
* 🐞 CVE : CVE-2025-29978 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29978)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-30375-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-excel"></a>
## 🐞 CVE-2025-30375 Vulnérabilité d'exécution de code à distance dans Microsoft Excel
L'accès à une ressource utilisant un type incompatible ('type confusion') dans Microsoft Office Excel permet à un attaquant non
* 🐞 CVE : CVE-2025-30375 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30375)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-30376-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-excel"></a>
## 🐞 CVE-2025-30376 Vulnérabilité d'exécution de code à distance dans Microsoft Excel
Un débordement de tampon basé sur le tas dans Microsoft Office Excel permet à un attaquant non autorisé d'exécuter du code
* 🐞 CVE : CVE-2025-30376 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30376)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-30377-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-office"></a>
## 🐞 CVE-2025-30377 Vulnérabilité d'exécution de code à distance dans Microsoft Office
L'utilisation après libération dans Microsoft Office permet à un attaquant non autorisé d'exécuter du code localement.
* 🐞 CVE : CVE-2025-30377 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30377)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-30378-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-sharepoint-server"></a>
## 🐞 CVE-2025-30378 Vulnérabilité d'exécution de code à distance dans Microsoft SharePoint Server
La désérialisation de données non fiables dans Microsoft Office SharePoint permet à un attaquant non autorisé de
* 🐞 CVE : CVE-2025-30378 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30378)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-30379-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-excel"></a>
## 🐞 CVE-2025-30379 Vulnérabilité d'exécution de code à distance dans Microsoft Excel
La libération d'un pointeur ou d'une référence invalide dans Microsoft Office Excel permet à un attaquant non autorisé de
* 🐞 CVE : CVE-2025-30379 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30379)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-30381-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-excel"></a>
## 🐞 CVE-2025-30381 Vulnérabilité d'exécution de code à distance dans Microsoft Excel
Une lecture hors limites dans Microsoft Office Excel permet à un attaquant non autorisé d'exécuter du code localement
* 🐞 CVE : CVE-2025-30381 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30381)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-30382-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-sharepoint-server"></a>
## 🐞 CVE-2025-30382 Vulnérabilité d'exécution de code à distance dans Microsoft SharePoint Server
La désérialisation de données non fiables dans Microsoft Office SharePoint permet à un attaquant non autorisé de
* 🐞 CVE : CVE-2025-30382 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30382)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-30383-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-excel"></a>
## 🐞 CVE-2025-30383 Vulnérabilité d'exécution de code à distance dans Microsoft Excel
L'accès à une ressource utilisant un type incompatible ('type confusion') dans Microsoft Office Excel permet à un attaquant non
* 🐞 CVE : CVE-2025-30383 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30383)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-30384-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-sharepoint-server"></a>
## 🐞 CVE-2025-30384 Vulnérabilité d'exécution de code à distance dans Microsoft SharePoint Server
La désérialisation de données non fiables dans Microsoft Office SharePoint permet à un attaquant non autorisé de
* 🐞 CVE : CVE-2025-30384 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30384)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-30386-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-office"></a>
## 🐞 CVE-2025-30386 Vulnérabilité d'exécution de code à distance dans Microsoft Office
L'utilisation après libération dans Microsoft Office permet à un attaquant non autorisé d'exécuter du code localement.
* 🐞 CVE : CVE-2025-30386 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30386)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-30387-vulnérabilité-délévation-de-privilèges-dans-document-intelligence-studio-on-prem"></a>
## 🐞 CVE-2025-30387 Vulnérabilité d'élévation de privilèges dans Document Intelligence Studio On-Prem
Limitation incorrecte d'un chemin d'accès à un répertoire restreint ('path traversal') dans Azure permet à un attaquant non
* 🐞 CVE : CVE-2025-30387 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30387)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-27468-vulnérabilité-délévation-de-privilèges-dans-le-pilote-windows-kernel-mode"></a>
## 🐞 CVE-2025-27468 Vulnérabilité d'élévation de privilèges dans le pilote Windows Kernel-Mode
Gestion incorrecte des privilèges dans Windows Secure Kernel Mode permet à un attaquant autorisé d'élever
* 🐞 CVE : CVE-2025-27468 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-27468)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-30393-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-excel"></a>
## 🐞 CVE-2025-30393 Vulnérabilité d'exécution de code à distance dans Microsoft Excel
L'utilisation après libération dans Microsoft Office Excel permet à un attaquant non autorisé d'exécuter du code localement.
* 🐞 CVE : CVE-2025-30393 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30393)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29826-vulnérabilité-délévation-de-privilèges-dans-microsoft-dataverse"></a>
## 🐞 CVE-2025-29826 Vulnérabilité d'élévation de privilèges dans Microsoft Dataverse
Gestion incorrecte des permissions ou privilèges insuffisants dans Microsoft Dataverse permet à un attaquant autorisé
* 🐞 CVE : CVE-2025-29826 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29826)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-30394-vulnérabilité-de-déni-de-service-dans-windows-remote-desktop-gateway-rd-gateway"></a>
## 🐞 CVE-2025-30394 Vulnérabilité de déni de service dans Windows Remote Desktop Gateway (RD Gateway)
Le stockage de données sensibles dans une mémoire mal verrouillée dans Remote Desktop Gateway Service permet à un attaquant non autorisé
* 🐞 CVE : CVE-2025-30394 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30394)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-30400-vulnérabilité-délévation-de-privilèges-dans-microsoft-dwm-core-library"></a>
## 🐞 CVE-2025-30400 Vulnérabilité d'élévation de privilèges dans Microsoft DWM Core Library
L'utilisation après libération dans Windows DWM permet à un attaquant autorisé d'élever des privilèges localement.
* 🐞 CVE : CVE-2025-30400 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30400)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-32701-vulnérabilité-délévation-de-privilèges-dans-le-pilote-windows-common-log-file-system"></a>
## 🐞 CVE-2025-32701 Vulnérabilité d'élévation de privilèges dans le pilote Windows Common Log File System
L'utilisation après libération dans Windows Common Log File System Driver permet à un attaquant autorisé d'élever pri
* 🐞 CVE : CVE-2025-32701 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32701)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-32703-vulnérabilité-de-divulgation-dinformations-dans-visual-studio"></a>
## 🐞 CVE-2025-32703 Vulnérabilité de divulgation d'informations dans Visual Studio
Granularité insuffisante du contrôle d'accès dans Visual Studio permet à un attaquant autorisé de divulguer
* 🐞 CVE : CVE-2025-32703 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32703)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-32706-vulnérabilité-délévation-de-privilèges-dans-le-pilote-windows-common-log-file-system"></a>
## 🐞 CVE-2025-32706 Vulnérabilité d'élévation de privilèges dans le pilote Windows Common Log File System
Validation d'entrée incorrecte dans Windows Common Log File System Driver permet à un attaquant autorisé
* 🐞 CVE : CVE-2025-32706 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32706)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-21264-vulnérabilité-de-contournement-de-fonctionnalité-de-sécurité-dans-visual-studio-code"></a>
## 🐞 CVE-2025-21264 Vulnérabilité de contournement de fonctionnalité de sécurité dans Visual Studio Code
Fichiers ou répertoires accessibles à des tiers externes dans Visual Studio Code permet à un attaquant non autorisé
* 🐞 CVE : CVE-2025-21264 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21264)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-32709-vulnérabilité-délévation-de-privilèges-dans-le-pilote-windows-ancillary-function-driver-pour-winsock"></a>
## 🐞 CVE-2025-32709 Vulnérabilité d'élévation de privilèges dans le pilote Windows Ancillary Function Driver pour WinSock
L'utilisation après libération dans Windows Ancillary Function Driver for WinSock permet à un attaquant autorisé d'éle
* 🐞 CVE : CVE-2025-32709 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32709)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-26677-vulnérabilité-de-déni-de-service-dans-windows-remote-desktop-gateway-rd-gateway"></a>
## 🐞 CVE-2025-26677 Vulnérabilité de déni de service dans Windows Remote Desktop Gateway (RD Gateway)
Consommation incontrôlée de ressources dans Remote Desktop Gateway Service permet à un attaquant non autorisé
* 🐞 CVE : CVE-2025-26677 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-26677)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-27488-vulnérabilité-délévation-de-privilèges-dans-microsoft-windows-hardware-lab-kit-hlk"></a>
## 🐞 CVE-2025-27488 Vulnérabilité d'élévation de privilèges dans Microsoft Windows Hardware Lab Kit (HLK)
L'utilisation de informations d'identification codées en dur dans Windows Hardware Lab Kit permet à un attaquant autorisé d'élever p
* 🐞 CVE : CVE-2025-27488 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-27488)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-26685-vulnérabilité-dusurpation-dans-microsoft-defender-for-identity"></a>
## 🐞 CVE-2025-26685 Vulnérabilité d'usurpation dans Microsoft Defender for Identity
Authentification incorrecte dans Microsoft Defender for Identity permet à un attaquant non autorisé de perform
* 🐞 CVE : CVE-2025-26685 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-26685)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29829-vulnérabilité-de-divulgation-dinformations-dans-windows-trusted-runtime-interface-driver"></a>
## 🐞 CVE-2025-29829 Vulnérabilité de divulgation d'informations dans Windows Trusted Runtime Interface Driver
L'utilisation d'une ressource non initialisée dans Windows Trusted Runtime Interface Driver permet à un attaquant autorisé
* 🐞 CVE : CVE-2025-29829 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29829)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29830-vulnérabilité-de-divulgation-dinformations-dans-windows-routing-and-remote-access-service-rras"></a>
## 🐞 CVE-2025-29830 Vulnérabilité de divulgation d'informations dans Windows Routing and Remote Access Service (RRAS)
L'utilisation d'une ressource non initialisée dans Windows Routing and Remote Access Service (RRAS) permet à un attaquant non autorisé
* 🐞 CVE : CVE-2025-29830 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29830)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29831-vulnérabilité-dexécution-de-code-à-distance-dans-windows-remote-desktop-services"></a>
## 🐞 CVE-2025-29831 Vulnérabilité d'exécution de code à distance dans Windows Remote Desktop Services
L'utilisation après libération dans Remote Desktop Gateway Service permet à un attaquant non autorisé d'exécuter du code
* 🐞 CVE : CVE-2025-29831 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29831)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29832-vulnérabilité-de-divulgation-dinformations-dans-windows-routing-and-remote-access-service-rras"></a>
## 🐞 CVE-2025-29832 Vulnérabilité de divulgation d'informations dans Windows Routing and Remote Access Service (RRAS)
Une lecture hors limites dans Windows Routing and Remote Access Service (RRAS) permet à un attaquant non autorisé
* 🐞 CVE : CVE-2025-29832 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29832)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29833-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-virtual-machine-bus-vmbus"></a>
## 🐞 CVE-2025-29833 Vulnérabilité d'exécution de code à distance dans Microsoft Virtual Machine Bus (VMBus)
Une condition de concurrence "time-of-check time-of-use" (toctou) dans Windows Virtual Machine Bus permet à un attaquant autorisé
* 🐞 CVE : CVE-2025-29833 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29833)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29835-vulnérabilité-de-divulgation-dinformations-dans-windows-remote-access-connection-manager"></a>
## 🐞 CVE-2025-29835 Vulnérabilité de divulgation d'informations dans Windows Remote Access Connection Manager
Une lecture hors limites dans Windows Routing and Remote Access Service (RRAS) permet à un attaquant non autorisé
* 🐞 CVE : CVE-2025-29835 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29835)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29836-vulnérabilité-de-divulgation-dinformations-dans-windows-routing-and-remote-access-service-rras"></a>
## 🐞 CVE-2025-29836 Vulnérabilité de divulgation d'informations dans Windows Routing and Remote Access Service (RRAS)
Une lecture hors limites dans Windows Routing and Remote Access Service (RRAS) permet à un attaquant non autorisé
* 🐞 CVE : CVE-2025-29836 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29836)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29837-vulnérabilité-de-divulgation-dinformations-dans-windows-installer"></a>
## 🐞 CVE-2025-29837 Vulnérabilité de divulgation d'informations dans Windows Installer
Résolution de lien incorrecte avant l'accès au fichier ('link following') dans Windows Installer permet à un attaquant authorisé
* 🐞 CVE : CVE-2025-29837 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29837)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29838-vulnérabilité-délévation-de-privilèges-dans-windows-executioncontext-driver"></a>
## 🐞 CVE-2025-29838 Vulnérabilité d'élévation de privilèges dans Windows ExecutionContext Driver
Déréférencement de pointeur nul dans Windows Drivers permet à un attaquant non autorisé d'élever des privilèges lo
* 🐞 CVE : CVE-2025-29838 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29838)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29839-vulnérabilité-de-divulgation-dinformations-dans-windows-multiple-unc-provider-driver"></a>
## 🐞 CVE-2025-29839 Vulnérabilité de divulgation d'informations dans Windows Multiple UNC Provider Driver
Une lecture hors limites dans Windows File Server permet à un attaquant non autorisé de divulguer des informations lo
* 🐞 CVE : CVE-2025-29839 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29839)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29840-vulnérabilité-dexécution-de-code-à-distance-dans-windows-media"></a>
## 🐞 CVE-2025-29840 Vulnérabilité d'exécution de code à distance dans Windows Media
Un débordement de tampon basé sur la pile dans Windows Media permet à un attaquant non autorisé d'exécuter du code sur un
* 🐞 CVE : CVE-2025-29840 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29840)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29841-vulnérabilité-délévation-de-privilèges-dans-universal-print-management-service"></a>
## 🐞 CVE-2025-29841 Vulnérabilité d'élévation de privilèges dans Universal Print Management Service
Exécution concurrente utilisant une ressource partagée avec synchronisation incorrecte ('race condition') dans Unive
* 🐞 CVE : CVE-2025-29841 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29841)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29842-vulnérabilité-de-contournement-de-fonctionnalité-de-sécurité-dans-urlmon"></a>
## 🐞 CVE-2025-29842 Vulnérabilité de contournement de fonctionnalité de sécurité dans UrlMon
L'acceptation de données non fiables superflues avec des données fiables dans UrlMon permet à un attaquant non autorisé
* 🐞 CVE : CVE-2025-29842 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29842)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29954-vulnérabilité-de-déni-de-service-dans-windows-lightweight-directory-access-protocol-ldap"></a>
## 🐞 CVE-2025-29954 Vulnérabilité de déni de service dans Windows Lightweight Directory Access Protocol (LDAP)
Consommation incontrôlée de ressources dans Windows LDAP - Lightweight Directory Access Protocol permet à un
* 🐞 CVE : CVE-2025-29954 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29954)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29955-vulnérabilité-de-déni-de-service-dans-windows-hyper-v"></a>
## 🐞 CVE-2025-29955 Vulnérabilité de déni de service dans Windows Hyper-V
Validation d'entrée incorrecte dans Windows Hyper-V permet à un attaquant non autorisé de refuser le service localement
* 🐞 CVE : CVE-2025-29955 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29955)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29956-vulnérabilité-de-divulgation-dinformations-dans-windows-smb"></a>
## 🐞 CVE-2025-29956 Vulnérabilité de divulgation d'informations dans Windows SMB
Lecture excessive de tampon dans Windows SMB permet à un attaquant autorisé de divulguer des informations sur un réseau
* 🐞 CVE : CVE-2025-29956 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29956)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29957-vulnérabilité-de-déni-de-service-dans-windows-deployment-services"></a>
## 🐞 CVE-2025-29957 Vulnérabilité de déni de service dans Windows Deployment Services
Consommation incontrôlée de ressources dans Windows Deployment Services permet à un attaquant non autorisé
* 🐞 CVE : CVE-2025-29957 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29957)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29958-vulnérabilité-de-divulgation-dinformations-dans-windows-routing-and-remote-access-service-rras"></a>
## 🐞 CVE-2025-29958 Vulnérabilité de divulgation d'informations dans Windows Routing and Remote Access Service (RRAS)
L'utilisation d'une ressource non initialisée dans Windows Routing and Remote Access Service (RRAS) permet à un attaquant non autorisé
* 🐞 CVE : CVE-2025-29958 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29958)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29961-vulnérabilité-de-divulgation-dinformations-dans-windows-routing-and-remote-access-service-rras"></a>
## 🐞 CVE-2025-29961 Vulnérabilité de divulgation d'informations dans Windows Routing and Remote Access Service (RRAS)
Une lecture hors limites dans Windows Routing and Remote Access Service (RRAS) permet à un attaquant non autorisé
* 🐞 CVE : CVE-2025-29961 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29961)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29962-vulnérabilité-dexécution-de-code-à-distance-dans-windows-media"></a>
## 🐞 CVE-2025-29962 Vulnérabilité d'exécution de code à distance dans Windows Media
Un débordement de tampon basé sur le tas dans Windows Media permet à un attaquant non autorisé d'exécuter du code sur un r
* 🐞 CVE : CVE-2025-29962 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29962)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29963-vulnérabilité-dexécution-de-code-à-distance-dans-windows-media"></a>
## 🐞 CVE-2025-29963 Vulnérabilité d'exécution de code à distance dans Windows Media
Un débordement de tampon basé sur le tas dans Windows Media permet à un attaquant non autorisé d'exécuter du code sur un r
* 🐞 CVE : CVE-2025-29963 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29963)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29974-vulnérabilité-de-divulgation-dinformations-dans-windows-kernel"></a>
## 🐞 CVE-2025-29974 Vulnérabilité de divulgation d'informations dans Windows Kernel
Un sous-débordement d'entier (wrap ou wraparound) dans Windows Kernel permet à un attaquant non autorisé de divulguer
* 🐞 CVE : CVE-2025-29974 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29974)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-30385-vulnérabilité-délévation-de-privilèges-dans-le-pilote-windows-common-log-file-system"></a>
## 🐞 CVE-2025-30385 Vulnérabilité d'élévation de privilèges dans le pilote Windows Common Log File System
L'utilisation après libération dans Windows Common Log File System Driver permet à un attaquant autorisé d'élever pri
* 🐞 CVE : CVE-2025-30385 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30385)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-30388-vulnérabilité-dexécution-de-code-à-distance-dans-windows-graphics-component"></a>
## 🐞 CVE-2025-30388 Vulnérabilité d'exécution de code à distance dans Windows Graphics Component
Un débordement de tampon basé sur le tas dans Windows Win32K - GRFX permet à un attaquant non autorisé d'exécuter du code
* 🐞 CVE : CVE-2025-30388 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30388)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-30397-vulnérabilité-de-corruption-de-mémoire-dans-le-moteur-de-script"></a>
## 🐞 CVE-2025-30397 Vulnérabilité de corruption de mémoire dans le moteur de script
L'accès à une ressource utilisant un type incompatible ('type confusion') dans Microsoft Scripting Engine permet à un
* 🐞 CVE : CVE-2025-30397 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30397)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-32702-vulnérabilité-dexécution-de-code-à-distance-dans-visual-studio"></a>
## 🐞 CVE-2025-32702 Vulnérabilité d'exécution de code à distance dans Visual Studio
Neutralisation incorrecte d'éléments spéciaux utilisés dans une commande ('command injection') dans Visual Studio
* 🐞 CVE : CVE-2025-32702 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32702)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-32704-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-excel"></a>
## 🐞 CVE-2025-32704 Vulnérabilité d'exécution de code à distance dans Microsoft Excel
Une lecture excessive de tampon dans Microsoft Office Excel permet à un attaquant non autorisé d'exécuter du code localement.
* 🐞 CVE : CVE-2025-32704 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32704)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-32705-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-outlook"></a>
## 🐞 CVE-2025-32705 Vulnérabilité d'exécution de code à distance dans Microsoft Outlook
Une lecture hors limites dans Microsoft Office Outlook permet à un attaquant non autorisé d'exécuter du code local
* 🐞 CVE : CVE-2025-32705 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32705)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-32707-vulnérabilité-délévation-de-privilèges-dans-ntfs"></a>
## 🐞 CVE-2025-32707 Vulnérabilité d'élévation de privilèges dans NTFS
Une lecture hors limites dans Windows NTFS permet à un attaquant non autorisé d'élever des privilèges localement.
* 🐞 CVE : CVE-2025-32707 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32707)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-24063-vulnérabilité-délévation-de-privilèges-dans-le-pilote-kernel-streaming-service"></a>
## 🐞 CVE-2025-24063 Vulnérabilité d'élévation de privilèges dans le pilote Kernel Streaming Service
Un débordement de tampon basé sur le tas dans Windows Kernel permet à un attaquant autorisé d'élever des privilèges loc
* 🐞 CVE : CVE-2025-24063 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-24063)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-29979-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-excel"></a>
## 🐞 CVE-2025-29979 Vulnérabilité d'exécution de code à distance dans Microsoft Excel
Un débordement de tampon basé sur le tas dans Microsoft Office Excel permet à un attaquant non autorisé d'exécuter du code
* 🐞 CVE : CVE-2025-29979 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29979)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z

<a name="cve-2025-26629-vulnérabilité-dexécution-de-code-à-distance-dans-microsoft-office"></a>
## 🐞 CVE-2025-26629 Vulnérabilité d'exécution de code à distance dans Microsoft Office
Pour traiter de manière exhaustive CVE-2025-26629, Microsoft a publié les mises à jour de sécurité de mai 2025 pour tous
* 🐞 CVE : CVE-2025-26629 (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-26629)
* 📊 CVSS : Non disponible dans le flux
* 📈 EPSS : Non disponible dans le flux
* Date de publication : Tue, 13 May 2025 07:00:00 Z
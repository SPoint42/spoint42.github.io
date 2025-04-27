---
layout: post
title: "Veille automatisée du 2025-04-27 via Gemini gemini-2.5-flash-preview-04-17"
date: 2025-04-27
categories:
    - veille
    - vulnérabilités
    - sécurité
---
yaml
---
layout: post
title: Bulletin de Sécurité Cyber - Résumé des Alertes Récentes (20-27 Avril 2025)
date: 2025-04-27 08:00:00 +0200
categories: [cybersecurity, vulnerabilities, monitoring, jekyll]
tags: [vulnerability, CVE, CVSS, exploit, security, patch, advisory, threatintel]
---

# ⚠️Important Security Alerts (CVSS > 7.5)⚠️

* 🚨 Nouvelle Faille Critique SAP NetWeaver Exploitée pour Déployer un Web Shell et le Framework Brute Ratel
* 🚨 Le Malware DslogdRAT Déployé via une Journée Zéro Ivanti ICS (CVE-2025-0282) lors d'Attaques au Japon

## Table of Contents

* [🚨 Nouvelle Faille Critique SAP NetWeaver Exploitée pour Déployer un Web Shell et le Framework Brute Ratel](#nouvelle-faille-critique-sap-netweaver-exploitée-pour-déployer-un-web-shell-et-le-framework-brute-ratel)
* [🔍 Des Chercheurs Identifient une Vulnérabilité Rack::Static Permettant des Violations de Données dans les Serveurs Ruby](#des-chercheurs-identifient-une-vulnérabilité-rackstatic-permettant-des-violations-de-données-dans-les-serveurs-ruby)
* [👾 Le Malware DslogdRAT Déployé via une Journée Zéro Ivanti ICS (CVE-2025-0282) lors d'Attaques au Japon](#le-malware-dslogdrat-déployé-via-une-journée-zéro-ivanti-ics-cve-2025-0282-lors-dattaques-au-japon)
* [🐛 CVE-2025-3857 - Condition de Boucle Infinie dans Amazon.IonDotnet](#cve-2025-3857---condition-de-boucle-infinie-dans-amazoniondotnet)

## 🚨 Nouvelle Faille Critique SAP NetWeaver Exploitée pour Déployer un Web Shell et le Framework Brute Ratel

Des acteurs malveillants exploitent probablement une nouvelle vulnérabilité dans SAP NetWeaver pour télécharger des web shells JSP afin de faciliter les téléversements de fichiers non autorisés et l'exécution de code.
L'exploitation est probablement liée soit à une vulnérabilité précédemment divulguée comme CVE-2017-9844, soit à un problème d'inclusion de fichier distant (RFI) non signalé.

* 🔗 CVE Potentiel : CVE-2017-9844 (ou RFI non signalé)
* 📊 CVSS : Potentiellement très élevé (CVSS 9.8 pour CVE-2017-9844)

## 🔍 Des Chercheurs Identifient une Vulnérabilité Rack::Static Permettant des Violations de Données dans les Serveurs Ruby

Des chercheurs en cybersécurité ont divulgué trois failles de sécurité dans l'interface de serveur web Ruby Rack qui, si elles sont exploitées avec succès, pourraient permettre à des attaquants d'obtenir un accès non autorisé à des fichiers, d'injecter des données malveillantes et de falsifier des logs sous certaines conditions.
La vulnérabilité CVE-2025-27610 a été signalée par OPSWAT.

* 🔗 CVE : CVE-2025-27610 - [https://nvd.nist.gov/vuln/detail/CVE-2025-27610](https://nvd.nist.gov/vuln/detail/CVE-2025-27610)
* 📊 CVSS : 7.5

## 👾 Le Malware DslogdRAT Déployé via une Journée Zéro Ivanti ICS (CVE-2025-0282) lors d'Attaques au Japon

Des chercheurs en cybersécurité alertent sur un nouveau malware appelé DslogdRAT qui est installé suite à l'exploitation d'une faille de sécurité maintenant corrigée dans Ivanti Connect Secure (ICS).
Le malware, ainsi qu'un web shell, ont été "installés en exploitant une vulnérabilité de type journée zéro à l'époque, CVE-2025-0282, lors d'attaques contre des organisations au Japon autour de décembre 2024", selon un chercheur de JPCERT/CC.

* 🔗 CVE : CVE-2025-0282 - [https://nvd.nist.gov/vuln/detail/CVE-2025-0282](https://nvd.nist.gov/vuln/detail/CVE-2025-0282)
* 📊 CVSS : Très élevé (potentiellement > 7.5 car exploitée en journée zéro)

## 🐛 CVE-2025-3857 - Condition de Boucle Infinie dans Amazon.IonDotnet

Une condition de boucle infinie (CVE-2025-3857) a été identifiée dans Amazon.IonDotnet. Lors de la lecture de données binaires Ion via la classe RawBinaryReader, la bibliothèque ne vérifie pas le nombre d'octets lus, déclenchant une boucle infinie en cas de données malformées ou tronquées, pouvant entraîner un déni de service (DoS). Une correction a été publiée dans la version 1.3.1.

* 🔗 CVE : CVE-2025-3857 - [https://www.cve.org/CVERecord?id=CVE-2025-3857](https://www.cve.org/CVERecord?id=CVE-2025-3857)
* 📊 CVSS : 7.5
* 🛠️ Résolution : Mettre à jour vers Amazon.IonDotnet version 1.3.1.
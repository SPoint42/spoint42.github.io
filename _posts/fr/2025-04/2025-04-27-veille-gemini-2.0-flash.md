---
layout: post
title: "Veille automatisée du 2025-04-27 via Gemini gemini-2.0-flash"
date: 2025-04-27
categories:
    - veille
    - vulnérabilités
    - sécurité
---

# ⚠️Important Security Alerts (CVSS > 7.5)⚠️
🚨 Researchers Identify Rack::Static Vulnerability Enabling Data Breaches in Ruby Servers
🚨 CVE-2025-27610 - A path traversal

## Table of Contents
*   [🚨Researchers Identify Rack::Static Vulnerability Enabling Data Breaches in Ruby Servers](#researchers-identify-rackstatic-vulnerability-enabling-data-breaches-in-ruby-servers)
*   [🚨CVE-2025-27610 - A path traversal](#cve-2025-27610---a-path-traversal)
*   [🍎Multiples vulnérabilités dans les produits Apple (17 avril 2025)](#multiples-vulnérabilités-dans-les-produits-apple-17-avril-2025)
*   [♾️CVE-2025-3857 - Infinite loop condition in Amazon.IonDotnet](#cve-2025-3857---infinite-loop-condition-in-amazoniondotnet)

## 🚨Researchers Identify Rack::Static Vulnerability Enabling Data Breaches in Ruby Servers
Cybersecurity researchers have disclosed three security flaws in the Rack Ruby web server interface that, if successfully exploited, could enable attackers to gain unauthorized access to files, inject malicious data, and tamper with logs under certain conditions.
The vulnerabilities, flagged by cybersecurity vendor OPSWAT, are listed below -
CVE-2025-27610 (CVSS score: 7.5) - A path traversal

*   :cve: CVE-2025-27610
*   :cvss: CVSS score: 7.5

## 🚨CVE-2025-27610 - A path traversal
Cybersecurity researchers have disclosed a security flaw in the Rack Ruby web server interface that, if successfully exploited, could enable attackers to gain unauthorized access to files, inject malicious data, and tamper with logs under certain conditions.
The vulnerabilities, flagged by cybersecurity vendor OPSWAT, are listed below -
CVE-2025-27610 (CVSS score: 7.5) - A path traversal

*   :cve: CVE-2025-27610
*   :cvss: CVSS score: 7.5

## 🍎Multiples vulnérabilités dans les produits Apple (17 avril 2025)
De multiples vulnérabilités ont été découvertes dans les produits Apple. Elles permettent à un attaquant de provoquer une exécution de code arbitraire et un contournement de la politique de sécurité. Apple indique que les vulnérabilités CVE-2025-31200 et CVE-2025-31201 sont activement exploitées.

Plusieurs vulnérabilités ont été découvertes dans les produits Apple. Elles permettent à un attaquant d'exécuter du code arbitraire et de contourner la politique de sécurité. Apple indique que les vulnérabilités CVE-2025-31200 et CVE-2025-31201 sont activement exploitées.

*   :cve: CVE-2025-31200
*   :cve: CVE-2025-31201

## ♾️CVE-2025-3857 - Infinite loop condition in Amazon.IonDotnet
We identified CVE-2025-3857, an infinite loop condition in Amazon.IonDotnet. When reading binary Ion data through this library using the RawBinaryReader class, Amazon.IonDotnet does not check the number of bytes read from the underlying stream while deserializing the binary format. If the Ion data is malformed or truncated, this triggers an infinite loop condition that could potentially result in a denial of service.
We released a fix in version 1.3.1 and recommend users upgrade to address this issue. Additionally, ensure any forked or derivative code is patched to incorporate the new fixes.

Nous avons identifié CVE-2025-3857, une condition de boucle infinie dans Amazon.IonDotnet. Lors de la lecture de données Ion binaires via cette bibliothèque à l'aide de la classe RawBinaryReader, Amazon.IonDotnet ne vérifie pas le nombre d'octets lus à partir du flux sous-jacent lors de la désérialisation du format binaire. Si les données Ion sont malformées ou tronquées, cela déclenche une condition de boucle infinie qui pourrait potentiellement entraîner un déni de service.
Nous avons publié un correctif dans la version 1.3.1 et recommandons aux utilisateurs de mettre à niveau pour résoudre ce problème. De plus, assurez-vous que tout code dérivé ou bifurqué est corrigé pour intégrer les nouveaux correctifs.

*   :cve: [CVE-2025-3857](https://www.cve.org/CVERecord?id=CVE-2025-3857)

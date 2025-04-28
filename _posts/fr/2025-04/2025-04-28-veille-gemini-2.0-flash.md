---
layout: post
title: "Veille automatisée du 2025-04-28 via Gemini gemini-2.0-flash"
date: 2025-04-28
categories:
    - veille
    - vulnérabilités
    - sécurité
---

# ⚠️Important Security Alerts (CVSS > 7.5)⚠️
🚨 Hackers exploitent des failles critiques dans Craft CMS; Des centaines de serveurs probablement compromis
🚨 Researchers Identify Rack::Static Vulnerability Enabling Data Breaches in Ruby Servers
🚨 CVE-2025-3857 - Condition de boucle infinie dans Amazon.IonDotnet

## Table of Contents
*   [🚨 Hackers exploitent des failles critiques dans Craft CMS; Des centaines de serveurs probablement compromis](#hackers-exploitent-des-failles-critiques-dans-craft-cms-des-centaines-de-serveurs-probablement-compromis)
*   [🚨 Researchers Identify Rack::Static Vulnerability Enabling Data Breaches in Ruby Servers](#researchers-identify-rackstatic-vulnerability-enabling-data-breaches-in-ruby-servers)
*   [🚨 CVE-2025-3857 - Condition de boucle infinie dans Amazon.IonDotnet](#cve-2025-3857---condition-de-boucle-infinie-dans-amazoniondotnet)

## 🚨 Hackers exploitent des failles critiques dans Craft CMS; Des centaines de serveurs probablement compromis
Des acteurs de menace ont été observés en train d'exploiter deux failles de sécurité critiques nouvellement divulguées dans Craft CMS lors d'attaques zero-day pour violer des serveurs et obtenir un accès non autorisé. Les attaques, observées pour la première fois par Orange Cyberdefense SensePost le 14 février 2025, impliquent le chaînage des vulnérabilités ci-dessous :
CVE-2024-58136 (score CVSS : 9,0) - Une protection inappropriée d'une faille de chemin alternatif dans le Yii PHP.

*   CVE: 🚨 [CVE-2024-58136](https://www.cve.org/CVERecord?id=CVE-2024-58136)
*   CVSS: 🚨 9.0

## 🚨 Researchers Identify Rack::Static Vulnerability Enabling Data Breaches in Ruby Servers
Des chercheurs en cybersécurité ont révélé trois failles de sécurité dans l'interface de serveur Web Rack Ruby qui, si elles sont exploitées avec succès, pourraient permettre aux attaquants d'obtenir un accès non autorisé aux fichiers, d'injecter des données malveillantes et de falsifier les journaux dans certaines conditions. Les vulnérabilités, signalées par le fournisseur de cybersécurité OPSWAT, sont répertoriées ci-dessous : CVE-2025-27610 (score CVSS : 7,5) - Une traversée de chemin.

*   CVE: 🚨 [CVE-2025-27610](https://www.cve.org/CVERecord?id=CVE-2025-27610)
*   CVSS: 🚨 7.5

## 🚨 CVE-2025-3857 - Condition de boucle infinie dans Amazon.IonDotnet
Amazon.IonDotnet (ion-dotnet) est une bibliothèque .NET avec une implémentation du format de sérialisation de données Ion. Nous avons identifié CVE-2025-3857, une condition de boucle infinie dans Amazon.IonDotnet. Lors de la lecture de données Ion binaires via cette bibliothèque à l'aide de la classe RawBinaryReader, Amazon.IonDotnet ne vérifie pas le nombre d'octets lus à partir du flux sous-jacent lors de la désérialisation du format binaire. Si les données Ion sont malformées ou tronquées, cela déclenche une condition de boucle infinie qui pourrait potentiellement entraîner un déni de service.

*   CVE: 🚨 [CVE-2025-3857](https://www.cve.org/CVERecord?id=CVE-2025-3857)

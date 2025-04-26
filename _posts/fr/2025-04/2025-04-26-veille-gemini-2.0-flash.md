---
layout: post
title: "Veille automatisée du 2025-04-26 via Gemini gemini-2.0-flash"
date: 2025-04-26
categories:
    - veille
    - vulnérabilités
    - sécurité
---

# ⚠️Important Security Alerts (CVSS > 7.5)⚠️
🚨 Researchers Identify Rack::Static Vulnerability Enabling Data Breaches in Ruby Servers
🚨 Critical Commvault Command Center Flaw Enables Attackers to Execute Code Remotely

## Table of Contents

*   [🚨 Les chercheurs identifient une vulnérabilité Rack::Static permettant des violations de données dans les serveurs Ruby](#les-chercheurs-identifient-une-vulnerabilite-rackstatic-permettant-des-violations-de-donnees-dans-les-serveurs-ruby)
*   [🚨 Une faille critique dans Commvault Command Center permet aux attaquants d'exécuter du code à distance](#une-faille-critique-dans-commvault-command-center-permet-aux-attaquants-dexecuter-du-code-a-distance)
*   [🐛 CVE-2025-3857 - Condition de boucle infinie dans Amazon.IonDotnet](#cve-2025-3857---condition-de-boucle-infinie-dans-amazoniondotnet)

## 🚨 Les chercheurs identifient une vulnérabilité Rack::Static permettant des violations de données dans les serveurs Ruby

Des chercheurs en cybersécurité ont révélé trois failles de sécurité dans l'interface de serveur Web Rack Ruby qui, si elles sont exploitées avec succès, pourraient permettre aux attaquants d'obtenir un accès non autorisé aux fichiers, d'injecter des données malveillantes et d'altérer les journaux sous certaines conditions.

Les vulnérabilités, signalées par le fournisseur de cybersécurité OPSWAT, sont énumérées ci-dessous :

CVE-2025-27610 (score CVSS : 7,5) - Une traversée de chemin.

*   🐛 CVE-2025-27610 <https://www.cve.org/CVERecord?id=CVE-2025-27610>
*   🔥 CVSS: 7.5

## 🚨 Une faille critique dans Commvault Command Center permet aux attaquants d'exécuter du code à distance

Une faille de sécurité critique a été divulguée dans Commvault Command Center qui pourrait permettre à des attaquants d'exécuter du code à distance.

## 🐛 CVE-2025-3857 - Condition de boucle infinie dans Amazon.IonDotnet

Amazon.IonDotnet (ion-dotnet) est une bibliothèque .NET avec une implémentation du format de sérialisation de données Ion.

Une condition de boucle infinie dans Amazon.IonDotnet a été identifiée. Lors de la lecture de données Ion binaires via cette bibliothèque à l'aide de la classe RawBinaryReader, Amazon.IonDotnet ne vérifie pas le nombre d'octets lus à partir du flux sous-jacent lors de la désérialisation du format binaire. Si les données Ion sont mal formées ou tronquées, cela déclenche une condition de boucle infinie qui pourrait potentiellement entraîner un déni de service.

Un correctif a été publié dans la version 1.3.1 et il est recommandé aux utilisateurs de mettre à niveau pour résoudre ce problème. De plus, assurez-vous que tout code forké ou dérivé est corrigé pour intégrer les nouveaux correctifs.

*   🐛 CVE-2025-3857 <https://www.cve.org/CVERecord?id=CVE-2025-3857>

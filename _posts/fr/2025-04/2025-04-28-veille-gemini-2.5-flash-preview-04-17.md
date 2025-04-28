---
layout: post
title: "Veille automatisée du 2025-04-28 via Gemini gemini-2.5-flash-preview-04-17"
date: 2025-04-28
categories:
    - veille
    - vulnérabilités
    - sécurité
---
# ⚠️Alertes de Sécurité Importantes (CVSS > 7.5)⚠️

## Table des Matières
*   [🐛 CVE-2025-3857 - Condition de boucle infinie dans Amazon.IonDotnet](#--cve-2025-3857---condition-de-boucle-infinie-dans-amazoniondotnet)

## 🐛 CVE-2025-3857 - Condition de boucle infinie dans Amazon.IonDotnet

Une condition de boucle infinie (CVE-2025-3857) a été identifiée dans la bibliothèque .NET Amazon.IonDotnet (ion-dotnet), utilisée pour la désérialisation de données Ion. Lors de la lecture de données Ion binaires via la classe `RawBinaryReader`, la bibliothèque ne vérifie pas le nombre d'octets lus à partir du flux sous-jacent lors de la désérialisation du format binaire. Si les données Ion sont malformées ou tronquées, cela déclenche une condition de boucle infinie qui pourrait potentiellement entraîner un déni de service (DoS). Une correction a été publiée dans la version 1.3.1.

*   🐛 CVE: [CVE-2025-3857](https://www.cve.org/CVERecord?id=CVE-2025-3857)
*   🛡️ Versions affectées: <= 1.3.0
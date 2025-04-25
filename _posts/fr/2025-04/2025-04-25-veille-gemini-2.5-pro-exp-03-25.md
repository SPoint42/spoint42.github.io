---
layout: post
title: "Veille automatisée du 2025-04-25 via Gemini gemini-2.5-pro-exp-03-25"
date: 2025-04-25
categories:
    - veille
    - vulnérabilités
    - sécurité
---
# ⚠️Alertes de Sécurité Importantes (CVSS > 7.5)⚠️
Aucune vulnérabilité critique (CVSS > 7.5) identifiée dans les articles publiés ou mis à jour entre le 18 et le 25 avril 2025.

## Table des Matières
*   [CVE-2025-3857 - Condition de boucle infinie dans Amazon.IonDotnet](#️-cve-2025-3857---condition-de-boucle-infinie-dans-amazoniondotnet)

## <0xF0><0x9F><0x94><0x97> CVE-2025-3857 - Condition de boucle infinie dans Amazon.IonDotnet
Une condition de boucle infinie a été identifiée dans la bibliothèque .NET Amazon.IonDotnet (ion-dotnet). Lors de la lecture de données binaires Ion via la classe `RawBinaryReader`, la bibliothèque (versions <=1.3.0) ne vérifie pas le nombre d'octets lus depuis le flux sous-jacent. Si les données Ion sont malformées ou tronquées, cela déclenche une boucle infinie pouvant potentiellement entraîner un déni de service. Il est recommandé de mettre à jour vers la version 1.3.1 qui contient le correctif.
*   <0xF0><0x9F><0x94><0x91> CVE : [CVE-2025-3857](https://www.cve.org/CVERecord?id=CVE-2025-3857)
*   <0xF0><0x9F><0x9A><0xA8> Date de Publication : 2025-04-21
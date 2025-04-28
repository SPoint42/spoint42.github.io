---
layout: post
title: "Veille automatisée du 2025-04-28 via Gemini gemini-2.5-pro-exp-03-25"
date: 2025-04-28
categories:
    - veille
    - vulnérabilités
    - sécurité
---
# ⚠️Alertes de Sécurité Importantes (CVSS > 7.5)⚠️
    *(Aucune vulnérabilité avec un score CVSS supérieur à 7.5 n'a été identifiée dans les articles publiés durant la période spécifiée)*

## Table des Matières
*   [👾 Vulnérabilité de Boucle Infinie dans Amazon.IonDotnet (CVE-2025-3857)](#-vulnérabilité-de-boucle-infinie-dans-amazoniondotnet-cve-2025-3857)

## 👾 Vulnérabilité de Boucle Infinie dans Amazon.IonDotnet (CVE-2025-3857)
Une vulnérabilité de boucle infinie (CVE-2025-3857) a été identifiée dans la bibliothèque Amazon.IonDotnet (ion-dotnet) pour .NET, utilisée pour la sérialisation des données au format Ion. Lors de la lecture de données Ion binaires via la classe `RawBinaryReader`, la bibliothèque ne vérifie pas le nombre d'octets lus depuis le flux sous-jacent. Si les données Ion sont malformées ou tronquées, cela peut déclencher une boucle infinie, entraînant potentiellement un déni de service (DoS). Un correctif a été publié dans la version 1.3.1 et il est recommandé aux utilisateurs de mettre à niveau.
*   🔑 **CVE :** [CVE-2025-3857](https://www.cve.org/CVERecord?id=CVE-2025-3857)
*   📅 **Date de publication :** 2025-04-21
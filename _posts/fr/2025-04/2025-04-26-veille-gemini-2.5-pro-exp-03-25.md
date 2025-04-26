---
layout: post
title: "Veille automatisée du 2025-04-26 via Gemini gemini-2.5-pro-exp-03-25"
date: 2025-04-26
categories:
    - veille
    - vulnérabilités
    - sécurité
---
# ⚠️Alertes de Sécurité Importantes (CVSS > 7.5)⚠️
Aucune vulnérabilité critique (CVSS > 7.5) n'a été identifiée dans la période de surveillance (19 avril 2025 - 26 avril 2025) sur la base des flux fournis.

## Table des Matières
* [♾️ Boucle infinie dans Amazon.IonDotnet (CVE-2025-3857)](#️-boucle-infinie-dans-amazoniondotnet-cve-2025-3857)

## ♾️ Boucle infinie dans Amazon.IonDotnet (CVE-2025-3857)
Une vulnérabilité de boucle infinie (CVE-2025-3857) a été identifiée dans Amazon.IonDotnet (versions <=1.3.0). Lors de la lecture de données binaires Ion malformées ou tronquées via la classe RawBinaryReader, la bibliothèque ne vérifie pas le nombre d'octets lus du flux sous-jacent, ce qui peut déclencher une boucle infinie et potentiellement entraîner un déni de service (DoS). La version 1.3.1 corrige ce problème. Il est recommandé de mettre à jour et de s'assurer que tout code dérivé ou forké intègre également les correctifs.
*   🏷️ CVE: [CVE-2025-3857](https://www.cve.org/CVERecord?id=CVE-2025-3857)
---
layout: post
title: "Veille automatisée du 2025-04-27 via Gemini gemini-2.5-pro-exp-03-25"
date: 2025-04-27
categories:
    - veille
    - vulnérabilités
    - sécurité
---
# ⚠️Alertes de Sécurité Importantes (CVSS > 7.5)⚠️
<div style='color: #d35400; background-color: #fdf3e6; border-left: 5px solid #d35400; padding: 10px; margin-bottom: 15px;'>
<p>🚨 <a href="#-condition-de-boucle-infinie-dans-amazoniondotnet-cve-2025-3857">Condition de boucle infinie dans Amazon.IonDotnet (CVE-2025-3857)</a></p>
</div>

## Table des Matières
*   [Condition de boucle infinie dans Amazon.IonDotnet (CVE-2025-3857)](#-condition-de-boucle-infinie-dans-amazoniondotnet-cve-2025-3857)

## <a name="-condition-de-boucle-infinie-dans-amazoniondotnet-cve-2025-3857"></a>🚨 Condition de boucle infinie dans Amazon.IonDotnet (CVE-2025-3857)
Une vulnérabilité de type boucle infinie a été identifiée dans la bibliothèque .NET Amazon.IonDotnet, utilisée pour le format de sérialisation de données Ion. Lors de la lecture de données Ion binaires via la classe `RawBinaryReader`, la bibliothèque ne vérifie pas le nombre d'octets lus depuis le flux sous-jacent. Si les données Ion sont malformées ou tronquées, cela déclenche une boucle infinie pouvant entraîner un déni de service (DoS). Un correctif a été publié dans la version 1.3.1 et il est recommandé de mettre à niveau. Assurez-vous également que tout code dérivé ou forké intègre ces correctifs.
*   <img src="https://img.shields.io/static/v1?label=CVE&message=CVE-2025-3857&color=critical" alt="CVE Badge"/> [CVE-2025-3857](https://www.cve.org/CVERecord?id=CVE-2025-3857)
*   <img src="https://img.shields.io/static/v1?label=CVSS&message=7.5&color=high" alt="CVSS Badge"/> 7.5 (Élevé)
*   <img src="https://img.shields.io/static/v1?label=DATE&message=2025-04-21&color=informational" alt="Publication Date Badge"/> 21/04/2025
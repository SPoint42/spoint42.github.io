---
layout: post
title: "Veille automatisée du 2025-04-26 via Gemini gemini-2.5-flash-preview-04-17"
date: 2025-04-26
categories:
    - veille
    - vulnérabilités
    - sécurité
---
# ⚠️Alertes de Sécurité Importantes (CVSS > 7.5)⚠️
Aucune alerte importante (CVSS > 7.5) n'a été identifiée dans les articles qualifiants de cette période basés sur les informations fournies.

## Table des Matières
* [🐛 CVE-2025-3857 - Condition de boucle infinie dans Amazon.IonDotnet](#cve-2025-3857---condition-de-boucle-infinie-dans-amazoniondotnet)

## 📝 CVE-2025-3857 - Condition de boucle infinie dans Amazon.IonDotnet
Une condition de boucle infinie (CVE-2025-3857) a été découverte dans Amazon.IonDotnet, une librairie .NET implémentant le format de sérialisation Ion. Ce problème se produit lors de la lecture de données binaires Ion via la classe `RawBinaryReader`. Si les données sont malformées ou tronquées, la librairie ne vérifie pas correctement le nombre d'octets lus, déclenchant une boucle infinie qui peut entraîner un déni de service. Une correction est disponible dans la version 1.3.1. Il est fortement recommandé aux utilisateurs de mettre à jour leurs installations et de patcher tout code dérivé.
* 🐛 CVE: CVE-2025-3857 [🔗](https://www.cve.org/CVERecord?id=CVE-2025-3857)
* Affecté: &lt;= 1.3.0
* Résolution: Mise à jour vers la version 1.3.1 ou supérieure
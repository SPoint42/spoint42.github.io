---
layout: post
title: "Veille automatisée du 2025-05-01 via Gemini gemini-2.0-flash"
date: 2025-05-01
categories:
    - veille
    - vulnérabilités
    - sécurité
---

# ⚠️Important Security Alerts (CVSS > 7.5)⚠️
🚨 SonicWall Confirms Active Exploitation of Flaws Affecting Multiple Appliance Models

## Table of Contents

*   [🚨 Pourquoi les meilleures équipes SOC se tournent vers la détection et la réponse réseau](#pourquoi-les-meilleures-equipes-soc-se-tournent-vers-la-detection-et-la-reponse-reseau)
*   [🤖 Claude AI Exploité pour Opérer Plus de 100 Personnalités Politiques Fake dans une Campagne d'Influence Mondiale](#claude-ai-exploite-pour-operer-plus-de-100-personnalites-politiques-fake-dans-une-campagne-dinfluence-mondiale)
*   [📉 Nouvelles Recherches Révèlent: 95% des Correctifs AppSec Ne Réduisent Pas le Risque](#nouvelles-recherches-revelent-95-des-correctifs-appsec-ne-reduisent-pas-le-risque)
*   [🇷🇺 Les Malwares DarkWatchman et Sheriff Frappent la Russie et l'Ukraine avec Discrétion et Tactiques de Niveau National](#les-malwares-darkwatchman-et-sheriff-frappent-la-russie-et-lukraine-avec-discretion-et-tactiques-de-niveau-national)
*   [☁️ Commvault Confirme que des Hackers ont Exploité CVE-2025-3928 comme Zero-Day dans une Brèche Azure](#commvault-confirme-que-des-hackers-ont-exploite-cve-2025-3928-comme-zero-day-dans-une-breche-azure)
*   [🔒 SonicWall Confirme l'Exploitation Active de Vulnérabilités Affectant Plusieurs Modèles d'Appareils](#sonicwall-confirme-lexploitation-active-de-vulnerabilites-affectant-plusieurs-modeles-dappareils)
*   [🧪 Des Chercheurs Démontrent Comment l'Injection d'Invite MCP Peut Être Utilisée à la Fois pour l'Attaque et la Défense](#des-chercheurs-demontrent-comment-linjection-dinvite-mcp-peut-etre-utilisee-a-la-fois-pour-lattaque-et-la-defense)
*   [🧑‍💻 \[Webinaire Gratuit] Guide pour Sécuriser l'Ensemble de Votre Cycle de Vie de l'Identité Contre les Menaces Basées sur l'IA](#webinaire-gratuit-guide-pour-securiser-lensemble-de-votre-cycle-de-vie-de-lidentite-contre-les-menaces-basees-sur-lia)
*   [🇨🇳 Des Hackers Chinois Abusent d'IPv6 SLAAC pour des Attaques AitM via l'Outil de Mouvement Latéral Spellbinder](#des-hackers-chinois-abusent-dipv6-slaac-pour-des-attaques-aitm-via-loutil-de-mouvement-lateral-spellbinder)
*   [💰 Les Prises de Contrôle de Comptes Clients: Le Problème de Plusieurs Milliards de Dollars Dont Vous N'Êtes Pas au Courant](#les-prises-de-controle-de-comptes-clients-le-probleme-de-plusieurs-milliards-de-dollars-dont-vous-netes-pas-au-courant)
*   [🕷️ Nebulous Mantis Cible des Entités Liées à l'OTAN avec des Attaques de Malware Multi-Étapes](#nebulous-mantis-cible-des-entites-liees-a-lotan-avec-des-attaques-de-malware-multi-etapes)
*   [🛡️ Vulnérabilité dans Synacor Zimbra Collaboration (28 janvier 2025)](#vulnerabilite-dans-synacor-zimbra-collaboration-28-janvier-2025)
*   [🍎 Multiples Vulnérabilités dans les produits Apple (01 avril 2025)](#multiples-vulnerabilites-dans-les-produits-apple-01-avril-2025)
*   [🏢 Multiples vulnérabilités dans les produits SAP (08 avril 2025)](#multiples-vulnerabilites-dans-les-produits-sap-08-avril-2025)
*   [🚇 Transports urbains - État de la menace informatique (17 avril 2025)](#transports-urbains-etat-de-la-menace-informatique-17-avril-2025)
*   [🐧 Multiples vulnérabilités dans le noyau Linux de Red Hat (18 avril 2025)](#multiples-vulnerabilites-dans-le-noyau-linux-de-red-hat-18-avril-2025)
*   [🛡️ Multiples vulnérabilités dans Tenable Nessus (18 avril 2025)](#multiples-vulnerabilites-dans-tenable-nessus-18-avril-2025)
*   [🐧 Multiples vulnérabilités dans le noyau Linux de Debian (18 avril 2025)](#multiples-vulnerabilites-dans-le-noyau-linux-de-debian-18-avril-2025)
*   [🌐 Multiples vulnérabilités dans Microsoft Edge (18 avril 2025)](#multiples-vulnerabilites-dans-microsoft-edge-18-avril-2025)
*   [⚙️ Vulnérabilité dans les produits Moxa (18 avril 2025)](#vulnerabilite-dans-les-produits-moxa-18-avril-2025)
*   [🏢 Vulnérabilité dans Liferay (18 avril 2025)](#vulnerabilite-dans-liferay-18-avril-2025)
*   [🏢 Multiples vulnérabilités dans les produits IBM (18 avril 2025)](#multiples-vulnerabilites-dans-les-produits-ibm-18-avril-2025)
*   [🐧 Multiples vulnérabilités dans le noyau Linux de SUSE (18 avril 2025)](#multiples-vulnerabilites-dans-le-noyau-linux-de-suse-18-avril-2025)
*   [🐧 Multiples vulnérabilités dans le noyau Linux d'Ubuntu (18 avril 2025)](#multiples-vulnerabilites-dans-le-noyau-linux-dubuntu-18-avril-2025)
*   [📰 Bulletin d'actualité CERTFR-2025-ACT-016 (22 avril 2025)](#bulletin-dactualite-certfr-2025-act-016-22-avril-2025)
*   [🛡️ Vulnérabilité dans PostgreSQL PgBouncer (22 avril 2025)](#vulnerabilite-dans-postgresql-pgbouncer-22-avril-2025)
*   [🚗 Multiples vulnérabilités dans Traefik (22 avril 2025)](#multiples-vulnerabilites-dans-traefik-22-avril-2025)
*   [🛡️ Vulnérabilité dans Tenable Security Center (22 avril 2025)](#vulnerabilite-dans-tenable-security-center-22-avril-2025)
*   [📚 Multiples vulnérabilités dans Moodle (22 avril 2025)](#multiples-vulnerabilites-dans-moodle-22-avril-2025)
*   [♾️ CVE-2025-3857 - Condition de boucle infinie dans Amazon.IonDotnet](#cve-2025-3857---condition-de-boucle-infinie-dans-amazoniondotnet)
*   [🛠️ Problème avec AWS SAM CLI (CVE-2025-3047, CVE-2025-3048)](#probleme-avec-aws-sam-cli-cve-2025-3047-cve-2025-3048)

## 🚨 Pourquoi les meilleures équipes SOC se tournent vers la détection et la réponse réseau

Les équipes des centres d'opérations de sécurité (SOC) sont confrontées à un défi fondamental : les outils de cybersécurité traditionnels ne parviennent pas à détecter les adversaires avancés qui sont devenus experts dans l'évasion des défenses basées sur les terminaux et des systèmes de détection basés sur les signatures. La réalité de ces "intrus invisibles" entraîne un besoin important d'une approche multicouche pour détecter les menaces.

## 🤖 Claude AI Exploité pour Opérer Plus de 100 Personnalités Politiques Fake dans une Campagne d'Influence Mondiale

La société d'intelligence artificielle (IA) Anthropic a révélé que des acteurs de menace inconnus ont exploité son chatbot Claude pour une opération "d'influence-as-a-service" afin d'interagir avec des comptes authentiques sur Facebook et X. L'activité sophistiquée, considérée comme financièrement motivée, aurait utilisé son outil d'IA pour orchestrer 100 personnes distinctes sur les deux plateformes de médias sociaux, créant un...

## 📉 Nouvelles Recherches Révèlent: 95% des Correctifs AppSec Ne Réduisent Pas le Risque

Depuis plus d'une décennie, les équipes de sécurité des applications sont confrontées à une ironie brutale : plus les outils de détection deviennent avancés, moins leurs résultats s'avèrent utiles. Alors que les alertes des outils d'analyse statique, des scanners et des bases de données CVE ont augmenté, la promesse d'une meilleure sécurité s'est éloignée. À sa place, une nouvelle réalité s'est installée, définie par la fatigue des alertes et les équipes dépassées. Selon OX...

## 🇷🇺 Les Malwares DarkWatchman et Sheriff Frappent la Russie et l'Ukraine avec Discrétion et Tactiques de Niveau National

Des entreprises russes ont été ciblées dans le cadre d'une campagne de phishing à grande échelle conçue pour diffuser un malware connu sous le nom de DarkWatchman. Les cibles des attaques comprennent des entités dans les secteurs des médias, du tourisme, de la finance et de l'assurance, de la fabrication, du commerce de détail, de l'énergie, des télécommunications, du transport et de la biotechnologie, a déclaré la société russe de cybersécurité F6. L'activité est considérée comme le travail d'un...

## ☁️ Commvault Confirme que des Hackers ont Exploité CVE-2025-3928 comme Zero-Day dans une Brèche Azure

La plateforme de sauvegarde de données d'entreprise Commvault a révélé qu'un acteur de menace étatique inconnu a violé son environnement Microsoft Azure en exploitant CVE-2025-3928, mais a souligné qu'il n'y a aucune preuve d'accès non autorisé aux données. "Cette activité a affecté un petit nombre de clients que nous avons en commun avec Microsoft, et nous travaillons avec ces clients pour leur fournir une assistance", a déclaré la société...

## 🔒 SonicWall Confirme l'Exploitation Active de Vulnérabilités Affectant Plusieurs Modèles d'Appareils

SonicWall a révélé que deux failles de sécurité désormais corrigées affectant ses appliances SMA100 Secure Mobile Access (SMA) ont été exploitées dans la nature. Les vulnérabilités en question sont énumérées ci-dessous :

*   🔒 **CVE:** [CVE-2023-44221](https://www.cve.org/CVERecord?id=CVE-2023-44221)
*   ⭐ **CVSS:** 7.2

Une neutralisation incorrecte d'éléments spéciaux dans l'interface de gestion SMA100 SSL-VPN permet à un attaquant distant authentifié avec privilège administratif de...

## 🧪 Des Chercheurs Démontrent Comment l'Injection d'Invite MCP Peut Être Utilisée à la Fois pour l'Attaque et la Défense

Alors que le domaine de l'intelligence artificielle (IA) continue d'évoluer à un rythme rapide, de nouvelles recherches ont montré comment les techniques qui rendent le Model Context Protocol (MCP) susceptible aux attaques par injection d'invite pourraient être utilisées pour développer des outils de sécurité ou identifier des outils malveillants, selon un nouveau rapport de Tenable. MCP, lancé par Anthropic en novembre 2024, est un cadre conçu pour connecter...

## 🧑‍💻 \[Webinaire Gratuit] Guide pour Sécuriser l'Ensemble de Votre Cycle de Vie de l'Identité Contre les Menaces Basées sur l'IA

Combien de lacunes se cachent dans votre système d'identité ? Il ne s'agit plus seulement des identifiants. Les attaquants d'aujourd'hui n'ont pas besoin de "pirater" : ils peuvent se frayer un chemin. Les deepfakes, les escroqueries par usurpation d'identité et l'ingénierie sociale basée sur l'IA les aident à contourner les défenses traditionnelles et à passer inaperçus. Une fois à l'intérieur, ils peuvent prendre le contrôle des comptes, se déplacer latéralement et causer des dommages à long terme, le tout sans...

## 🇨🇳 Des Hackers Chinois Abusent d'IPv6 SLAAC pour des Attaques AitM via l'Outil de Mouvement Latéral Spellbinder

Un groupe de menace persistante avancée (APT) aligné sur la Chine appelé TheWizards a été lié à un outil de mouvement latéral appelé Spellbinder qui peut faciliter les attaques d'intermédiaire (AitM). "Spellbinder permet des attaques d'intermédiaire (AitM), via l'usurpation de la configuration automatique d'adresse sans état IPv6 (SLAAC), pour se déplacer latéralement dans le réseau compromis, interceptant les paquets et...

## 💰 Les Prises de Contrôle de Comptes Clients: Le Problème de Plusieurs Milliards de Dollars Dont Vous N'Êtes Pas au Courant

Tout le monde a des histoires de cybersécurité impliquant des membres de sa famille. Voici une histoire relativement courante. La conversation se déroule généralement comme suit : "La chose la plus étrange est arrivée à mon compte de streaming. J'ai été bloqué de mon compte, j'ai donc dû changer mon mot de passe. Quand je me suis reconnecté, toutes mes émissions avaient disparu. Tout était en espagnol et il y avait toutes ces émissions espagnoles que je n'ai jamais vues...

## 🕷️ Nebulous Mantis Cible des Entités Liées à l'OTAN avec des Attaques de Malware Multi-Étapes

Les chercheurs en cybersécurité ont mis en lumière un groupe d'espionnage cybernétique russophone appelé Nebulous Mantis qui...

## 🛡️ Vulnérabilité dans Synacor Zimbra Collaboration (28 janvier 2025)

Une vulnérabilité a été découverte dans Synacor Zimbra Collaboration. Elle permet à un attaquant de provoquer une injection de code indirecte à distance (XSS).

## 🍎 Multiples Vulnérabilités dans les produits Apple (01 avril 2025)

De multiples vulnérabilités ont été découvertes dans les produits Apple. Certaines d'entre elles permettent à un attaquant de provoquer une exécution de code arbitraire, une élévation de privilèges et une atteinte à la confidentialité des données. Apple indique que les vulnérabilités...

## 🏢 Multiples vulnérabilités dans les produits SAP (08 avril 2025)

De multiples vulnérabilités ont été découvertes dans les produits SAP. Certaines d'entre elles permettent à un attaquant de provoquer une exécution de code arbitraire à distance, une atteinte à la confidentialité des données et une atteinte à l'intégrité des données.

## 🚇 Transports urbains - État de la menace informatique (17 avril 2025)

La menace à l’encontre des entités des transports urbains cible des entreprises de toutes les tailles dans le monde entier qui opèrent différents modes de transport. La convergence de technologies industrielles et bureautique, l’interconnexion de réseaux informatiques de grande taille composés...

## 🐧 Multiples vulnérabilités dans le noyau Linux de Red Hat (18 avril 2025)

De multiples vulnérabilités ont été découvertes dans le noyau Linux de Red Hat. Elles permettent à un attaquant de provoquer une atteinte à la confidentialité des données, un contournement de la politique de sécurité et un déni de service.

## 🛡️ Multiples vulnérabilités dans Tenable Nessus (18 avril 2025)

De multiples vulnérabilités ont été découvertes dans Tenable Nessus. Certaines d'entre elles permettent à un attaquant de provoquer une élévation de privilèges, un déni de service à distance et une atteinte à la confidentialité des données.

## 🐧 Multiples vulnérabilités dans le noyau Linux de Debian (18 avril 2025)

De multiples vulnérabilités ont été découvertes dans le noyau Linux de Debian. Elles permettent à un attaquant de provoquer une élévation de privilèges, une atteinte à la confidentialité des données et un déni de service.

## 🌐 Multiples vulnérabilités dans Microsoft Edge (18 avril 2025)

De multiples vulnérabilités ont été découvertes dans Microsoft Edge. Elles permettent à un attaquant de provoquer un problème de sécurité non spécifié par l'éditeur.

## ⚙️ Vulnérabilité dans les produits Moxa (18 avril 2025)

Une vulnérabilité a été découverte dans les produits Moxa. Elle permet à un attaquant de provoquer une exécution de code arbitraire à distance et une élévation de privilèges.

## 🏢 Vulnérabilité dans Liferay (18 avril 2025)

Une vulnérabilité a été découverte dans Liferay. Elle permet à un attaquant de provoquer une injection de code indirecte à distance (XSS).

## 🏢 Multiples vulnérabilités dans les produits IBM (18 avril 2025)

De multiples vulnérabilités ont été découvertes dans les produits IBM. Certaines d'entre elles permettent à un attaquant de provoquer une exécution de code arbitraire à distance, un déni de service à distance et une atteinte à la confidentialité des données.

## 🐧 Multiples vulnérabilités dans le noyau Linux de SUSE (18 avril 2025)

De multiples vulnérabilités ont été découvertes dans le noyau Linux de SUSE. Certaines d'entre elles permettent à un attaquant de provoquer une exécution de code arbitraire à distance, une élévation de privilèges et une atteinte à la confidentialité des données.

## 🐧 Multiples vulnérabilités dans le noyau Linux d'Ubuntu (18 avril 2025)

De multiples vulnérabilités ont été découvertes dans le noyau Linux d'Ubuntu. Certaines d'entre elles permettent à un attaquant de provoquer une élévation de privilèges, une atteinte à la confidentialité des données et un déni de service.

## 📰 Bulletin d'actualité CERTFR-2025-ACT-016 (22 avril 2025)

Ce bulletin d'actualité du CERT-FR revient sur les vulnérabilités significatives de la semaine passée pour souligner leurs criticités. Il ne remplace pas l'analyse de l'ensemble des avis et alertes publiés par le CERT-FR dans le cadre d'une analyse de risques pour prioriser l'application des...

## 🛡️ Vulnérabilité dans PostgreSQL PgBouncer (22 avril 2025)

Une vulnérabilité a été découverte dans PostgreSQL PgBouncer. Elle permet à un attaquant de provoquer un contournement de la politique de sécurité.

## 🚗 Multiples vulnérabilités dans Traefik (22 avril 2025)

De multiples vulnérabilités ont été découvertes dans Traefik. Elles permettent à un attaquant de provoquer un contournement de la politique de sécurité et un problème de sécurité non spécifié par l'éditeur.

## 🛡️ Vulnérabilité dans Tenable Security Center (22 avril 2025)

Une vulnérabilité a été découverte dans Tenable Security Center. Elle permet à un attaquant de provoquer une injection SQL (SQLi).

## 📚 Multiples vulnérabilités dans Moodle (22 avril 2025)

De multiples vulnérabilités ont été découvertes dans Moodle. Certaines d'entre elles...

## ♾️ CVE-2025-3857 - Condition de boucle infinie dans Amazon.IonDotnet

Une condition de boucle infinie a été identifiée dans Amazon.IonDotnet lors de la lecture de données binaires Ion avec la classe RawBinaryReader. Une donnée Ion malformée ou tronquée peut déclencher cette boucle, entraînant potentiellement un déni de service. La version corrigée est la 1.3.1.

*   🐛 **CVE:** [CVE-2025-3857](https://www.cve.org/CVERecord?id=CVE-2025-3857)

## 🛠️ Problème avec AWS SAM CLI (CVE-2025-3047, CVE-2025-3048)

Des vulnérabilités ont été découvertes dans AWS SAM CLI. CVE-2025-3047 permet à un utilisateur d'accéder à des fichiers privilégiés sur l'hôte via des liens symboliques lors de l'utilisation de Docker. CVE-2025-3048 copie le contenu de ces liens symboliques dans le cache local, donnant accès à des données qui ne devraient pas l'être. Les versions corrigées sont 1.133.0 et 1.134.0 respectivement.

*   🐛 **CVE:** [CVE-2025-3047](https://www.cve.org/CVERecord?id=CVE-2025-3047)
*   🐛 **CVE:** [CVE-2025-3048](https://www.cve.org/CVERecord?id=CVE-2025-3048)

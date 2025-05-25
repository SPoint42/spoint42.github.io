---
layout: post
title: "STRIDE : Les 6 Types de Menaces que Chaque Développeur Devrait Connaître"
author: Sébastien Gioria
date: 2025-05-25 10:00:00 +0200
categories:
  - CyberSec
  - Threat-Modeling
  - STRIDE
  - GenAI
  - Fiche-Pratique
---

Après avoir exploré la méthodologie complète de [PASTA]({{home}}/2025/05/24/secu-ia-pasta) dans notre article précédent,
il est temps 
de se pencher sur un
outil plus spécifique mais tout aussi puissant pour l'identification des menaces : **STRIDE**. Développé par Microsoft,
[STRIDE]({{home}}/2025/04/26/STRIDE/) est une taxonomie simple et mémorable qui vous aide à ne rien oublier lorsque vous 
réfléchissez aux types d'attaques qu'un système peut subir.

STRIDE n'est pas une méthodologie en soi, mais plutôt une **liste de contrôle systématique** des catégories de menaces.
C'est un excellent point de départ pour le "brainstorming" des menaces, notamment lors des phases d'analyse des cas d'
utilisation et des menaces (étapes 3 et 4) d'une démarche PASTA.

Chaque lettre de STRIDE représente une catégorie distincte de menaces :

### S - Spoofing (Usurpation d'identité)
* **Qu'est-ce que c'est ?** Un attaquant se fait passer pour une entité légitime (utilisateur, système, application,
  donnée) afin d'obtenir un accès ou des informations non autorisées.
* **Exemple courant :** Un e-mail de phishing où l'expéditeur se fait passer pour votre banque.
* **Exemple IA Générative :** Un attaquant se fait passer pour une source de données fiable pour injecter des données
  d'entraînement empoisonnées dans votre modèle. Un utilisateur malveillant se fait passer pour un utilisateur autorisé
  pour accéder à l'API de votre modèle et générer du contenu illicite.

### T - Tampering (Altération)
* **Qu'est-ce que c'est ?** Un attaquant modifie des données en transit ou au repos, ou altère le fonctionnement normal
  d'un processus ou d'un système.
* **Exemple courant :** Modification d'une transaction bancaire en ligne.
* **Exemple IA Générative :** Une "prompt injection" où l'attaquant manipule l'entrée du modèle pour le faire dévier de
  son comportement attendu. L'altération des poids d'un modèle d'IA pour modifier ses sorties.

### R - Repudiation (Répudiation)
* **Qu'est-ce que c'est ?** Un attaquant (ou un utilisateur malveillant) nie avoir effectué une action, sans preuve
  irréfutable pour le contredire.
* **Exemple courant :** Une personne effectue une transaction financière mais nie l'avoir faite.
* **Exemple IA Générative :** Un utilisateur génère un contenu illégal ou offensant avec votre IA générative et nie
  l'avoir produit, faute de journaux d'audit ou de preuves numériques. Un modèle d'IA qui ne peut pas prouver qu'il a
  généré une sortie spécifique.

### I - Information Disclosure (Divulgation d'informations)
* **Qu'est-ce que c'est ?** Un attaquant accède à des informations sensibles qui ne devraient pas lui être accessibles.
  Cela peut inclure des données personnelles, des secrets commerciaux, ou des informations système.
* **Exemple courant :** Une base de données non sécurisée exposée sur Internet.
* **Exemple IA Générative :** Une attaque par "model inversion" où un attaquant parvient à reconstruire des données
  sensibles du jeu d'entraînement à partir des sorties du modèle. La divulgation involontaire de PII dans les réponses
  générées par un chatbot d'IA.

### D - Denial of Service (Déni de service)
* **Qu'est-ce que c'est ?** Un attaquant empêche les utilisateurs légitimes d'accéder à un service ou à une ressource en
  surchargeant le système ou en le rendant inutilisable.
* **Exemple courant :** Une attaque DDoS qui rend un site web inaccessible.
* **Exemple IA Générative :** Une attaque qui submerge l'API de votre modèle d'IA générative avec des requêtes, rendant
  l'application incapable de répondre aux requêtes légitimes, ou épuisant vos crédits cloud.

### E - Elevation of Privilege (Élévation de privilèges)
* **Qu'est-ce que c'est ?** Un attaquant parvient à obtenir des droits d'accès plus élevés que ceux qui lui ont été
  initialement accordés, lui permettant d'effectuer des actions qu'il ne devrait pas pouvoir faire.
* **Exemple courant :** Un utilisateur normal qui parvient à obtenir les droits d'administrateur système.
* **Exemple IA Générative :** Une vulnérabilité dans le système de gestion d'accès de votre plateforme d'IA qui permet à
  un utilisateur non privilégié d'accéder aux paramètres d'entraînement du modèle ou de déployer de nouvelles versions.

![Diagramme Modèle de Menaces STRIDE]({{home}}/assets/img/stride.png)


**STRIDE : Votre Boussole dans l'Univers des Menaces**

La force de STRIDE réside dans sa simplicité et sa couverture. En passant en revue chaque catégorie pour chaque
composant ou flux de données de votre application, vous vous assurez de ne pas laisser de menaces majeures de côté.
C'est un excellent outil de "brainstorming" pour compléter l'approche plus structurée de PASTA.

Dans le prochain article, nous verrons comment ces deux méthodologies, **PASTA** et **STRIDE**, peuvent être combinées
pour former une stratégie de sécurité inébranlable spécifiquement adaptée aux défis uniques de l'IA générative. La
synergie entre ces deux approches est la clé pour bâtir des applications d'IA générative robustes et dignes de
confiance.
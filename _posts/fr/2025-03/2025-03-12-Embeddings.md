---
layout: post
date: 2025-03-12
title: "Les embedding dans le RAG quesako ?"
categories:
  - veille
  - CyberSec
  - Top10
  - OWASP
  - LLM
---


Dans le contexte de la **Génération Augmentée de Récupération (RAG)**, les _embeddings_ sont des représentations vectorielles
de mots ou de groupes de mots. Ces vecteurs encapsulent des informations sur les contextes dans lesquels les mots
apparaissent, permettant ainsi aux modèles de langage de calculer des similarités sémantiques entre eux. Les _embeddings_
sont essentiels pour la RAG car ils permettent de rechercher et de comparer efficacement les informations pertinentes
dans une base de données vectorielle, améliorant ainsi la précision des réponses générées par les modèles de langage.

Voici comment les embeddings fonctionnent dans un système RAG :

- **Transformation en Vecteurs** : Les mots ou les phrases sont transformés en vecteurs numériques. Cette transformation
conserve la proximité sémantique, c'est-à-dire que deux concepts proches sémantiquement sont proches numériquement.

- **Recherche dans une Base de Données Vectorielle** : Lorsqu'une question est posée, son embedding est calculé et comparé aux
embeddings stockés dans la base de données pour identifier les chunks de texte les plus pertinents.

- **Génération de Réponses** : Les chunks pertinents sont ensuite combinés avec la question pour créer un prompt qui est
transmis à un modèle de langage pour générer une réponse.

Les embeddings sont donc cruciaux pour permettre aux systèmes RAG de fournir des réponses précises et contextualisées en
intégrant des sources d'information externes.
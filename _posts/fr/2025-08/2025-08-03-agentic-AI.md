---
layout: post
date: 2025-08-03 10:00:00 +0200
title: "Introduction à l'Agentic AI : Comprendre les Fondamentaux"
categories:
  - CyberSec
  - OWASP
  - GENAI 
  - Fiche-Pratique
---

Dans cette suite de posts, nous allons explorer les concepts fondamentaux de l'**Agentic AI** et les risques 
associés, en mettant l'accent sur les différences entre les modèles de langage (LLM) et les agents IA. 
Nous verrons également comment les agents IA introduisent de nouveaux défis en matière de sécurité.

Rappelons que l'**Agentic AI** est un terme qui désigne les systèmes d'intelligence artificielle capables d'agir
autonomement pour atteindre des objectifs spécifiques, en utilisant des modèles de langage avancés (LLM) comme base.

### LLM vs Agentic AI
Un **LLM** (Large Language Model) est un modèle de langage entraîné sur de vastes ensembles de données textuelles pour
générer du texte, répondre à des questions ou effectuer des tâches de traitement du langage naturel. Il est
essentiellement un outil de génération de texte, sans capacité d'action autonome ou de prise de décision.

### Qu'est-ce qu'un Agent IA ?

Un **Agent IA** est un système qui va au-delà de la simple génération de texte d'un grand modèle de langage (LLM). Il
est conçu pour percevoir son environnement, planifier des actions, utiliser des outils et travailler de manière autonome
pour atteindre un objectif spécifique.

Pour mieux comprendre, imaginez la différence entre une voiture et un conducteur.

* Le LLM est le **moteur de la voiture** : il fournit la puissance et la logique pour avancer.
* L'Agent IA est le **conducteur** : il utilise ce moteur, perçoit la route, prend des décisions, utilise les
  commandes (volant, pédales) et navigue jusqu'à une destination.

Voici un schéma simple qui illustre les composants et le flux de travail d'un Agent IA :

![AgentIA.png]({{home}}/assets/img/AgentAI.png)
-----

### Les Risques Spécifiques aux Agents IA

Les risques du top 10 de l'OWASP s'appliquent toujours, mais l'autonomie et l'utilisation d'outils des Agents IA créent
de nouvelles menaces critiques.

#### 1\. L'Injection de Prompt Persistante

Ce n'est plus seulement une injection ponctuelle, c'est une attaque qui vise à **manipuler l'état ou la "mémoire" de
l'agent**. L'agent est programmé secrètement pour accomplir une tâche malveillante de manière répétée et autonome.

* **Exemple :** Un attaquant insère une instruction cachée dans un document demandant à l'agent d'extraire des
  informations sensibles à chaque fois qu'il traite un fichier. L'agent obéit à cette instruction de manière
  persistante, sans que les utilisateurs ne s'en rendent compte.

#### 2\. Le Détournement et l'Abus des Outils

Un agent peut être forcé, par une injection de prompt ou une entrée malveillante, à utiliser ses outils de manière non
intentionnelle. L'agent, en croyant agir pour le bien, peut causer des dégâts majeurs.

* **Exemple :** Un agent est chargé d'interagir avec une base de données. Un attaquant le manipule pour qu'il exécute
  des requêtes de suppression au lieu de simples requêtes de lecture, causant une perte de données.

#### 3\. L'Action Malveillante Autonome

L'agent peut prendre une décision risquée, non pas à cause d'une injection, mais à cause d'une 
**erreur de raisonnement** ou d'une mauvaise compréhension d'une situation. Son autonomie peut transformer une simple erreur logique en une
action dommageable.

* **Exemple :** Un agent chargé d'optimiser le stockage d'un serveur interprète une commande comme un ordre de supprimer
  les fichiers qu'il considère "redondants", entraînant la perte de données importantes.

#### 4\. La Fuite de Données via les Outils

Un agent, en raison de son accès aux outils et à l'environnement, est un vecteur idéal pour l'exfiltration de données.
Un attaquant peut manipuler l'agent pour qu'il transmette des informations confidentielles à un service externe.

* **Exemple :** L'agent, après avoir lu un document contenant des PII, est incité à utiliser son outil d'envoi d'e-mails
  pour envoyer ces informations à un destinataire externe contrôlé par l'attaquant.

En résumé, les Agents IA introduisent la notion de **contrôle des actions**, en plus du contrôle des entrées. C'est ce
que nous explorerons plus en détail dans les prochains posts.


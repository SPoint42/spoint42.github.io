---
layout: post
date: 2025-08-03 16:00:00 +0200
title: "🧑‍🍳 Agentic AI : Sécurisation des Agents IA quelle est la recette ?"
categories:
  - Fiche-Pratique
  - CyberSec
  - OWASP
  - LLM
  - GenAI 
  - AgenticAI
---


Voici donc la recette pour sécuriser les Agents IA, en se basant sur les principes de l'OWASP et les meilleures pratiques
de sécurité. Cette approche vise à identifier les risques spécifiques aux Agents IA et à proposer des solutions adaptées.

![howto.png]({{home}}/assets/img/2025-08/howto.png)

#### **1. Les 5 Risques Principaux**

Pour commencer notre exploration, nous allons nous concentrer sur les risques spécifiques aux Agents IA, qui diffèrent de ceux
des LLM classiques. Ces risques sont souvent liés à l'autonomie et à la capacité d'action des agents, ce qui les rend
particulièrement critiques dans un contexte de sécurité.
 Meme si les LLM classiques peuvent être vulnérables à des attaques, les Agents IA introduisent de nouveaux défis en raison de
leur capacité à agir de manière autonome et à interagir avec des systèmes externes.

Voici les 5 risques principaux que nous allons aborder :
* **[Injection de Prompt Persistante]({{home}}/2025/08/07/agenticIa-risks/)** : Manipulation durable de l'agent.
* **[Détournement d'Outil]({{home}}/2025/08/11/agenticIa-risks2)** : Utilisation abusive des outils de l'agent.
* **[Fuite de Données]({{home}}/2025/08/14/agenticIa-risk3)** : Exfiltration de données via les actions de l'agent.
* **Actions Malveillantes Autonomes** : Décisions dangereuses prises par l'agent sans intervention humaine.
* **Vulnérabilité d'Exécution de Code** : Code généré ou exécuté par l'agent qui contient des failles.

---

#### **2. Solutions et Stratégies**

Pour chacun des risques identifiés, nous allons proposer des solutions concrètes et des stratégies de mitigation. Ces
solutions sont conçues pour être intégrées dans votre méthodologie de développement agile et DevSecOps, afin de garantir
que la sécurité est une priorité dès le début du cycle de vie du développement logiciel (SDLC).

* **Sécuriser le "Cerveau"** : Mettre en place des gardes-fous (guardrails).
* **Sécuriser les Outils** : Appliquer le principe du **moindre privilège** et le "Human-in-the-Loop".
* **Protéger l'Environnement** : Utiliser le **sandboxing** et valider les données.
* **Surveillance** : Mettre en place une journalisation et une détection d'anomalies.

---

#### **3. Intégration dans le Cycle DevSecOps**

Nous allons voir comment intégrer ces solutions dans votre méthodologie de développement agile et DevSecOps existante,
sans la complexifier. L'objectif est de garantir que la sécurité est une priorité dès le début du cycle de vie du
développement logiciel (SDLC), tout en maintenant la flexibilité et l'efficacité des processus agiles.

* **Conception** : Définir les limites de l'agent.
* **CI/CD** : Automatiser les tests de sécurité (SAST, SCA).
* **Production** : Mettre en place une surveillance continue et une gestion sécurisée des secrets.

---

#### **4. Référentiels de l'OWASP associés**

Pour finaliser notre approche, nous allons établir un lien entre les risques identifiés et les référentiels de sécurité
de l'OWASP, notamment le **OWASP Top 10 for LLM (OWASP LLM AI)**. Cela nous permettra de valider notre approche et de
s'assurer que nous couvrons les risques les plus critiques associés aux Agents IA.

Pour chaque risque, nous allons faire référence aux contrôles et aux recommandations de l'OWASP, afin de garantir que
nous suivons les meilleures pratiques de sécurité reconnues dans l'industrie.



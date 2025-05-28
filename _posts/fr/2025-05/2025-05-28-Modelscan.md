---
layout: post
date: 2025-05-28
title: " 🛠️Contrer les attaques par sérialisation de modèles avec Modelscan"
categories:
  - CyberSec
  - Top10
  - OWASP
  - LLM
  - Tools
---

Protect AI a lancé Modelscan, un projet open-source visant à sécuriser les modèles d'intelligence artificielle. Cet
outil novateur est le premier de son genre à prendre en charge plusieurs formats de modèles, notamment H5, Pickle et
SavedModel, offrant une protection étendue à travers des frameworks comme PyTorch, TensorFlow, Keras, Sklearn et
XGBoost.

L'objectif principal de Modelscan est de contrer les attaques par sérialisation de modèles, un risque croissant où du
code malveillant est intégré directement dans le modèle lors de sa sauvegarde et distribution. En scannant le contenu
des fichiers octet par octet, Modelscan identifie les signatures de code potentiellement dangereuses.

La force de Modelscan réside dans sa capacité à classer les codes non sûrs en catégories de gravité : CRITICAL, HIGH,
MEDIUM ou LOW, permettant aux développeurs et aux équipes de sécurité de prioriser et d'adresser les menaces. L'outil
fournit également des codes de statut de sortie CLI clairs, facilitant l'intégration dans les pipelines CI/CD et l'
automatisation des processus de sécurité des modèles.

En somme, Modelscan est un ajout crucial à l'arsenal de cybersécurité des systèmes d'IA. Il assure que les modèles
utilisés en production sont exempts de vulnérabilités cachées, renforçant ainsi la confiance et la sécurité dans
l'écosystème de l'intelligence artificielle. 

C'est un bon outil pour les développeurs et les équipes de sécurité  tout comme le OWASP Top10 [Machine Learning 
Security]({{home}}{% post_url 2025-03-13-OWASP-MLTOP10 %}) et [PromptFoo]({{home}}{% post_url 2025-03-19-prompfoo-1 
%}).

Pour plus de détails, vous pouvez consulter la page GitHub du projet :

[Modelscan GitHub Repository](https://github.com/protectai/modelscan)
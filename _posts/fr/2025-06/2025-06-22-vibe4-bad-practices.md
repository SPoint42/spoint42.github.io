---
layout: post
date: 2025-06-22 15:00:00 +0100
title: "🤖Mauvaises Pratiques du Vibe Coding et Comment les Éviter"
categories:
 - CyberSec
 - LLM
 - SecureCoding

---

Le "vibe coding" peut devenir un cauchemar de sécurité si certaines mauvaises pratiques ne sont pas évitées.

# Exemples de Bad Practices :

* **Confiance aveugle dans l'IA :** Ne pas réviser ou comprendre le code généré par l'IA. L'IA peut introduire des bugs,
  des inefficacités ou des vulnérabilités sans intention malveillante. C'est le piège du "code first, refine later" sans
  le "refine".
* **Absence de validation des entrées :** Demander à l'IA de générer un formulaire sans spécifier la validation des
  entrées, ouvrant la porte aux injections SQL, XSS, etc.
* **Hardcoding des secrets :** L'IA peut, si le prompt n'est pas explicite, inclure des identifiants, des clés API ou
  d'autres informations sensibles directement dans le code source.
* **Utilisation de dépendances non sécurisées :** L'IA peut générer du code qui utilise des bibliothèques obsolètes ou
  vulnérables sans en informer le développeur.
* **Manque de documentation :** Le code généré par l'IA peut être moins lisible ou moins bien documenté, rendant sa
  maintenance et son audit de sécurité difficiles.
* **Négliger les tests de sécurité :** Se fier uniquement à l'IA pour générer du code "correct" sans effectuer de tests
  unitaires, d'intégration ou de sécurité.

# Comment les éviter :

* **Révision humaine systématique :** Toujours relire et comprendre le code généré par l'IA. C'est le développeur qui
  reste responsable du code en production.
* **Prompts explicites et sécurisés :** Spécifier clairement les exigences de sécurité dans vos prompts ("assurer la
  validation de toutes les entrées utilisateur", "utiliser des requêtes préparées", "gérer les secrets de manière
  sécurisée").
* **Outillage de sécurité automatisé :** Utiliser des outils SAST, SCA, DAST intégrés au pipeline CI/CD pour analyser le
  code généré en continu.
* **Gestion des secrets :** Toujours stocker les secrets dans des gestionnaires de secrets dédiés (Vault, AWS Secrets
  Manager, Azure Key Vault) et ne jamais les intégrer directement dans le code, même si l'IA le suggère.
* **Mise à jour des dépendances :** Mettre en place un processus automatisé pour scanner et mettre à jour les
  dépendances afin d'éviter les vulnérabilités connues.
* **Formation et sensibilisation :** Former les développeurs aux risques spécifiques du "vibe coding" et aux bonnes
  pratiques de sécurité avec l'IA.


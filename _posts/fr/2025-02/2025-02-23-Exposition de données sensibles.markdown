---
layout: post
title:  "Sécurité de la GEN AI && OWASP ! 💥Exposition de Données Sensibles💥 "
date:   2025-02-23
categories: veille security owasp genAI 
lang : french
---

L'exposition de données sensibles se produit lorsque des informations confidentielles, telles que des identifiants personnels, des
informations financières, des dossiers médicaux, ou des secrets commerciaux, deviennent accessibles à des parties non autorisées.


### Scénario

Une application de santé utilise un modèle d'intelligence artificielle générative (GEN AI) pour analyser des dossiers médicaux afin 
d'identifier des tendances et de fournir des recommandations de traitement. Cependant, les données des patients ne sont pas correctement 
anonymisées avant d'être traitées par le modèle GEN AI.

### Conséquence

Les informations personnelles sensibles des patients, telles que les noms, les numéros de sécurité sociale, et les historiques médicaux, 
sont accidentellement exposées. Cela entraîne une violation de la confidentialité des patients et une non-conformité avec les réglementations 
sur la protection des données comme le RGPD ou HIPAA.

### Meilleures Pratiques de Protection

- **Anonymisation des Données :** Assurez-vous que toutes les données sensibles sont anonymisées avant d'être traitées par le modèle GEN AI. 
- Utilisez des techniques telles que la pseudonymisation et le hachage pour protéger les informations personnelles.
  - [OWASP Cheat Sheet: Data Anonymization](https://cheatsheetseries.owasp.org/cheatsheets/Data_Anonymization_Cheat_Sheet.html)

- **Contrôles d'Accès :** Mettez en place des contrôles d'accès stricts pour limiter l'accès aux données sensibles uniquement aux personnes autorisées. Utilisez des mécanismes d'authentification et d'autorisation robustes.
  - [OWASP Cheat Sheet: Authentication](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

- **Surveillance et Audit :** Implémentez des mécanismes de surveillance pour détecter et répondre rapidement aux accès non autorisés ou aux 
- comportements suspects. Effectuez régulièrement des audits de sécurité pour identifier les vulnérabilités potentielles.
  - [OWASP Cheat Sheet: Logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)

- **Chiffrement :** Chiffrez les données sensibles à la fois en transit et au repos pour empêcher les accès non autorisés, même en cas de fuite 
- de données.
  - [OWASP Cheat Sheet: Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
  - [OWASP Cheat Sheet : Transport Layer Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)

### Exemple Concret

**CVE-2024-5982** : Une vulnérabilité de traversée de répertoire dans la fonction de téléchargement utilisateur de ChuanhuChatGPT a permis 
l'exécution arbitraire de code, la création de répertoires, et l'exposition de données sensibles. Cette vulnérabilité illustre comment des 
failles dans les systèmes utilisant l'IA générative peuvent être exploitées pour accéder à des informations sensibles.

🌐 **[En savoir plus sur la CVE-2024-5982](https://thehackernews.com/2024/10/researchers-uncover-vulnerabilities-in.html)**

---
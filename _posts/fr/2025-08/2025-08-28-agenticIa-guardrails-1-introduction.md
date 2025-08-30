---
layout: post
date: 2025-08-28 8:00:00 +0200
title: "🧠 Agentic AI : Guardrails - Introduction et Concepts Fondamentaux (1/4) 🛡️ "
categories:
  - Fiche-Pratique
  - CyberSec
  - OWASP
  - LLM
  - GenAI
  - AgenticAI
---

<div style="background: linear-gradient(to right, #6f42c1, #5a32a3); color: white; padding: 15px; border-radius: 8px; margin: 20px 0;">
    <div style="display: flex; align-items: center; gap: 15px;">
        <div style="font-size: 2em;">📚</div>
        <div>
            <h3 style="margin: 0; font-size: 1.1em;">Article un peu plus long que d'habitude</h3>
            <p style="margin: 5px 0 0 0; font-size: 0.9em;">
                ⏱️ Temps de lecture estimé : 15-20 minutes (enfin pour bien le comprendre 😊)<br>
            </p>
        </div>
    </div>
</div>


# 🤔**Qu'est-ce que les Guardrails ?** 



Les guardrails sont des **mécanismes de contrôle automatisés** qui interceptent et valident les interactions avec les LLM. Ils agissent comme des filtres intelligents qui :

- **Analysent les entrées** (prompts utilisateur) avant qu'elles n'atteignent le modèle
- **Vérifient les sorties** (réponses du modèle) avant qu'elles ne soient transmises à l'utilisateur
- **Appliquent des règles de sécurité** définies selon vos politiques métier
- **Détectent et mitigent les risques** en temps réel

## **Architecture Conceptuelle des Guardrails**

![GuardRails Architecture]({{home}}/assets/img/2025-08/guardrails-archiHL.png)

### **Flux de Traitement Sécurisé**

1. **Phase d'Entrée** : Validation et nettoyage des inputs utilisateur
2. **Phase de Traitement** : Interaction contrôlée avec le LLM
3. **Phase de Sortie** : Vérification et filtrage des réponses
4. **Phase de Logging** : Enregistrement des incidents de sécurité

---

# **Pourquoi les Guardrails sont-ils Essentiels ?** 

<div style="background: linear-gradient(to right, #ff4d4d, #d9534f); color: white; padding: 15px; border-radius: 8px; margin: 20px 0; text-align: center;">
    <h2 style="margin: 0; font-size: 1.4em;">🚨  Quels sont les Risques sans Guardrails ? 🚨</h2>
</div>


<div style="display: flex; gap: 20px; margin: 20px 0;">
    <div style="flex: 1;">
        <h3>🎯 Injection de Prompt</h3>
        <p style="font-size: 0.9em; padding: 8px 12px; background-color: #fff3cd; border-left: 4px solid #ffc107; border-radius: 4px; margin: 10px 0;">🚨  Les utilisateurs malveillants peuvent manipuler les instructions du modèle de plusieurs façons</p>
        <ul style="list-style: none; padding-left: 0;">
            <li>🔓 Contournement des restrictions</li>
            <li>🔑 Extraction d'informations</li>
            <li>🤖 Modification du comportement</li>
        </ul>
        <p style="font-size: 0.9em;">👉 <a href="{{home}}/2025/02/26/prompt/">Article : OWASP Top 10 LLM - Injection</a></p>
    </div>

    <div style="flex: 1;">
        <h3>🔐 Fuites de Données</h3>
        <p style="font-size: 0.9em; padding: 8px 12px; background-color: #fff3cd; border-left: 4px solid #ffc107; border-radius: 4px; margin: 10px 0;">🚨Sans protection, les LLM peuvent révéler </p>
        <ul style="list-style: none; padding-left: 0;">
            <li>👤 Données personnelles (PII)</li>
            <li>🏢 Secrets d'entreprise</li>
            <li>⚙️ Config système</li>
            <li>©️ Contenu protégé</li>
        </ul>
    </div>

    <div style="flex: 1;">
        <h3>⚠️ Contenu Inapproprié</h3>
        <p style="font-size: 0.9em; padding: 8px 12px; background-color: #fff3cd; border-left: 4px solid #ffc107; border-radius: 4px; margin: 10px 0;">🚨Génération non contrôlée de </p>
        <ul style="list-style: none; padding-left: 0;">
            <li>🚫 Contenu toxique</li>
            <li>❌ Désinformation</li>
            <li>⚖️ Biais discriminatoires</li>
            <li>⛔ Contenu illégal</li>
        </ul>
    </div>
</div>

<div style="background: linear-gradient(to right, #4CAF50, #45a049); color: white; padding: 15px; border-radius: 8px; margin: 20px 0; text-align: center;">
    <h2 style="margin: 0; font-size: 1.4em;">💫 Les Bénéfices des Guardrails 💫</h2>
</div>

✅ **Sécurité** : Prévention des attaques et fuites  
✅ **Confiance Utilisateur** : Expérience sûre et prévisible  
✅ **Fiabilité** : Réponses cohérentes et factuelles  
✅ **Conformité Réglementaire** : Respect RGPD, sectoriels  


---

# **Quelques Types de Guardrails par Fonction** 

<!-- Input Guards Section -->
<div style="background: linear-gradient(to right, #ff6b6b, #ee5253); color: white; padding: 15px; border-radius: 8px; margin: 20px 0; text-align: center;">
    <h2 style="margin: 0; font-size: 1.4em;">🛡️ Guardrails d'Entrée (Input Guards)</h2>
</div>

<div style="display: flex; gap: 20px; margin: 20px 0;">
    <div style="flex: 1; background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
        <h3 style="color: #ff6b6b;">🔍 Validation Préventive</h3>
        <ul style="list-style: none; padding-left: 0;">
            <li>🚫 <strong>Détection de Jailbreaking</strong> : Identification des tentatives de contournement</li>
            <li>🔒 <strong>Filtrage PII</strong> : Protection des données personnelles</li>
            <li>📋 <strong>Contrôle Thématique</strong> : Restriction aux sujets autorisés</li>
            <li>✅ <strong>Validation Format</strong> : Vérification de la structure des requêtes</li>
        </ul>
    </div>
    
    <div style="flex: 1; background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
        <h3 style="color: #ff6b6b;">⚠️ Exemples de Triggers Détectés</h3>
        <div style="background: #fff3cd; padding: 15px; border-radius: 4px; font-family: monospace;">
            ❌ "Ignore all previous instructions..."<br>
            ❌ "You are now in developer mode..."<br>
            ❌ "Pretend you are not an AI assistant..."<br>
            ❌ "Override your safety guidelines..."
        </div>
    </div>
</div>

<!-- Output Guards Section -->
<div style="background: linear-gradient(to right, #20bf6b, #18a65d); color: white; padding: 15px; border-radius: 8px; margin: 20px 0; text-align: center;">
    <h2 style="margin: 0; font-size: 1.4em;">🔍 Guardrails de Sortie (Output Guards)</h2>
</div>

<div style="display: flex; gap: 20px; margin: 20px 0;">
    <div style="flex: 1; background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
        <h3 style="color: #20bf6b;">🔄 Validation Post-Génération</h3>
        <ul style="list-style: none; padding-left: 0;">
            <li>📊 <strong>Contrôle Factualité</strong> : Vérification des sources et cohérence</li>
            <li>🚫 <strong>Filtrage Contenu</strong> : Suppression d'éléments inappropriés</li>
            <li>🔐 <strong>Anonymisation</strong> : Protection automatique des données sensibles</li>
            <li>✨ <strong>Validation Qualité</strong> : Contrôle de la pertinence et du style</li>
        </ul>
    </div>
    
    <div style="flex: 1; background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
        <h3 style="color: #20bf6b;">✅ Critères de Qualité</h3>
        <ul style="list-style: none; padding-left: 0;">
            <li>📏 Longueur appropriée des réponses</li>
            <li>📖 Niveau de lecture accessible</li>
            <li>🎯 Cohérence avec la marque</li>
            <li>⚖️ Absence de biais détectables</li>
        </ul>
    </div>
</div>

---

# **3 types d'Architectures de Déploiement potentiel** 🏗️

<div style="background: linear-gradient(to right, #6f42c1, #5a32a3); color: white; padding: 15px; border-radius: 8px; margin: 20px 0; text-align: center;">
    <h2 style="margin: 0; font-size: 1.4em;">🏗️ Architecture Centralisée</h2>
    <p style="margin: 10px 0 0 0; font-size: 0.9em; opacity: 0.9;">Une approche unifiée pour la gestion des guardrails</p>
</div>

<div style="background: #f8f9fa; padding: 20px; border-radius: 8px; margin: 20px 0;">
    <div style="display: flex; gap: 20px; margin: 20px 0;">
        <div style="flex: 1;">
            <img src="{{home}}/assets/img/2025-08/guardrails-archi-centralisee.png" alt="Architecture Centralisée" style="width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" />
        </div>
        
        <div style="flex: 1;">
            <h3 style="color: #6f42c1;">🌐 Couche Front</h3>
            <div style="background: white; padding: 15px; border-radius: 8px; margin-bottom: 15px;">
                <h4>1. Applications</h4>
                <ul style="list-style: none; padding-left: 0;">
                    <li>🔄 <strong>API Gateway</strong>
                        <ul style="padding-left: 20px;"><li>Kong</li><li>Azure API Management</li><li>AWS API Gateway</li></ul>
                    </li>
                    <li>⚖️ <strong>Load Balancer</strong>
                        <ul style="padding-left: 20px;"><li>HAProxy</li><li>NGINX</li><li>AWS ELB</li></ul>
                    </li>
                    <li>📖 <strong>Service Registry</strong>
                        <ul style="padding-left: 20px;"><li>Consul</li><li>Eureka</li><li>etcd</li></ul>
                    </li>
                </ul>
            </div>
        </div>
        
        <div style="flex: 1;">
            <h3 style="color: #6f42c1;">⚙️ Couche Back</h3>
            <div style="background: white; padding: 15px; border-radius: 8px; margin-bottom: 15px;">
                <h4>2. Guardrails & LLMs</h4>
                <ul style="list-style: none; padding-left: 0;">
                    <li>🎯 <strong>Frameworks</strong>
                        <ul style="padding-left: 20px;">
                            <li>Langkit (Microsoft)</li>
                            <li>NeMo Guardrails (NVIDIA)</li>
                            <li>Guardrails OSS (Anthropic)</li>
                        </ul>
                    </li>
                    <li>🤖 <strong>LLMs</strong>
                        <ul style="padding-left: 20px;">
                            <li>Azure OpenAI</li>
                            <li>AWS Bedrock</li>
                            <li>Vertex AI</li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </div>

    <div style="display: flex; gap: 20px; margin-top: 20px;">
        <div style="flex: 1; background: white; padding: 15px; border-radius: 8px;">
            <h3 style="color: #28a745;">✅ Avantages</h3>
            <ul style="list-style: none; padding-left: 0;">
                <li>🎯 Gestion centralisée des politiques</li>
                <li>🔄 Mise à jour cohérente des règles</li>
                <li>📊 Monitoring unifié</li>
                <li>💰 Économies d'échelle</li>
            </ul>
        </div>
        <div style="flex: 1; background: white; padding: 15px; border-radius: 8px;">
            <h3 style="color: #dc3545;">⚠️ Points de Vigilance</h3>
            <ul style="list-style: none; padding-left: 0;">
                <li>🎯 Point de défaillance unique</li>
                <li>⏱️ Latence supplémentaire</li>
                <li>🔒 Moins de flexibilité</li>
            </ul>
        </div>
    </div>
</div>

<div style="background: linear-gradient(to right, #fd7e14, #e65f02); color: white; padding: 15px; border-radius: 8px; margin: 20px 0; text-align: center;">
    <h2 style="margin: 0; font-size: 1.4em;">🔄 Architecture Distribuée</h2>
    <p style="margin: 10px 0 0 0; font-size: 0.9em; opacity: 0.9;">Une approche décentralisée pour plus de flexibilité</p>
</div>

<div style="background: #f8f9fa; padding: 20px; border-radius: 8px; margin: 20px 0;">
    <div style="text-align: center; margin-bottom: 20px;">
     <div style="flex: 1;">
            <img src="{{home}}/assets/img/2025-08/archi-distribue.png" alt="Architecture Décentralisée" style="width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" />
        </div> 
</div>
    

    <div style="display: flex; gap: 20px;">
        <div style="flex: 1; background: white; padding: 15px; border-radius: 8px;">
            <h3 style="color: #28a745;">✅ Avantages</h3>
            <ul style="list-style: none; padding-left: 0;">
                <li>🎨 Personnalisation fine par application</li>
                <li>🛡️ Résilience et indépendance</li>
                <li>⚡ Performance optimisée</li>
                <li>🔄 Déploiement découplé</li>
            </ul>
        </div>
        <div style="flex: 1; background: white; padding: 15px; border-radius: 8px;">
            <h3 style="color: #dc3545;">⚠️ Points de Vigilance</h3>
            <ul style="list-style: none; padding-left: 0;">
                <li>🔧 Complexité de gestion</li>
                <li>⚖️ Risque d'incohérence</li>
                <li>🔄 Duplication d'efforts</li>
            </ul>
        </div>
    </div>
</div>

<div style="background: linear-gradient(to right, #17a2b8, #138496); color: white; padding: 15px; border-radius: 8px; margin: 20px 0; text-align: center;">
    <h2 style="margin: 0; font-size: 1.4em;">🔗 Architecture Hybride</h2>
    <p style="margin: 10px 0 0 0; font-size: 0.9em; opacity: 0.9;">Le meilleur des deux mondes</p>
</div>

<div style="background: #f8f9fa; padding: 20px; border-radius: 8px; margin: 20px 0;">
    <div style="display: flex; gap: 20px;">
        <div style="flex: 1; background: white; padding: 15px; border-radius: 8px;">
            <h3 style="color: #17a2b8;">🔄 Composants Clés</h3>
            <ul style="list-style: none; padding-left: 0;">
                <li>🌐 <strong>Guardrails centraux</strong> : politiques communes</li>
                <li>🎯 <strong>Guardrails locaux</strong> : spécificités métier</li>
                <li>🧠 <strong>Orchestration intelligente</strong> : selon le contexte</li>
            </ul>
        </div>
    </div>
</div>

---

# **Considérations de Performance** ⚡

<div style="background: linear-gradient(to right, #007bff, #0056b3); color: white; padding: 15px; border-radius: 8px; margin: 20px 0; text-align: center;">
    <h2 style="margin: 0; font-size: 1.4em;">⚡ Impact sur la Performance ⚡</h2>
    <p style="margin: 10px 0 0 0; font-size: 0.9em; opacity: 0.9;">Comprendre les temps de traitement et leurs implications</p>
</div>

<div style="background: #f8f9fa; padding: 20px; border-radius: 8px; margin: 20px 0;">
    <table style="width: 100%; border-collapse: collapse; margin: 15px 0;">
        <thead style="background: #007bff; color: white;">
            <tr>
                <th style="padding: 10px; text-align: left;">Type de Validation</th>
                <th style="padding: 10px; text-align: center;">Latence Typique</th>
                <th style="padding: 10px; text-align: right;">Impact Utilisateur</th>
            </tr>
        </thead>
        <tbody>
            <tr style="border-bottom: 1px solid #dee2e6;">
                <td style="padding: 10px;">⚡ Validation syntaxique</td>
                <td style="padding: 10px; text-align: center;">< 10ms</td>
                <td style="padding: 10px; text-align: right;">✨ Imperceptible</td>
            </tr>
            <tr style="border-bottom: 1px solid #dee2e6;">
                <td style="padding: 10px;">🔒 Détection PII</td>
                <td style="padding: 10px; text-align: center;">50-100ms</td>
                <td style="padding: 10px; text-align: right;">👍 Acceptable</td>
            </tr>
            <tr style="border-bottom: 1px solid #dee2e6;">
                <td style="padding: 10px;">🧠 Analyse sémantique</td>
                <td style="padding: 10px; text-align: center;">200-500ms</td>
                <td style="padding: 10px; text-align: right;">👀 Perceptible</td>
            </tr>
            <tr>
                <td style="padding: 10px;">📊 Validation factuelle</td>
                <td style="padding: 10px; text-align: center;">1-3s</td>
                <td style="padding: 10px; text-align: right;">⏳ Significatif</td>
            </tr>
        </tbody>
    </table>
</div>

<div style="background: linear-gradient(to right, #28a745, #218838); color: white; padding: 15px; border-radius: 8px; margin: 20px 0; text-align: center;">
    <h2 style="margin: 0; font-size: 1.4em;">🔄 Stratégies d'Optimisation 🚀</h2>
    <p style="margin: 10px 0 0 0; font-size: 0.9em; opacity: 0.9;">Solutions pour améliorer les performances sans compromettre la sécurité</p>
</div>

<div style="display: flex; gap: 20px; margin: 20px 0;">
    <div style="flex: 1; background: #f8f9fa; padding: 20px; border-radius: 8px;">
        <h3 style="color: #28a745;">🎯 Optimisation Préventive</h3>
        <ul style="list-style: none; padding-left: 0;">
            <li>⚡ <strong>Validation progressive</strong> : Arrêt au premier échec</li>
            <li>💾 <strong>Cache intelligent</strong> : Réutilisation des validations</li>
            <li>🔄 <strong>Parallélisation</strong> : Traitement simultané des règles</li>
        </ul>
    </div>
    
    <div style="flex: 1; background: #f8f9fa; padding: 20px; border-radius: 8px;">
        <h3 style="color: #28a745;">⚖️ Compromis Performance/Sécurité</h3>
        <ul style="list-style: none; padding-left: 0;">
            <li>📊 <strong>Profils adaptatifs</strong> selon le niveau de risque</li>
            <li>🔄 <strong>Validation asynchrone</strong> pour les contrôles non-bloquants</li>
            <li>📈 <strong>Sampling intelligent</strong> pour les validations coûteuses</li>
        </ul>
    </div>
</div>


---

# **Conclusion** 🎯

Les guardrails constituent la **première ligne de défense** pour sécuriser les agents IA. Ils permettent de **contrôler les interactions**, **prévenir les risques** et **assurer une expérience utilisateur fiable et conforme**.

Le prochain article détaillera les différents types de guardrails et leurs stratégies de mitigation spécifiques.

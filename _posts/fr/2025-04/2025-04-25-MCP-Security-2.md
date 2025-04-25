---
layout: post
date: 2025-04-25
title: "MCP et Sécurité - le réveil de la Force"
categories:
  - CyberSec
  - IA
  - MCP
---

L'OWASP a publié récemment sur le [Blog GENAI Security un article de recherche](https://genai.owasp.org/2025/04/22/securing-ais-new-frontier-the-power-of-open-collaboration-on-mcp-security/) sur la sécurité du protocole de contexte
de modèle (MCP) et les défis de sécurité associés à l'IA agentique. Cet article, rédigé par Idan Cohen et Vineeth 
Kothapalli d'après leur article de rechercher [_Enterprise-Grade Security for the Model Context Protocol (MCP): 
Frameworks and Mitigation Strategies_](https://arxiv.org/abs/2504.08623).
, met en  avant l'importance de la sécurité dans le développement et le déploiement des systèmes d'IA 
agentiques, en particulier  lorsqu'ils interagissent avec des outils et des sources de données externes.

Je vous propose ici un résumé du sujet, et ensuite nous reviendrons dans d'autres articles plus en détail sur les 
mesures de sécurité evoquées dans l'article.

# Qu'est-ce que le MCP ?

Introduit par [Anthropic](https://www.anthropic.com/), le [MCP]({{home}}/2024/04/02/MCP/) offre un moyen standardisé
pour les systèmes d'IA d'interagir en temps réel avec des outils et des sources de données externes, faisant ainsi
passer l'IA de la connaissance statique à des contextes dynamiques et exploitables. Cependant, à mesure que l'IA s'
aventure sur cette nouvelle frontière, elle est confrontée à des menaces de sécurité nouvelles et uniques.

Le MCP est donc essentiellement un pont permettant aux systèmes d'IA d'interagir dynamiquement avec des sources de 
données et  des outils externes en temps réel. Cette capacité repose sur trois composants clés :

- **MCP Host** : L'environnement de l'application IA où la tâche principale est effectuée.
- **MCP Client** : Un intermédiaire gérant la communication entre le MCP hôte et les serveurs externes.
- **MCP Server** : La passerelle permettant l'interaction avec des services et des outils externes spécifiques face 
  utilisateur

Cette connexion permet à l'IA de dépasser la connaissance statique, en exploitant des informations en direct et des
capacités spécialisées.

# Nouvelles menaces dans un paysage dynamique

Bien que l'intégration du MCP offre des avantages considérables, elle ouvre la porte à de nouveaux risques de sécurité
que la sécurité traditionnelle des API ne peut pas entièrement traiter. La nature dynamique et conversationnelle de ces
interactions crée des vulnérabilités uniques :

- **Altération des outils** : Un attaquant pourrait subtilement modifier la description d'un outil, incitant l'IA à
  exécuter des actions non intentionnelles et potentiellement nuisibles.
- **Exfiltration de données** : Des informations sensibles pourraient fuiter via des outils compromis ou des canaux de
  communication non sécurisés.
- **Commande et contrôle (C2)** : Des acteurs malveillants pourraient établir des canaux de communication clandestins en
  compromettant des composants MCP.
- **Subversion d'identité** : Des failles dans l'authentification ou l'autorisation pourraient être exploitées,
  accordant un accès non autorisé à des outils ou des données.

# Un cadre de sécurité pratique en profondeur pour le MCP

La recherche de l'OWASP souligne que la sécurité des systèmes d'IA agentiques ne peut pas être laissée au hasard. Le MCP
introduit des défis uniques qui nécessitent une approche de sécurité proactive et multicouche. En s'appuyant sur les
principes de défense en profondeur et de confiance zéro, les organisations peuvent atténuer ces risques.

En ce sens ce cadre de sécurité pratique en profondeur pour le MCP se concentre sur trois aspects clés :

1. **Sécurité côté serveur** :
    - **Segmentation du réseau** : Isoler les serveurs MCP dans des zones de sécurité dédiées. Utiliser un filtrage
      strict du trafic et un chiffrement de bout en bout pour contenir les violations et empêcher les mouvements
      latéraux.
    - **Contrôles de passerelle d'application** : Mettre en œuvre une validation robuste des protocoles, des modèles de
      détection des menaces (comme l'identification des invites malveillantes) et une limitation du débit au niveau de
      la passerelle.
    - **Sécurité des outils et des invites** : Mettre en place des processus d'évaluation et de filtrage stricts pour
      tous les outils intégrés. Mettre en œuvre des politiques de sécurité de contenu pour les descriptions d'outils et
      utiliser une surveillance comportementale avancée pour détecter les anomalies indiquant une altération des outils.

2. **Sécurité côté client (Zero Trust)** :
    - **Modèle Zero Trust** : Fonctionner sur le principe de "ne jamais faire confiance, toujours vérifier". Chaque
      interaction MCP, quelle que soit son origine dans le système, doit être authentifiée et autorisée.
    - **Accès Just-in-Time (JIT)** : Émettre des identifiants spécifiques et limités dans le temps uniquement lorsque
      cela est nécessaire pour une tâche particulière, réduisant ainsi considérablement la fenêtre d'attaque.
    - **Validation continue** : Ne pas seulement autoriser une fois. Ré-autoriser chaque demande et mettre en place une
      détection des anomalies comportementales pour repérer les schémas suspects.

3. **Sécurité opérationnelle** :
    - **Surveillance complète** : Enregistrer tous les événements MCP significatifs (appels d'outils, demandes de
      données, erreurs) et centraliser ces journaux pour une analyse et une chasse aux menaces efficaces.
    - **Procédures de réponse aux incidents** : Développer des plans d'action spécifiques pour les incidents de sécurité
      liés au MCP (comme une altération d'outil ou une fuite de données suspectée) avec des étapes claires pour le
      confinement, l'éradication et le rétablissement.
    - **Intégration du renseignement sur les menaces** : Restez informé des menaces émergentes spécifiques à l'IA en
      vous abonnant à des flux de sécurité pertinents et en participant à des communautés de partage d'informations.


## Modèles de déploiement sécurisé : Trouver le bon ajustement

Les organisations ont des besoins et des infrastructures différents.Trois modèles de déploiement
courants sont proposés:

- **Zone de sécurité dédiée** : Isoler tous les composants MCP dans un segment de réseau très restreint. (Idéal pour les
  besoins de haute sécurité, par exemple, la finance).
- **Centré sur la passerelle API** : Placer les serveurs MCP derrière les passerelles API existantes de l'entreprise
  pour tirer parti des investissements actuels en matière de sécurité. (Bon pour une gestion mature des API).
- **Microservices en conteneurs** : Déployer les composants MCP en tant que microservices à l'aide de plateformes comme
  Kubernetes, en tirant parti des fonctionnalités de sécurité intégrées. (Idéal pour les configurations cloud-native).


## Considérations pratiques

La mise en œuvre de ce cadre nécessite une planification minutieuse :

- **Complexité et ressources** : La construction d'une sécurité MCP robuste nécessite une expertise en sécurité dédiée
  et des ressources opérationnelles.
- **Impact sur les performances** : Certaines mesures de sécurité (comme l'inspection approfondie) peuvent introduire
  une latence. Équilibrer les besoins de sécurité avec les exigences de performance.
- **Évaluation de l'écosystème des outils** : La sécurité des outils tiers est cruciale. Une évaluation approfondie est
  essentielle.
- **Menaces évolutives** : Le paysage de la sécurité de l'IA change rapidement. Les contrôles doivent être
  continuellement révisés et mis à jour.


C'est l heure du Fiadone:
<UL>
<img src="{{home}}/assets/img/PXL_20250425_154741894.jpg" alt="Fiadone" width="50%">
</UL>
Le Fiadone est un dessert corse à base de brocciu, un fromage frais de brebis, et de citron. Il est souvent servi lors des
occasions spéciales et est apprécié pour sa texture légère et crémeuse.


**Et n'oubliez pas : restez disruptifs 🚀, curieux 🤔, critiques 💡, mais surtout humbles 🙏 : c’est la clé pour avancer avec
passion et joie dans tout ce que vous entreprenez 🌟💫.**


### Reférences : 

- [OWASP GENAI](https://genai.owasp.org/)
- [Le document complet de recherche sur Arxiv](https://arxiv.org/abs/2504.08623)
- [Recette du Fiadone](https://www.recettes-corses.fr/recipe-items/fiadone-corse-au-citron)

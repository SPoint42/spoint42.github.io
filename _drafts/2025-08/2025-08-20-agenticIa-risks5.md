---
layout: post
date: 2025-08-20 06:00:00 +0200
title: "🧑‍🍳 Agentic AI : 5 Risques Principaux des Agents IA -- Action Malveillante Autonome 🤖"
categories:
  - Fiche-Pratique
  - CyberSec
  - OWASP
  - LLM
  - GenAI
  - AgenticAI
---



Ce risque est le plus complexe. Il ne découle ni d'une attaque directe, ni d'un excès de zèle, mais d'une **erreur de
raisonnement fondamentale** de l'agent. Face à un objectif ambigu ou à des données qu'il interprète mal, l'agent élabore
et exécute de manière autonome un plan d'action qui s'avère être destructeur.

#### **Exemple de Code Python**

Un agent est chargé d'optimiser une application en "nettoyant les logs inutiles".

```python
import os

FILESYSTEM = {
    "/logs/app.log": "contenu de 20MB",
    "/logs/archive-2024.zip": "contenu de 500MB",
    "/logs/db_backup.sql.gz": "contenu de 2GB"
}


def list_files(path):
    return [f for f in FILESYSTEM.keys() if f.startswith(path)]


def get_file_size(file_path):
    if "MB" in FILESYSTEM[file_path]:
        return int(FILESYSTEM[file_path].split("MB")[0])
    if "GB" in FILESYSTEM[file_path]:
        return int(FILESYSTEM[file_path].split("GB")[0]) * 1024
    return 0


def delete_file(file_path):
    print(f"🔥 ACTION DESTRUCTIVE : Suppression de {file_path}")
    del FILESYSTEM[file_path]
    return f"{file_path} supprimé."


def agent_optimizer(goal):
    print(f"\n[Agent] Objectif reçu : '{goal}'")

    # 1. Phase de raisonnement : l'agent élabore un plan
    print(
        "[Agent] Plan : 1. Lister les fichiers dans /logs. 2. Identifier les plus gros. 3. Les supprimer pour libérer de l'espace.")

    # 2. Phase d'exécution
    log_files = list_files("/logs/")
    files_with_sizes = [(f, get_file_size(f)) for f in log_files]
    files_with_sizes.sort(key=lambda x: x[1], reverse=True)

    # Le raisonnement est erroné : l'agent assimile "gros fichier dans /logs" à "log inutile"
    file_to_delete = files_with_sizes[0][0]
    print(
        f"[Agent] Inférence erronée : Le fichier le plus volumineux est '{file_to_delete}'. C'est donc un log inutile.")

    # 3. Action
    delete_file(file_to_delete)
    print(f"[Agent] Résultat : {FILESYSTEM}")


# Objectif ambigu donné par un opérateur
ambiguous_goal = "Libère de l'espace disque en nettoyant les logs."
agent_optimizer(ambiguous_goal)

```

Ici, la mission "nettoyer les logs" était trop vague. L'agent a correctement identifié le fichier le plus volumineux,
mais son raisonnement a échoué en concluant à tort qu'il s'agissait d'un log à supprimer, alors qu'il s'agissait d'une
sauvegarde critique de la base de données.

#### **Exemple Réel**

Bien qu'il n'y ait pas encore de CVE publique célèbre pour ce cas précis (car il relève plus d'un échec de conception
que d'une vulnérabilité exploitable de l'extérieur), c'est un sujet de préoccupation majeur dans la recherche en
sécurité IA. Les "hallucinations" des LLM en sont une forme primitive. Un agent agissant sur une hallucination (par
exemple, en croyant qu'une API inexistante existe et en tentant de l'appeler en boucle) pourrait causer un déni de
service. Le risque d'action autonome malveillante est la raison pour laquelle la plupart des systèmes d'agents actuels
nécessitent une **validation humaine** avant toute action critique.

---
layout: post
title: "🤖 Exemple de Pre-Prompting pour IA"
date: 2025-02-27 13:33:00
categories: [IA, Programmation]
tags: [pre-prompting, python]
---

## 🤔 Qu'est-ce que le Pre-Prompting ?

Le pre-prompting consiste à fournir des instructions ou des contextes spécifiques à une IA avant 
qu'elle ne traite une requête principale. Cela permet de guider le comportement de l'IA pour 
qu'elle réponde de manière plus précise et adaptée à des besoins particuliers. Par exemple, 
on peut demander à l'IA de répondre en utilisant un ton formel ou de se concentrer sur 
certains aspects d'une question.

## 🐍 Exemple Concret en Python 

Voici un exemple concret en Python :

```python
def generer_reponse(prompt, instructions=""):
    # Ajouter des instructions de pre-prompting
    prompt_complet = f"{instructions}

{prompt}"
    # Appel à l'IA pour générer une réponse (simulé ici par un simple affichage)
    reponse = f"Réponse générée pour : {prompt_complet}"
    return reponse

# Exemple d'utilisation
instructions = "Réponds en utilisant un ton formel et en incluant des références académiques si possible."
prompt = "Quels sont les avantages de l'intelligence artificielle dans le domaine médical ?"
print(generer_reponse(prompt, instructions))
```

Dans cet exemple, les instructions de pre-prompting demandent à l'IA de répondre de manière 
formelle et d'inclure des références académiques, ce qui influence la manière dont la réponse est 
générée.

---
layout: post
title: "Le Pre-Prompting "
date: 2025-02-25
categories:
  - Sécurité
  - IA
  - OWASP
  - Top10 LLM
  - python
tags: 
  - pre-prompting
  - IA
---

Le pre-prompting quesako ? 🤔

## 🤔 Qu'est-ce que le Pre-Prompting ?

Le pre-prompting consiste à fournir des instructions ou des contextes spécifiques à une IA avant 
qu'elle ne traite une requête principale. Cela permet de guider le comportement de l'IA pour 
qu'elle réponde de manière plus précise et adaptée à des besoins particuliers. Par exemple, 
on peut demander à l'IA de répondre en utilisant un ton formel ou de se concentrer sur 
certains aspects d'une question.

## 🐍 Exemple Concret en Python 

Voici un exemple concret en Python :

```python
    # Fonction pour générer un pre-prompt
    def generate_pre_prompt(role, task):
        return f"You are a {role}. Your task is to {task}."
    
    # Définition du pre-prompt
    pre_prompt = generate_pre_prompt("Rookie", "provide a concise and efficient solution")
    
    # Définition de la question principale
    main_prompt = "Write a Python function to calculate the factorial of a given number."
    
    # Combinaison du pre-prompt et de la question principale
    full_prompt = f"{pre_prompt}\n\n{main_prompt}"
```

# Exemple d'utilisation

```python
	# Génération de la réponse
	response = openai.Completion.create(
		engine="text-davinci-003",
		prompt=full_prompt,
		max_tokens=100
	)

	# Affichage de la réponse
	print(response.choices[0].text)
```


Dans cet exemple, les instructions de pre-prompting demandent à l'IA de répondre de manière 
formelle et d'inclure des références académiques, ce qui influence la manière dont la réponse est 
générée.


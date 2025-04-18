import os
import xml.etree.ElementTree as ET

from dotenv import load_dotenv
import requests
from datetime import date
from google import genai
DEBUG = False

def parse_rss(xml_file):
    """Parse le fichier RSS et extrait les contenus clés"""
    tree = ET.parse(xml_file)
    root = tree.getroot()

    articles = []
    for item in root.findall('.//item'):
        title = item.find('title').text
        description = item.find('description').text
        articles.append(f"## {title}\n{description}\n")

    return "\n".join(articles)[:5000]  # Limite pour respecter le contexte



load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

rss_urls = (
    ["https://feeds.feedburner.com/TheHackersNews", "The Hacker News"],
    ["https://www.cert.ssi.gouv.fr/feed/", "CERT-FR"],
    ["https://aws.amazon.com/security/security-bulletins/rss/feed/", "AWS Security Bulletins"],
    ["https://feeds.feedburner.com/GoogleOnlineSecurityBlog", "Google Online Security Blog"]
)

today = date.today().strftime("%Y-%m-%d")
os.mkdir(f"{today}") if not os.path.exists(f"{today}") else None
tabFile = list()

for url in rss_urls:
    try :
        print(f"Récupération du flux RSS depuis {url[0]}...")
        response = requests.get(url[0])
        if response.status_code != 200:
            print (f"Erreur lors de la récupération du flux RSS : {response.status_code}")
        else :
            print (f"Flux RSS récupéré avec succès depuis {url[0]}")

            with open(f"{today}/{url[1]}temp.rss", 'w') as f:
                f.write(response.text)
            rss_content = parse_rss(f"{today}/{url[1]}temp.rss")
            tabFile.append (client.files.upload(file=f"{today}/{url[1]}temp.rss"))
    except :
        print (f"Erreur lors de la récupération du flux RSS depuis {url[0]} : {response.status_code}")
        continue


format_article  = f"""
---
layout: post
title: "Veille automatisée du {today}"
date: {today}
categories:
  - veille
  - vulnérabilités
  - sécurité
---

Voici la veille de sécurité du {today} :

# ⚠️Alertes de sécurité importantes (CVSS > 8.5)⚠️
    Place le titre des articles  dont la CVSS est supérieure a 8.5 

# Sommaire
Place ici le sommaire
   
## Place ici le ritre de l'article 
    Place ici le résumé de l'article (#résumé-de-larticle)
* CVE si existante + lien vers la page de la CVE 
* Score CVSS (si existant sinon afficher inconnu) + Score EPSS ((si existant sinon afficher inconnu) 

"""

prompt = f"""
Tu es un expert en cybersécurité et tu dois analyser ces {tabFile} représentant le contenu de ta veille du {today} 
et provenant de test flux RSS. 



Tu dois respecter les consignes suivantes : 
- Tu dois analyser ces fichiers pour créer un seul document que tu publiera 
sur ton blog de veille a destination de l'ensemble de tes équipes. Le document que tu publiera doit uniquement comporter des 
éléments  publiés ou mis a jour dans ces fichiers rss le {today}.
- Tu dois analyser les articles parlant de vulnérabilités ou d'attaque zero-day uniquement.
- Je veux que tu ne prennes en compte que les articles dont la date de publication est le {today}.
- Ne pas inclure d'articles qui ne parlent pas de cybersécurité
- Ne pas inclure d'articles qui ne parlent pas de menaces
- Tu dois effectuer ton analyse uniquement  sur les elements fournis dans les fichiers {tabFile} et ne pas inclure 
d'autres sources.

Lorsque tu trouves un contenu qui parle de vulnérabilités ou d'attaques zero-day, tu dois créer un element  structuré (
article) comportant :
    - le résumé de l'article
    - le lien hypertexte vers l'article 
    - l'identifiant CVE(si existant sinon mettre Inconnue + le score CVSS(si existant sinon mettre Inconnu) + le score 
    EPSS(si existant sinon mettre Inconnu ) ainsi le lien hypertexte vers la page CVE concernée
    - la source de donnees de l'article (ex: The Hacker News, CERT-FR, ...)
    
Lorsque tous les {tabFile} sont traités, tu dois créer un sommaire comportant les titres des articles et les liens vers les articles
Le sommaire doit être généré en fonction des titres des articles et comporter les liens vers les articles.
Le contenu doit être traduit en francais. 
Tu peux  inclure des emoticons pour rendre le contenu plus attrayant

Je ne souhaite pas avoir d'explication de tes choix, je n'ai pas besoin que le fichier indique le format yaml ou 
markdown, ni que tu me donnes autre chose que le contenu brut pour que je  puisse directement le publier avec  jekyll.


{format_article}
"""

if DEBUG :
    print("Prompt :\n")
    print(prompt)
    print("\n\n")
    print("Liste des modèles disponibles :\n")
    for m in client.models.list():
        print(f"""{m.display_name} : {m.name}""")

response = client.models.generate_content(model='gemma-3-27b-it',
contents= prompt)

markdown_filename = f"{today}-veille.md"
with open(markdown_filename, "w", encoding="utf-8") as md_file:
    md_file.write(response.text)


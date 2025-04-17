import google.generativeai as genai
import os
import xml.etree.ElementTree as ET

from dotenv import load_dotenv
import requests
from datetime import date

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


# Charger les variables d'environnement depuis un fichier .env
load_dotenv()

# Configurer l'API avec votre clé
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
# Sélectionner le modèle Gemini à utiliser
model = genai.GenerativeModel('gemini-2.0-flash')


rss_urls = (
    ["https://feeds.feedburner.com/TheHackersNews", "The Hacker News"],
    ["https://www.cert.ssi.gouv.fr/feed/", "CERT-FR"]
)



for url in rss_urls:
    print(f"Récupération du flux RSS depuis {url[0]}...")
    response = requests.get(url[0])
    if response.status_code != 200:
        raise Exception(f"Erreur lors de la récupération du flux RSS : {response.status_code}")
    print (f"Flux RSS récupéré avec succès depuis {url[0]}")
    with open(f"{url[1]}temp.rss", 'w') as f:
        f.write(response.text)
    rss_content = parse_rss(f"{url[1]}temp.rss")

    format_article  = f"""    
    Titre de l'article 
        Résumé de l'article (#résumé-de-larticle)
        Score CVSS + Score EPSS + Lien vers l'article + Lien vers la page CVE
    """


    prompt = f"""
Agis comme un expert en veille informatique. Voici le contenu d'un  flux RSS :
{rss_content}
Tu dois analyser les articles parlant de vulnérabilités uniquement.

Tu dois respecter les consignes suivantes :
2. Ne pas inclure d'articles qui ne parlent pas de cybersécurité
3. Ne pas inclure d'articles qui ne parlent pas de menaces

Pour chacun des articles, génère un element structuré comportant :
    - le résumé de l'article
    - le lien hypertexte vers l'article 
    - l'identifiant CVE(si existant sinon mettre Inconnue + le score CVSS(si existant sinon mettre Inconnu) + le score 
    EPSS(si existant sinon mettre Inconnu ) le lien hypertexte vers la page CVE concernée

Je ne souhaite pas avoir d'explication de tes choix, je n'ai pas besoin que le fichier indique le format yaml ou 
markdown, ni que tu me donnes autre chose que le contenu brut pour que je 
puisse directement le publier avec  jekyll.

Le sommaire doit être généré en fonction des titres des articles et comporter les liens vers les articles.
Le contenu doit être en français. 
Tu dois inclure des emoticons pour rendre le contenu plus attrayant

Le format de ta réponse doit etre le  suivant 

{format_article}
"""

    today = date.today().strftime("%Y-%m-%d")
    response = model.generate_content(prompt)
    markdown_filename = f"{today}-veille-{url[1]}.md"
    with open(markdown_filename, "a", encoding="utf-8") as md_file:
        # Écris le contenu de la réponse
        md_file.write(response.text)

## ensuite on creer un seul fichier depuis tous les fichiers
## parcourir tous les fichiers de veille et en creer un seul, puis
prompt = f"""
Voici le contenu plusieurs  fichiers de  veille {veille}. Je souhaite que tu me les fusionnes en un seul fichier markdown.
"""


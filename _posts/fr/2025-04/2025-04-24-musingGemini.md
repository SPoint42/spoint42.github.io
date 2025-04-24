---
layout: post
date: 2025-04-24
title: "Musing avec Gemini... pendant les jours de pluie..."
categories:
    - LLM
    - Gemini
    - GenAI
---

Il pleut sur Bordeaux en cette semaine de Paques, mes nains regardent un film ou dorment encore,j'ai donc un peu de 
temps. 

Je me décide dont de faire un petit tour sur [Gemini](https://ai.google.dev/), le modèle de Google. 

Je me suis donné comme objectif de tester l'API et les fonctionnalités de Gemini, et de voir si je peux l'utiliser 
pour ma veille sécurité. En effet, je screen tous les jours de nombreux sites de sécurité, et je me dis que Gemini 
pourrait m'aider à faire le tri dans tout cela facilement, car je n'ai pas envie de payer un [Feedly AI](https://feedly.com/ai) :). 

Je vais donc essayer de lui faire faire un résumé de mes flux RSS, et voir si il est capable de me donner
un résumé pertinent de l'actualité sécurité.


Je reprends donc un petit script python tout bete qui permet d'aller chercher des flux RSS et de les parser : 
```python
import os
import xml.etree.ElementTree as ET

from dotenv import load_dotenv
import requests
from datetime import date
from google import genai
import argparse

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

```

Ensuite, j'initialise le client Gemini avec ma clé API, et je lui demande de me faire un résumé de mes flux RSS.
```python
if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser(description="Generation de veille via un model")
    parser.add_argument("-d", "--debug", help="Activer le mode debug.")
    parser.add_argument("-m", "--model", help="model a utiliser.")

    args = parser.parse_args()

    try:
        api_key = os.getenv("GEMINI_API_KEY")
        client = genai.Client(api_key=api_key)

        rss_urls = (
            ["https://feeds.feedburner.com/TheHackersNews", "The-Hacker-News"],
            ["https://www.cert.ssi.gouv.fr/feed/", "CERT-FR"],
            ["https://aws.amazon.com/security/security-bulletins/rss/feed/", "AWS-Security-Bulletins"],
            ["https://feeds.feedburner.com/GoogleOnlineSecurityBlog", "Google-Online-Security-Blog"]
        )
        rsscontent = ""
        today = date.today().strftime("%Y-%m-%d")
        os.mkdir(f"{today}") if not os.path.exists(f"{today}") else None
        tabFile = list()
        for url in rss_urls:
            try:
                print(f"Récupération du flux RSS depuis {url[0]}...")
                response = requests.get(url[0])
                if response.status_code != 200:
                    print(f"Erreur lors de la récupération du flux RSS : {response.status_code}")
                else:
                    print(f"Flux RSS récupéré avec succès depuis {url[0]}")
                    with open(f"{url[1]}temp.xml", 'w') as f:
                        f.write(response.text)
                    rsscontent += parse_rss(f"{url[1]}temp.xml")
                    tabFile.append (client.files.upload(file=f"{today}/{url[1]}temp.rss"))
                    
            except Exception as e:
                raise (e)
```

Je veux une sortie en format post Jekyll pour faire tourner tout cela dans mon github....
```python
format_article = f"""
# ⚠️Important Security Alerts (CVSS > 7.5)⚠️
    Place an emoji and  the titles of articles with a CVSS score above 7.5 here

## Table of Contents
    Place the table of contents here

## Place an emoji here and Place the Article Title here
    Place the article summary here
* Place an emoji for CVE  + CVE if available + link to the CVE page
* Place an emoji for CVSS  + CVSS score (if available, otherwise don't add the line ) 
* Place an emoji for EPSS + EPSS score (if available, otherwise don't add the line ) 
        """
```
Maintenant je passe au prompting (et la je me suis amusé longtemps, car j'ai testé l'API de Gemini, et je suis tombé 
sur un bug lié au fichiers uploader et de faire référence, malgré que la doc dit que c'est possible...Doit y avoir 
un soucis de décodage [d'entités XML quelconque](https://cwe.mitre.org/data/definitions/611.html) qq part car je n'y arrive pas....) 

Mon prompt qui bug (d'ou la présence dans l'init de `tabFile=list()`). Et quand je regarde les retours, les fichiers 
sont bien uploadés, je n'ai aucune erreur, mais Gemini, n'arrive pas a y 'accéder' ..... 
```python
prompt=f"""
        Act like an CyberSecurity  monitoring expert. Here's the content of RSS feed in the following XML 
        files {tabFile}.
        You are an expert in cybersecurity and must analyze these files  to generate a cybersecurity monitoring article 
        summarizing the vulnerabilities  contained in these content.
        When you find content that discusses vulnerabilities, you must create an article if the content has been 
        published or updated at the date :  {today} or  the last 7 days before {today}
        
        Once content of all files is processed, you MUST create a table of contents with the article titles and 
        links to 
        these structured elements. The table of contents must be generated based on the article titles and include links 
        to the original articles. 
        All the content must be translated to french.
        You MUST include emojis to make the content more appealing on social networks.
         I don't want an explanation for your choices. The content MUST be directly usable in a jekyll post without 
         modification. You MUST not include any element before the content of the article that describe the content type
        The article must be structured as follows:
        {format_article}
        """
```
et celui qui bug pas .... 
```python
prompt=f"""
        Act like an CyberSecurity  monitoring expert. Here's the content of RSS feed:
            {rsscontent}.
        You are an expert in cybersecurity and must analyze these files  to generate a cybersecurity monitoring article 
        summarizing the vulnerabilities  contained in these content.
        When you find content that discusses vulnerabilities, you must create an article if the content has been 
        published or updated at the date :  {today} or  the last 7 days before {today}
        
        Once content is processed, you MUST create a table of contents with the article titles and links to 
        these structured elements. The table of contents must be generated based on the article titles and include links 
        to the original articles. 
        All the content must be translated to french.
        You MUST include emojis to make the content more appealing on social networks.
         I don't want an explanation for your choices. The content MUST be directly usable in a jekyll post without 
         modification. You MUST not include any element before the content of the article that describe the content type
        The article must be structured as follows:
        {format_article}
        """
```

J'appelle Gemini 
```python
response = client.models.generate_content(model=modele,
                                                  contents=[prompt])
        markdown_filename = f"{today}/{today}-veille-{modele.replace("models/", "")}.md"
        print(f"Creation du fichier markdown : {markdown_filename}")
        with open(markdown_filename, "w", encoding="utf-8") as md_file:
            md_file.write(f"""---
layout: post
title: "Veille automatisée du {today} via Gemini {modele}"
date: {today}
categories:
    - veille
    - vulnérabilités
    - sécurité
---
""")
            md_file.write(response.text.replace ("```markdown", "").replace("```", ""))
```
Et cela donne cela: 
* [avec le modele 2.0-flash]({{home}}/2025/04/24/veille-gemini-2.0-flash/) 
* [avec le modele 2.5-flash-preview-04-17]({{home}}/2025/04/24/veille-gemini-2.5-flash-preview-04-17/)
* [avec le modele gemini-2.5-pro-exp-03-25]({{home}}/2025/04/24/veille-gemini-2.5-pro-exp-03-25/)

Reste maintenant a mettre tout cela dans une action github tournant toutes les semaines pour voir la pertinence globale
de mon [POC](https://github.com/SPoint42/spoint42.github.io/blob/main/scripts/veille/pocGemini.py).....

_Oui, j'avoue le code est pas des plus propres...mais c'est un POC et je suis en congés...j'ai d'autres  choses a 
faire quand meme_
![miam]({{home}}/assets/img/PXL_20250424_103953917.jpg) 

**Et n'oubliez pas : restez disruptifs 🚀, curieux 🤔, critiques 💡, mais surtout humbles 🙏 : c’est la clé pour avancer avec
passion et joie dans tout ce que vous entreprenez 🌟💫.**

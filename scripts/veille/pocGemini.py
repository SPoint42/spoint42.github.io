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

            except Exception as e:
                raise (e)

        format_article = f"""---
layout: post
title: "Veille automatisée du {today}"
date: {today}
categories:
  - veille
  - vulnérabilités
  - sécurité
---

# ⚠️Important Security Alerts (CVSS > 7.5)⚠️
    Place here the titles of articles with a CVSS score above 7.5

## Table of Contents
    Place the table of contents here

## Place an emoji here and Place the Article Title here
    Place the article summary here
* Place an emoji for CVE  + CVE if available + link to the CVE page
* Place an emoji for CVSS  + CVSS score (if available, otherwise don't add the line ) 
* Place an emoji for EPSS + EPSS score (if available, otherwise don't add the line ) 
        """

        prompt = f"""
        Act like an CyberSecurity  monitoring expert. Here's the content of RSS feed:
            {rsscontent}.
        You are an expert in cybersecurity and must analyze these files  to generate a cybersecurity monitoring article 
        summarizing the vulnerabilities  contained in these content.
        When you find content that discusses vulnerabilities, you must create an article if the content has been 
        published  {today} or  the last 7 days before {today}
        
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

        if args.debug:
            print("Prompt :\n")
            print(prompt)
            print("\n\n")
            print("Liste des modèles disponibles :\n")
            for m in client.models.list():
                print(f"""{m.display_name} : {m.name}""")
        if args.model:
            modele = args.model
        else:
            modele = "gemini-2.0-flash"
        print(f"Modèle utilisé : {modele}")
        response = client.models.generate_content(model=modele,
                                                  contents=[prompt])
        markdown_filename = f"{today}/{today}-veille-{modele.replace("models/", "")}.md"
        print(f"Creation du fichier markdown : {markdown_filename}")
        with open(markdown_filename, "w", encoding="utf-8") as md_file:
            md_file.write(response.text)
    except Exception as e:
        raise (e)

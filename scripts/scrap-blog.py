import requests
from bs4 import BeautifulSoup
import os
import markdownify

# URL de base du blog
base_url = "http://blog.gioria.org/search/label/veille"

# Fonction pour obtenir les liens des articles
def get_article_links(url):
    try:
        print (f"Getting article links from {url}")
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        article_links = []
        print (response.content)
        # Supposons que les liens vers les articles sont dans des balises <a> avec une classe spécifique
        for link in soup.find_all('div', class_='article-link'):
            article_links.append(link.get('href'))

        return article_links
    except requests.exceptions.RequestException as e:
        raise (f"Error: {e}")
        return None

# Fonction pour télécharger et convertir un article en Markdown
def download_and_convert_article(url):
    try :
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Supposons que le contenu de l'article est dans une balise <div> avec une classe spécifique
        article_content = soup.find('div', class_='article-content')

        if article_content:
            # Convertir le contenu HTML en Markdown
            md_content = markdownify.markdownify(str(article_content), heading_style="ATX")
            return md_content
        return None
    except Exception as e:
        raise (f"Error: {e}")
        return None


# Fonction principale pour télécharger tous les articles
def main():
    # Créer un dossier pour sauvegarder les articles
    if not os.path.exists('articles'):
        os.makedirs('articles')

    # Obtenir les liens des articles
    try:
        article_links = get_article_links(base_url)

        for link in article_links:
            article_url = base_url + link
            md_content = download_and_convert_article(article_url)

            if md_content:
                # Sauvegarder le contenu Markdown dans un fichier
                filename = link.split('/')[-1] + '.md'
                with open(os.path.join('articles', filename), 'w', encoding='utf-8') as file:
                    file.write(md_content)
                print(f"Saved: {filename}")
    except Exception     as e:
        raise(f"Error: {e}")

if __name__ == "__main__":
    main()

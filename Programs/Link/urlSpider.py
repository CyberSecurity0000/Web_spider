# Bibliotecas
import sys
import requests
from bs4 import BeautifulSoup

# Conjunto de links
conj_links = set()


if not len(sys.argv) == 2:
    print("Usage: python3 urlSpider.py <url>")
    sys.exit(1)

def texto_html():

    try:
        url = sys.argv[1]
        html = requests.get(url)

        if html.status_code == 200:            
            return html.text

    except Exception:
        print("Conexão falhou !")

    return None


def main():

    try:
        html = texto_html()
        soup = BeautifulSoup(html, "html.parser")
    
        links = soup.find_all("a")

        for i in links:
            href = i.get("href")

            if href and href.startswith("http"):
                conj_links.add(href)


        ordem_links = sorted(conj_links)

        for i in ordem_links:
            print(i)
    
    except Exception:
        pass

# Programa
main()

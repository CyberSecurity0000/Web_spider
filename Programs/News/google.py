import requests
from colorama import Fore
from bs4 import BeautifulSoup
import pyfiglet


class Scrap:

    def __init__(self):
        self.url = url

    def scrape(self):

        resp = requests.get(self.url)
        soup = BeautifulSoup(resp.content.decode(),"xml",)

        #print(soup.prettify())
        tags = soup.find_all("item")
        print(pyfiglet.figlet_format("Google - Noticias", font="slant"))

        for i, j in enumerate(tags):

            title = j.find("title")
            links = j.find("link")

            if title:
                print(f"\n{Fore.LIGHTYELLOW_EX}Titulo{Fore.RESET}: {Fore.LIGHTGREEN_EX}{title.text}{Fore.RESET}")
                print(f"{Fore.LIGHTMAGENTA_EX}Link{Fore.RESET}: {Fore.LIGHTCYAN_EX}{links.text}{Fore.RESET}")

            if i+1 == 10:
                break

        print(f"\n{Fore.LIGHTRED_EX}Quantidade de notícias{Fore.RESET}: {Fore.BLUE}{i+1}{Fore.RESET}")


url = "https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419"
obj = Scrap()
obj.scrape()
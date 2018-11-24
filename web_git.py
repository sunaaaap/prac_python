
import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self,site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        sp = BeautifulSoup(r.read(),"html.parser")
        
        for tag in sp.find_all("a"):
            print(tag.get("href"))

news = "https://news.google.com/"
Scraper(news).scrape()

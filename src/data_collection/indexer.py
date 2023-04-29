import requests
from bs4 import BeautifulSoup

class Indexer:
    def __init__(self, url, pdp=[]):
        self.url = url
        self.sitemap = self.find_sitemap()
        self.pdp = pdp
        self.pdp_urls = []
    
    def find_sitemap(self):
        # Send a GET request to the desired URL
        response = requests.get(f'{self.url}/robots.txt')
        # Finding sitemap url under the assumption that a) sitemap is included in txt
        # file and b) sitemap is located as last component of txt file
        sitemap_url = response.text.lower().split('sitemap:')[-1].strip()
        # Return the the sitemap url
        return sitemap_url

    def find_pdp_urls(self):
        for pdp_page in self.pdp:
            # Send a GET request to the desired URL
            response = requests.get(pdp_page)
            # Find all relevant PDP urls
            pdp_urls = BeautifulSoup(response.text, 'lxml').find_all('loc')
            # Extend current list of urls
            self.pdp_urls += [url.text for url in pdp_urls]

    


    

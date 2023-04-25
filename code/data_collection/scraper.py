import requests
import selenium
from indexer import Indexer
from jcrew_utilities import get_info
from bs4 import BeautifulSoup

class Scraper(Indexer):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.product_data = []
    
    def scrape_prod_info(self):
        for url in self.pdp_urls:
            response = requests.get(url)
            if response.status_code == '200': 
                maybe_info = get_info(response)
                if maybe_info: self.product_data.append(maybe_info)
            else: continue
    
    def post_data(self):
        #pass in the data
        pass




s = Scraper(url='https://jcrew.com', pdp = ['https://www.jcrew.com/sitemap-wex/sitemap-pdp1.xml'])
    
s.find_pdp_urls()

print(s.pdp_urls)
        

    #now we have to figure out what pieces of information to parse and 
    #where we are storing it

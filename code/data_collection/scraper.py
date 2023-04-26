import requests
from indexer import Indexer
from jcrew_utilites import Jcrew_Utilities
import concurrent.futures
import json
from tqdm import tqdm

class Scraper(Indexer):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.product_data_json = []
    
    def scrape(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            list(tqdm(executor.map(self.scrape_prod_info, self.pdp_urls), total=len(self.pdp_urls)))
        # for url in self.pdp_urls:
        #     self.scrape_prod_info(url)
        

    def scrape_prod_info(self, url):
        response = requests.get(url)
        if response.status_code == 200: 
            jcrew = Jcrew_Utilities(url)
            maybe_info = jcrew.get_info()
            if maybe_info: self.product_data_json.append(maybe_info)
    
    #what are we doing a concurrent threader for ?
    #mapping over
    
    def post_data(self):
        #pass in the data
        pass




s = Scraper(url='https://jcrew.com', pdp = ['https://www.jcrew.com/sitemap-wex/sitemap-pdp1.xml'])
    
s.find_pdp_urls()

s.scrape()

with open ('/Users/irischeng/Documents/Instalily_CC/Instalily-CC-Chatbot/data/results.json', 'w') as outfile:
	json.dump(s.product_data, outfile, indent=2)
	print("File Dumped as results.json")
        

    #now we have to figure out what pieces of information to parse and 
    #where we are storing it

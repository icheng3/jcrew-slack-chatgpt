from indexer import Indexer
from jcrew_utilites_partial import Jcrew_Utilities
import concurrent.futures
from tqdm import tqdm

class Scraper(Indexer):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.product_data_json = []
    
    def scrape(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            list(tqdm(executor.map(self.scrape_prod_info, self.pdp_urls), total=(len(self.pdp_urls))))

    def scrape_prod_info(self, url):
        jcrew = Jcrew_Utilities(url)
        maybe_info = jcrew.get_info()
        if maybe_info: 
            self.product_data_json.append(maybe_info)
    
    def post_data(self):
        pass
    



        

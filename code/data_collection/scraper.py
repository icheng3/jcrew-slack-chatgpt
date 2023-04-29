from indexer import Indexer
from jcrew_utilites_partial import Jcrew_Utilities
import concurrent.futures
import json
from tqdm import tqdm

class Scraper(Indexer):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.product_data_json = []
    
    def scrape(self):
        print(self.pdp_urls)
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            list(tqdm(executor.map(self.scrape_prod_info, self.pdp_urls), total=(len(self.pdp_urls))))

    def scrape_prod_info(self, url):
        #response = requests.get(url)
        jcrew = Jcrew_Utilities(url)
        maybe_info = jcrew.get_info()
        if maybe_info: 
            self.product_data_json.append(maybe_info)
    
    def post_data(self):
        #pass in the data
        pass





        
# a = Scraper(url='https://jcrew.com', pdp = ['https://www.jcrew.com/sitemap-wex/sitemap-pdp2.xml'])
    
# a.find_pdp_urls()

# a.scrape()

# with open ('/Users/irischeng/Documents/Instalily_CC/Instalily-CC-Chatbot/data/results2.json', 'w') as outfile:
# 	json.dump(a.product_data_json, outfile, indent=2)
# 	print("File Dumped as results.json")

# b = Scraper(url='https://jcrew.com', pdp = ['https://www.jcrew.com/sitemap-wex/sitemap-pdp3.xml'])
    
# b.find_pdp_urls()

# b.scrape()

# with open ('/Users/irischeng/Documents/Instalily_CC/Instalily-CC-Chatbot/data/results3.json', 'w') as outfile:
# 	json.dump(b.product_data_json, outfile, indent=2)
# 	print("File Dumped as results.json")

# c = Scraper(url='https://jcrew.com', pdp = ['https://www.jcrew.com/sitemap-wex/sitemap-pdp4.xml'])
    
# c.find_pdp_urls()

# c.scrape()

# with open ('/Users/irischeng/Documents/Instalily_CC/Instalily-CC-Chatbot/data/results4.json', 'w') as outfile:
# 	json.dump(c.product_data_json, outfile, indent=2)
# 	print("File Dumped as results.json")

# d = Scraper(url='https://jcrew.com', pdp = ['https://www.jcrew.com/sitemap-wex/sitemap-pdp5.xml'])
    
# d.find_pdp_urls()

# d.scrape()

# with open ('/Users/irischeng/Documents/Instalily_CC/Instalily-CC-Chatbot/data/results5.json', 'w') as outfile:
# 	json.dump(d.product_data_json, outfile, indent=2)
# 	print("File Dumped as results.json")
#     #now we have to figure out what pieces of information to parse and 
#     #where we are storing it

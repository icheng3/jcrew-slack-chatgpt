import requests
import selenium
from indexer import Indexer
from bs4 import BeautifulSoup

class Scraper(Indexer):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.product_data = []
    
    def scrape_prod_info(self):
        for url in self.pdp_urls:
            data = {}
            response = requests.get(url)
            if response.status_code == '200':
                soup = BeautifulSoup(response.text, 'html')
                # check if sold out
                item_name = soup.find(id='product-name__p').text
                item_code = soup.find("section", class_="ProductDetailPage__code___SOGoM c-product__code")
                #for price, need to check if sale or not
                """metadata to find:
                - item name
                - item code
                - item price
                - recommendation/rating rate
                - available sizes
                - color
                - sizing (runs true to size..?)
                - """
                self.product_data.append(data)
    
    def post_data(self):
        #pass in the data
        pass




s = Scraper(url='https://jcrew.com', pdp = ['https://www.jcrew.com/sitemap-wex/sitemap-pdp1.xml'])
    
s.find_pdp_urls()

print(s.pdp_urls)
        

    #now we have to figure out what pieces of information to parse and 
    #where we are storing it

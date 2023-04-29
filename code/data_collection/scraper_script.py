from scraper import Scraper
import json

s = Scraper(url='https://jcrew.com', pdp = ['https://www.jcrew.com/sitemap-wex/sitemap-pdp3.xml'])
    
s.find_pdp_urls()

s.scrape()

with open ('/Users/irischeng/Documents/Instalily_CC/Instalily-CC-Chatbot/data/results3.json', 'w') as outfile:
	json.dump(s.product_data_json, outfile, indent=2)
	print("File Dumped as results.json")
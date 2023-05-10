from scraper import Scraper
import json

scraper = Scraper(url='https://jcrew.com', pdp=[f'https://www.jcrew.com/sitemap-wex/sitemap-pdp{i}.xml' for i in range(1,6)])
    
scraper.find_pdp_urls()
scraper.scrape()

with open ('/Users/irischeng/Documents/Instalily_CC/Instalily-CC-Chatbot/data/results.json', 'w') as outfile:
	json.dump(scraper.product_data_json, outfile, indent=2)
	print("File Dumped as results.json")















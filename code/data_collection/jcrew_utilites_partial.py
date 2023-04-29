from selenium import webdriver
from scrapy import Selector
from jcrew_xpaths import * 
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

class Jcrew_Utilities():
    """Class containing (partial) utility functions for scraping JCrew PDPs"""
    def __init__(self, url):
        self.url = url
        self.webdriver = webdriver.Chrome(options=chrome_options)
        self.sel = None
        self.curr_data = {}

    def get_info(self):
        """Retrieves item name and product description for the current PDP"""
        self.webdriver.get(self.url)
        maybe_content = self.webdriver.find_elements('xpath', content_xpath)
        i = 0
        while not maybe_content: #entered if unable to find container housing relevant production information, sometimes happens
        #when page isn't rendered complete on first try
            if i > 100: return {}
            time.sleep(0.2)
            maybe_content = self.webdriver.find_elements('xpath', content_xpath) 
            i += 1
        self.sel = Selector(text=self.webdriver.page_source)
        self.curr_data['item_name'] = self.get_name()
        self.curr_data['description'] = self.get_details()
        # if not self.sold_out():
        #     self.curr_data['colors'] = self.get_price()
        #     self.curr_data['price'] = self.get_colors()
        return self.curr_data

    def get_name(self):
        """Retrieves product details utilizing Scrapy Selector for speed"""
        return self.sel.xpath(f"{name_xpath}/text()").get(default='')

    def get_details(self):
        """Retrieves product details utilizing Scrapy Selector for speed"""
        return self.sel.xpath(f"{prod_details_xpath}/text()").get(default='')

    def sold_out(self):
        """Returns whether or not a product is sold out"""
        sold_out_res =  self.webdriver.find_elements('xpath', sold_out_xpath)
        return sold_out_res

    def get_price(self):
        """Retrieves product price, if current product is on sale through a range, then returns the lowest price point"""
        # UNCOMMENT BELOW if selenium is failing --------------------------------------------------------------------
        # maybe_price = self.soup.find_all('span', class_='is-price ProductPrice__regular-price___arzwy regular-price')
        # maybe_sale_price = self.soup.find_all('span', class_='ProductPrice__price___0KAYS')
        maybe_price = self.webdriver.find_elements('xpath', price_xpath)
        maybe_sale_price = self.webdriver.find_elements('xpath', sale_xpath)
        try:
            i = 0
            while not maybe_price and not maybe_sale_price: #entered if unable to find price element, sometimes happens
            #when page isn't rendered complete on first try
                if i > 10:
                    break
                time.sleep(0.2)
                self.webdriver.get(self.url)
                maybe_price = self.webdriver.find_elements('xpath', price_xpath)
                maybe_sale_price = self.webdriver.find_elements('xpath', sale_xpath)
                i += 1
                # UNCOMMENT BELOW if selenium is failing --------------------------------------------------------------------
                # maybe_price = self.soup.find_all('span', class_='is-price ProductPrice__regular-price___arzwy regular-price')
                # maybe_sale_price = self.soup.find_all('span', class_='ProductPrice__price___0KAYS')
            if maybe_price: return maybe_price.pop(0).text[1:]
            if maybe_sale_price: return maybe_sale_price.pop(0).text.split('-').pop(0)[1:]
            else: return ''
        except:
            return ''
    
    def get_colors(self):
        """Retrieves product colors"""
        try:
            item_color_container = self.webdriver.find_elements('xpath', color_container_xpath)
            if not item_color_container: return ''
            colors = []
            for container in item_color_container:
                inner = container.find_elements(By.TAG_NAME, "div")
                colors += [el.get_attribute('data-name').lower() for el in inner]
            colors = ",".join(colors)
            return colors
        except:
            return ''

    

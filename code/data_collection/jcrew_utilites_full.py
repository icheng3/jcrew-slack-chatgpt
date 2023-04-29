from bs4 import BeautifulSoup
from selenium import webdriver
from scrapy import Selector
from selenium.webdriver.common.by import By
from jcrew_xpaths import *
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

class Jcrew_Utilities():
    """Class containing utility functions for scraping JCrew PDPs"""
    def __init__(self, url):
        self.url = url
        self.webdriver = webdriver.Chrome(options=chrome_options)
        self.soup = None
        self.sel = None
        self.curr_data = {}

    def get_info(self):
        """Retrieves relevant information for the current PDP"""
        self.webdriver.get(self.url)
        maybe_content = self.webdriver.find_elements('xpath', content_xpath)
        i = 0
        while not maybe_content: #entered if unable to find container housing relevant production information, sometimes happens
        #when page isn't rendered complete on first try
            if i > 100:
                return {}
            time.sleep(0.2)
            maybe_content = self.webdriver.find_elements('xpath', content_xpath)
            i += 1
        self.sel = Selector(text=self.webdriver.page_source)
        self.soup = BeautifulSoup(self.webdriver.page_source, 'lxml')
        if not self.sold_out(): 
            self.curr_data['item_name'] = self.get_name()
            self.curr_data['item_id'] = self.get_id()
            self.curr_data['price'] = self.get_price()
            self.curr_data['colors'] = self.get_colors()
            self.curr_data['in_stock_sizes'], self.curr_data['sold_out_sizes'] = self.get_sizes()
            self.curr_data['item_type'] = ''
            self.curr_data['gender'] = ''
            self.curr_data['description'] = self.get_details()
            self.get_breadcrumbs()
        return self.curr_data

    def get_name(self):
        """Retrieves product details, utilizing Scrapy Selector for speed"""
        return self.sel.xpath(f"{name_xpath}/text()").get(default='')

    def get_id(self):
        """Retrieves the item id, utilizing Scrapy Selector for speed"""
        return self.sel.xpath(f"{id_xpath}/text()").get(default='')

    def get_price(self):
        """Retrieves product price, if current product is on sale through a range, then returns the lowest price point"""
        # UNCOMMENT BELOW if selenium is failing --------------------------------------------------------------------
        # maybe_price = self.soup.find_all('span', class_='is-price ProductPrice__regular-price___arzwy regular-price')
        # maybe_sale_price = self.soup.find_all('span', class_='ProductPrice__price___0KAYS')
        maybe_price = self.webdriver.find_elements('xpath', price_xpath)
        maybe_sale_price = self.webdriver.find_elements('xpath', sale_xpath)
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


    def get_colors(self):
        """Retrieves product colors"""
        item_color_container = self.webdriver.find_elements('xpath', color_container_xpath)
        if not item_color_container: return ''
        colors = []
        for container in item_color_container:
            inner = container.find_elements(By.TAG_NAME, "div")
            colors += [el.get_attribute('data-name').lower() for el in inner]
        colors = ",".join(colors)
        return colors

    def get_sizes(self):
        """Retrieves in stock and sold out sizes for current product"""
        item_size_container = self.webdriver.find_elements('xpath', size_container_xpath)
        if not item_size_container: return '', ''
        item_list = item_size_container[0].find_elements(By.TAG_NAME, 'div')
        in_stock = [el.get_attribute('data-name').lower() for el in item_list if el.get_attribute('aria-disabled') == 'false']
        sold_out = [el.get_attribute('data-name').lower() for el in item_list if el.get_attribute('aria-disabled') == 'true']
        in_stock = ",".join(in_stock)
        sold_out = ",".join(sold_out)
        return in_stock, sold_out

    def get_details(self):
        """Retrieves product details, utilizing Scrapy Selector for speed"""
        return self.sel.xpath(f"{description_xpath}/text()").get(default='')

    def get_breadcrumbs(self):
        """Retrieves breadcrumb elements for current product"""
        bread_container = self.webdriver.find_elements('xpath', bread_xpath)
        for container in bread_container:
            text = container.text.lower().strip()
            if text == 'home' or text =='back': continue
            if self.is_gendered_item(text): self.curr_data['gender'] = text
            else: self.curr_data['item_type'] += f'{text},'

    def is_gendered_item(self, text):
        """Returns whether or not a term is 'gendered'"""
        return text in set(('women', 'men', 'kids', 'girls', 'boys'))

    def sold_out(self):
        """Returns whether or not a product is sold out"""
        sold_out_res =  self.webdriver.find_elements('xpath', sold_out_xpath)
        return sold_out_res
    

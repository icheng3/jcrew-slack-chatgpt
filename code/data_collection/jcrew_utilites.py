from bs4 import BeautifulSoup
from selenium import webdriver
from scrapy import Selector
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

class Jcrew_Utilities():
    def __init__(self, url):
        self.url = url
        self.webdriver = webdriver.Chrome(ChromeDriverManager(version='112.0.5615.49').install(), options=chrome_options)
        self.soup = None
        self.sel = None
        self.curr_data = {}

    def get_info(self):
        self.webdriver.get(self.url)
        content_xpath = "//div[@class='ProductDetailPage__row___BSQwN']"
        maybe_content = self.webdriver.find_elements('xpath', content_xpath)
        while not maybe_content:
            #print('content not found')
            time.sleep(0.2)
            maybe_content = self.webdriver.find_elements('xpath', content_xpath)
        # price_xpath = "//div[@data-qaid='ProductPrice__price-list___G3o__ product__price--list ProductPrice__remove-margin___tKORn']"
        # sale_xpath = "//span[@class='ProductPrice__price___0KAYS']"
        # maybe_price = self.webdriver.find_elements('xpath', price_xpath)
        # maybe_sale_price = self.webdriver.find_elements('xpath', sale_xpath)
        # while not maybe_price and not maybe_sale_price:
        #     time.sleep(0.5)
        #     maybe_price = self.webdriver.find_elements('xpath', price_xpath)
        #     maybe_sale_price = self.webdriver.find_elements('xpath', sale_xpath)
        self.sel = Selector(text=self.webdriver.page_source)
        self.soup = BeautifulSoup(self.webdriver.page_source, 'lxml')
        if not self.sold_out(): 
            #print('getting info')
            self.curr_data['item_name'] = self.get_name()
            #print('name', self.data['item_name'])
            self.curr_data['item_id'] = self.get_id()
            #print('id', self.data['item_id'])
            self.curr_data['price'] = self.get_price()
            #print('price', self.data['price'])
            self.curr_data['colors'] = self.get_colors()
            #print('colors', self.data['colors'])
            self.curr_data['in_stock_sizes'], self.curr_data['sold_out_sizes'] = self.get_sizes()
            self.curr_data['item_type'] = []
            self.curr_data['gender'] = ''
            self.curr_data['description'] = self.get_details()
            self.get_breadcrumbs()
            print('got info', self.curr_data)
        return self.curr_data

    def get_name(self):
        return self.sel.xpath("//h1[@id='product-name__p']/text()").get()
        return self.soup.find(id='product-name__p').text

    def get_id(self):
        return self.sel.xpath("//section[@class='ProductDetailPage__code___SOGoM c-product__code']/text()").get()
        return self.soup.find("section", class_="ProductDetailPage__code___SOGoM c-product__code").text

    def get_price(self):
        price_xpath = "//span[@class='is-price ProductPrice__regular-price___arzwy regular-price']"
        sale_xpath = "//span[@class='ProductPrice__price___0KAYS']"
        #maybe_price = self.soup.find_all('span', class_='is-price ProductPrice__regular-price___arzwy regular-price')
        # ProductPrice__price-list___G3o__ product__price--list ProductPrice__remove-margin___tKORn
        #maybe_sale_price = self.soup.find_all('span', class_='ProductPrice__price___0KAYS')
        maybe_price = self.webdriver.find_elements('xpath', price_xpath)
        maybe_sale_price = self.webdriver.find_elements('xpath', sale_xpath)
        while not maybe_price and not maybe_sale_price:
            time.sleep(0.2)
            # maybe_price = self.webdriver.find_elements('xpath', price_xpath)
            # maybe_sale_price = self.webdriver.find_elements('xpath', sale_xpath)
            self.webdriver.get(self.url)
            #self.soup = BeautifulSoup(self.webdriver.page_source, 'lxml')
            # maybe_price = self.soup.find_all('span', class_='is-price ProductPrice__regular-price___arzwy regular-price')
            # maybe_sale_price = self.soup.find_all('span', class_='ProductPrice__price___0KAYS')
            maybe_price = self.webdriver.find_elements('xpath', price_xpath)
            maybe_sale_price = self.webdriver.find_elements('xpath', sale_xpath)
        if maybe_price: return float(maybe_price.pop(0).text[1:])
        if maybe_sale_price: return float(maybe_sale_price.pop(0).text.split('-').pop(0)[1:])


    def get_colors(self):
        #item_color_container = self.sel.xpath("//div[@class='product__colors colors-list ProductPriceColors__colors-list___Wx5Go']").extract()

        #item_color_container = self.webdriver.find_elements('xpath', "//div[@class='product__colors colors-list ProductPriceColors__colors-list___Wx5Go']")
            #'div', class_='product__colors colors-list ProductPriceColors__colors-list___Wx5Go')
        item_color_container = self.webdriver.find_elements('xpath', "//div[@class='product__colors colors-list ProductPriceColors__colors-list___Wx5Go']")
        print(item_color_container)
        colors = []
        for container in item_color_container:
            inner = container.find_elements(By.TAG_NAME, "div")
            colors += [el.get_attribute('data-name').lower() for el in inner]
        return colors

    def get_sizes(self):
        item_size_container = self.webdriver.find_element('xpath', "//div[@class='ProductSizes__sizes-list___1Pg_4']")
        item_list = item_size_container.find_elements(By.TAG_NAME, 'div')
        #tem_size_container = self.soup.find('div', class_='ProductSizes__sizes-list___1Pg_4')
        in_stock = [el.get_attribute('data-name').lower() for el in item_list if el.get_attribute('aria-disabled') == 'false']
        sold_out = [el.get_attribute('data-name').lower() for el in item_list if el.get_attribute('aria-disabled') == 'true']
        return in_stock, sold_out

    def get_details(self):
        description = self.sel.xpath("//p[@class='ProductDescription__intro___ZGbWh']/text()").get()
        return description

    def get_breadcrumbs(self):
        bread_container = self.webdriver.find_elements('xpath', "//li[@class='Breadcrumbs__breadcrumb-item___2PmjZ']")
        #'li', class_='Breadcrumbs__breadcrumb-item___2PmjZ')
        #bread_container = self.sel.xpath("//li[@class='Breadcrumbs__breadcrumb-item___2PmjZ']/text()").getall()
        for container in bread_container:
            text = container.text.lower().strip()
            if text == 'home' or text =='back': continue
            if self.is_gendered_item(text): self.curr_data['gender'] = text
            else: self.curr_data['item_type'].append(text)

    def is_gendered_item(self, text):
        #print('BREADCRUMB', text)
        return text in set(('women', 'men', 'kids', 'girls', 'boys'))

    def sold_out(self):
        #sold_out_res = self.sel.xpath("//div[@class='error-messages__message___WI2oU ProductSoldout__sold-out___ekdtz is-centered']").extract()
        sold_out_res =  self.webdriver.find_elements('xpath', "//div[@class='error-messages__message___WI2oU ProductSoldout__sold-out___ekdtz is-centered']")
        #print('res', sold_out_res)
        return sold_out_res
    

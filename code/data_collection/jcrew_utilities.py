from bs4 import BeautifulSoup

SOUP = None
DATA = {}

def get_info(response):
    DATA = {}
    SOUP = BeautifulSoup(response, 'lxml')
    if is_soldout: return DATA
    DATA['item_name'] = get_name()
    DATA['item_id'] = get_id()
    DATA['price'] = get_price()
    DATA['colors'] = get_colors()
    DATA['sizes'] = get_sizes()
    DATA['item_type'] = []
    DATA['gender'] = ''
    get_breadcrumbs()
    return DATA

def get_name():
    return SOUP.find(id='product-name__p').text

def get_id():
    return SOUP.find("section", class_="ProductDetailPage__code___SOGoM c-product__code").text

def get_price():
    maybe_price = SOUP.find_all('div', class_='ProductPrice__price-list___G3o__ product__price--list ProductPrice__remove-margin___tKORn')
    if maybe_price:
        return float(maybe_price.pop(0).text[1:])
    return get_sale_price()

def get_sale_price():
    price = SOUP.find('span', class_='ProductPrice__price___0KAYS')
    price = price.text.split('-').pop(0)[1:]
    return float(price)

def get_colors():
    item_color_container = SOUP.find_all('div', class_='product__colors colors-list ProductPriceColors__colors-list___Wx5Go')
    colors = []
    for container in item_color_container:
        colors += [el.get('data-name').lower() for el in container]
    return colors

def get_sizes():
    item_size_container = SOUP.find('div', class_='ProductSizes__sizes-list___1Pg_4')
    return [el.get('data-name').lower() for el in item_size_container if el.get('aria-disabled') == 'false']

def get_breadcrumbs():
    bread_container = SOUP.find('ul', class_='Breadcrumbs__breadcrumb___yYdHT')
    for i in range(len(bread_container)):
        if i == 0: continue
        text = bread_container[i].text.lower().strip()
        if is_gendered_item(text):
            DATA['gender'] = text
        else:
            DATA['item_type'].append(text)

def is_gendered_item(text):
    return text in set('women', 'men', 'kids', 'girls', 'boys')

def is_soldout():
    return SOUP.find_all('div', class_='error-messages__message___WI2oU ProductSoldout__sold-out___ekdtz is-centered') 
# error-messages__message___WI2oU ProductSoldout__sold-out___ekdtz is-centered
"""import re
import time
import logging
from shutil import which

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from cars.models import Car

class CarSpider():
    base_url = 'https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePageModel&entitySelectingHelper.selectedEntity=&zip={}'
    
    def __init__(self, zip_code):
        self.url = self.base_url.format(zip_code)
        self.zip_code = zip_code
        self.options = Options()
        self.driver = webdriver.Firefox(executable_path=which('geckodriver'), options=self.options)

    def start_scraper(self):
        self.driver.get(self.url)
        self.parse_html(self.driver.page_source)
        while True:
            try:
                wait = WebDriverWait(self.driver, 10)
                show_more = wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'nextPageElement')))
                time.sleep(3)
                show_more.click()
                self.parse_html(self.driver.page_source)
            except Exception as e:
                print(e)
                break
        
    def parse_html(self, html):
        soup = BeautifulSoup(html, "html.parser")
        listings_divs = soup.find_all('div', id=re.compile('^listing_'))
        for div in listings_divs:
            data = div.find('h4').get_text().strip().split(' ')
            price = div.find('span', {'class': 'cg-dealFinder-priceAndMoPayment'})
            spec_price = price.find_all('span')[0].get_text()
            car = Car()
            car.make = data[1]
            car.year = data[0]
            car.model = ' '.join(data[2:])
            car.zip_code = self.zip_code
            car.save()"""
import requests
from bs4 import BeautifulSoup

from cars.models import CarMake


class CarMakeSpider():
    base_url = 'https://www.cargurus.com/'
    
    def __init__(self):
        self.session = requests.Session()

    def start_scraper(self):
        r = self.session.get(self.base_url)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'html.parser')
            makes = soup.find('select', {'id': 'carPickerUsed_makerSelect'})
            optgroups = makes.find_all('optgroup')
            optgroup = optgroups[1]
            options = optgroup.find_all('option')
            lista = []
            for option in options:
                make = CarMake
                print(option.text)
                print(option['value'])
"""    def parse_html(self, html):
        soup = BeautifulSoup(html, "html.parser")
        listings_divs = soup.find_all('div', id=re.compile('^listing_'))
        for div in listings_divs:
            data = div.find('h4').get_text().strip().split(' ')
            price = div.find('span', {'class': 'cg-dealFinder-priceAndMoPayment'})
            spec_price = price.find_all('span')[0].get_text()
            car = Car()
            car.make = data[1]
            car.year = data[0]
            car.model = ' '.join(data[2:])
            car.zip_code = self.zip_code
            car.save()"""


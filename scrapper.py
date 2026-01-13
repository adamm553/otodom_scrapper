from bs4 import BeautifulSoup
import pandas as pd
import requests 
import time
from config import RENT_OR_BUY, TYPE, VOIVODESHIP, CITY, RECORDS

class Apartment:
    def __init__(self, title, price, rooms, area, address, floor):
        self.title = title
        self.price = price
        self.rooms = rooms
        self.area = area
        self.floor = floor

        if len(address) == 4:
            self.street = address[0].strip()
            self.district = address[1].strip()
            self.city = address[2].strip()
        else:
            self.street = "No data"
            self.district = address[0].strip()
            self.city = address[1].strip()
    
    def to_dict(self):
        return {
            "Title": self.title,
            "Price": self.price,
            "Rooms": self.rooms,
            "Area": self.area,
            "Floor": self.floor,
            "Street": self.street, 
            "District": self.district,
            "City": self.city
        }

class Parser:

    @staticmethod
    def parse_article(article):
        price_tag = article.find('span', attrs={'data-sentry-element': 'MainPrice'})
        price = price_tag.get_text(strip=True) if price_tag else "Null"

        rooms_tag = article.find('span', string=lambda t: t and 'pok' in t)
        rooms = rooms_tag.get_text(strip=True) if rooms_tag else "Null"

        title_tag = article.find('p', attrs={'data-cy': 'listing-item-title'})
        title = title_tag.get_text(strip=True) if title_tag else "Null"

        area_tag = article.find('span', string=lambda t: t and "m²" in t and "zł" not in t)
        area = area_tag.get_text(strip=True) if area_tag else "Null"

        address_tag = article.find('p', attrs={'data-sentry-component': 'Address'})
        address = address_tag.get_text(strip=True).split(",") if address_tag else ["null", "null"]

        floor_tag = article.find('span', string=lambda t: t and 'piętro' in t)
        if not floor_tag:
            floor_tag = article.find('span', string=lambda t: t and 'parter' in t)
        floor = floor_tag.get_text(strip=True) if floor_tag else "null"

        return Apartment(title, price, rooms, area, address, floor)
    

class Scrapper:

    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers
        self.apartments = []

    def fetch_page(self, page_num):
        url = f"{self.base_url}/{RENT_OR_BUY}/{TYPE}/{VOIVODESHIP}/{CITY}/{CITY}/{CITY}?limit={RECORDS}&page={page_num}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return BeautifulSoup(response.content, 'html.parser')
    
    def run(self, start_page, end_page):
        for num in range(start_page, end_page + 1):
            soup = self.fetch_page(num)
            if not soup:
                continue
        
            articles = soup.find_all('article')
            for art in articles:
                apr_obj = Parser.parse_article(art)
                self.apartments.append(apr_obj)
            time.sleep(5)

    def to_csv(self, name):
        data = [apt.to_dict() for apt in self.apartments]
        df = pd.DataFrame(data)
        df.to_csv(name, index=False, encoding='utf-8-sig')

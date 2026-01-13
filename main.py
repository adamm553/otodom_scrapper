from scrapper import Scrapper
from config import BASE_URL, HEADERS, START_PAGE, END_PAGE

if __name__ == "__main__":
    

    scraper = Scrapper(BASE_URL, HEADERS)
    scraper.run(START_PAGE, END_PAGE) 
    scraper.to_csv("Mieszkania_OOP.csv") 
BASE_URL = "https://www.otodom.pl/pl/wyniki"
HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
START_PAGE = 1
END_PAGE = 2

RENT_OR_BUY = "wynajem" # type "wynajem" if you want to rent or "sprzedaz" if you want to buy
TYPE = "mieszkanie" # type "mieszkanie" if you want to buy an apartment or "dom" if you want to buy a house
VOIVODESHIP = "slaskie" # type any other voivodeship
CITY = "sosnowiec" # type your location
RECORDS = 72 # possible values are [24, 36, 48, 72]
FILE_NAME = "apartments.csv"
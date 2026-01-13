
```markdown
# Otodom Real Estate Scraper

An object-oriented Python web scraper designed to extract real estate data from the Otodom portal. This tool automates the process of gathering property information such as titles, prices, room counts, area, and location details.

## Project Structure

The project is divided into modules:

- `main.py`: The entry point of the application.
- `scrapper.py`: Contains the core logic (Data Model, HTML Parser, and the Scraper engine).
- `config.py`: Centralized configuration for URLs, Headers, and Scraping limits.

##  Tech Stack

- **Python 3.x**
- **BeautifulSoup4**: For parsing HTML content.
- **Requests**: For handling HTTP protocols.
- **Pandas**: For data manipulation and CSV exporting.

##  Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/adamm553/otodom_scrapper

```

2. **Install dependencies**:
```bash
pip install -r requirements.txt

```


*(Note: Ensure you have `beautifulsoup4`, `requests`, and `pandas` installed)*.

##  Configuration

You can modify the scraping parameters in the `config.py` file:

```python
BASE_URL = "[https://www.otodom.pl/](https://www.otodom.pl/)..."
START_PAGE = 1
END_PAGE = 2
RENT_OR_BUY = "wynajem" # type "wynajem" if you want to rent or "sprzedaz" if you want to buy
TYPE = "mieszkanie" # type "mieszkanie" if you want to buy an apartment or "dom" if you want to buy a house
VOIVODESHIP = "slaskie" # type any other voivodeship
CITY = "sosnowiec" # type your location
RECORDS = 72 # possible values are [24, 36, 48, 72]
FILE_NAME = "apartments.csv"

```

##  Usage

Simply run the `main.py` script to start the extraction process:

```bash
python main.py

```

##  Data Output

The generated CSV includes the following columns:

* **Title**: The headline of the listing.
* **Price**: Total price of the apartment.
* **Rooms**: Number of rooms.
* **Area**: Total area in square meters (m²).
* **Floor**: Floor level (e.g., "1 piętro", "parter").
* **Street / District / City**: Granular location data extracted from the address string.

##  Legal Disclaimer

This project was created for educational purposes. Scraping websites may violate their Terms of Service. Please use responsibly and check the website's `robots.txt` before intensive scraping.

---

Created by Adam Piątek



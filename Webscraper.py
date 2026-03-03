import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from openpyxl.utils.exceptions import InvalidFileException

def scrape_books():
    url = "http://books.toscrape.com/"
    
    try:
        # Send request to website
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises HTTPError if bad response
        
    except requests.exceptions.RequestException as e:
        print("Error while connecting to website:", e)
        return []

    try:
        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("article", class_="product_pod")
        
        data = []
        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            availability = book.find("p", class_="instock availability").text.strip()
            
            data.append([title, price, availability])
        
        return data
    
    except Exception as e:
        print("Error while parsing data:", e)
        return []


def save_to_excel(data):
    try:
        wb = Workbook()
        ws = wb.active
        ws.title = "Scraped Data"

        # Header
        ws.append(["Title", "Price", "Availability"])

        # Data rows
        for row in data:
            ws.append(row)

        wb.save("scraped_books.xlsx")
        print("Data saved successfully to scraped_books.xlsx")

    except PermissionError:
        print("Permission denied. Close the Excel file if it is open.")
    
    except InvalidFileException as e:
        print("Invalid file error:", e)
    
    except Exception as e:
        print("Error while saving Excel file:", e)


if __name__ == "__main__":
    print("Scraping started...")
    
    scraped_data = scrape_books()
    
    if scraped_data:
        save_to_excel(scraped_data)
    else:
        print("No data scraped.")
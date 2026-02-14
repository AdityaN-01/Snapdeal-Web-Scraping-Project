import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Base URL
base_url = "https://www.snapdeal.com/search"

headers = {
    "User-Agent": "Mozilla/5.0"
}

all_data = []

# Scraping Multiple Pages
for page in range(1, 6):

    params = {
        "keyword": "mens sports shoes",
        "page": page
    }

    response = requests.get(base_url, headers=headers, params=params)
    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.find_all("div", class_="product-tuple-listing")

    for item in products:

        # Product Name
        name = item.find("p", class_="product-title")
        name = name.text.strip() if name else None

        # Price
        price = item.find("span", class_="product-price")
        price = price.text.strip().replace("Rs.", "") if price else None

        # Discount
        discount = item.find("span", class_="product-discount")
        discount = discount.text.strip() if discount else None

        # Brand
        brand = item.get("data-brand") if item else None

        # Rating
        rating = item.find("div", class_="filled-stars")
        rating = rating["style"] if rating else None

        all_data.append({
            "Product Name": name,
            "Brand": brand,
            "Price": price,
            "Discount": discount,
            "Rating": rating
        })

    print(f"Page {page} Scraped Successfully")

    time.sleep(2)  # Avoid blocking

# Save to CSV
df = pd.DataFrame(all_data)
df.to_csv("snapdeal_shoes.csv", index=False)

print("Data Saved to snapdeal_shoes.csv")


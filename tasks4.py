import requests
from bs4 import BeautifulSoup
import re
import time
from config import *

def get_price():
     headers = {
        "User-Agent": "Mozilla/5.0"
    }
     response = requests.get(PRODUCT_URL , headers=headers)
     soup = BeautifulSoup(response.text, "html.parser")
     price_text = soup.find("p", class_="price_color").text
     price = float(re.search(r"\d+\.\d+", price_text).group())
     return price

def send_webhook(price):
    data = {
        "content": f"Price Alert!\nCurrent Price: £{price}\n{PRODUCT_URL}"
    }
    requests.post(WEBHOOK_URL, json=data)
print("Price Tracker Started")

while True:
    try:
        price = get_price()
        print("Current Price:", price)

        if price <= PRICE_LIMIT:
           print("Price Dropped!")
           send_webhook(price)

        else:
            print("Price is above target.")

    except Exception as e:
        print("Error:", e)

    print("----------------------")
    time.sleep(CHECK_INTERVAL)
    
        
import requests
from bs4 import BeautifulSoup

url = "https://omsk.kingstore.link/catalog/iphone/iphone-16/"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

prices = []

price_blocks = soup.find_all('div', class_='index-products-body-item__button-price')

for block in price_blocks:
    text = block.get_text(strip=True)
    if '₽' in text or 'руб' in text:
        digits = ''.join([ch for ch in text if ch.isdigit()])
        if digits:
            price = int(digits)
            if 50000 < price < 300000:
                prices.append(price)

if prices:
    print(f"Найдено товаров: {len(prices)}")
    print(f"Минимальная цена: {min(prices)} ₽")
    print(f"Максимальная цена: {max(prices)} ₽")
    print(f"Средняя цена: {sum(prices) / len(prices):.2f} ₽")
else:
    print("Цены не найдены. Проверьте сайт.")

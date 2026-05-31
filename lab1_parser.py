import requests
from bs4 import BeautifulSoup

url = "https://omsk.kingstore.link/catalog/iphone/iphone-16/"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

prices = []
# Ищем div с нужным классом
price_blocks = soup.find_all('div', class_='index-products-body-item__button-price')

for block in price_blocks:
    text = block.get_text(strip=True)
    if '₽' in text or 'руб' in text:
        # Извлекаем цифры
        digits = ''.join([ch for ch in text if ch.isdigit()])
        if digits:
            price = int(digits)
            if 50000 < price < 300000:  # фильтр разумных цен
                prices.append(price)

if prices:
    print(f"Найдено товаров: {len(prices)}")
    print(f"Минимальная цена: {min(prices)} ₽")
    print(f"Максимальная цена: {max(prices)} ₽")
    print(f"Средняя цена: {sum(prices) / len(prices):.2f} ₽")
    
    with open("result_variant7.txt", "w", encoding="utf-8") as f:
        f.write(f"Вариант 7\n")
        f.write(f"URL: {url}\n")
        f.write(f"Найдено товаров: {len(prices)}\n")
        f.write(f"Минимальная цена: {min(prices)} ₽\n")
        f.write(f"Максимальная цена: {max(prices)} ₽\n")
        f.write(f"Средняя цена: {sum(prices) / len(prices):.2f} ₽\n")
        f.write("\nВсе цены (отсортировано):\n")
        for p in sorted(prices):
            f.write(f"{p} ₽\n")
    print("\nРезультат сохранён в файл result_variant7.txt")
else:
    print("Цены не найдены. Проверьте сайт.")

import re
import json
from pathlib import Path


# Read raw.txt
file_path = Path(__file__).parent / "raw.txt"

with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()


# 1. Extract product names
product_names = re.findall(
    r"(?ms)^\d+\.\s*\n(.+?)\n\d+,\d{3}\s*x",
    text
)


# 2. Extract product prices
prices = re.findall(
    r"Стоимость\s*\n([\d\s]+,\d{2})",
    text
)

clean_prices = []

for price in prices:
    price = price.replace(" ", "").replace(",", ".")
    clean_prices.append(float(price))


# 3. Calculate total
calculated_total = sum(clean_prices)


# 4. Extract date and time
date_time = re.search(
    r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})",
    text
)

if date_time:
    date = date_time.group(1)
    time = date_time.group(2)
else:
    date = None
    time = None


# 5. Extract payment method
payment = re.search(
    r"(Банковская карта|Наличные)",
    text
)

if payment:
    payment_method = payment.group(1)
else:
    payment_method = "Unknown"


# 6. Extract receipt total
total_match = re.search(
    r"ИТОГО:\s*\n([\d\s]+,\d{2})",
    text
)

if total_match:
    receipt_total = total_match.group(1)
    receipt_total = receipt_total.replace(" ", "").replace(",", ".")
    receipt_total = float(receipt_total)
else:
    receipt_total = None


# Create product list
products = []

for name, price in zip(product_names, clean_prices):
    products.append({
        "name": name.strip(),
        "price": price
    })


# Structured output
result = {
    "date": date,
    "time": time,
    "payment_method": payment_method,
    "products": products,
    "calculated_total": calculated_total,
    "receipt_total": receipt_total
}


# Print JSON
print(json.dumps(result, ensure_ascii=False, indent=4))
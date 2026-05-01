import re
import json

# Read receipt text
with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Extract prices (supports formats like 1200, 1200.50, 1,200.50)
prices = re.findall(r"\d+[.,]?\d*", text)

# Extract date (example: 2026-05-01 or 01/05/2026)
date_match = re.search(r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b", text)
date = date_match.group() if date_match else None

# Extract time (example: 14:35)
time_match = re.search(r"\b\d{1,2}:\d{2}\b", text)
time = time_match.group() if time_match else None

# Extract payment method
payment_match = re.search(
    r"(cash|card|visa|mastercard|paypal)",
    text,
    re.IGNORECASE
)
payment_method = payment_match.group() if payment_match else None

# Extract product lines (basic assumption)
product_lines = re.findall(r"([A-Za-z ]+)\s+\d+[.,]?\d*", text)

# Calculate total amount
numeric_prices = []
for price in prices:
    cleaned = price.replace(",", ".")
    try:
        numeric_prices.append(float(cleaned))
    except ValueError:
        pass

calculated_total = sum(numeric_prices)

# Create structured output
parsed_receipt = {
    "products": product_lines,
    "prices": numeric_prices,
    "date": date,
    "time": time,
    "payment_method": payment_method,
    "calculated_total": calculated_total
}

# Print formatted JSON
print(json.dumps(parsed_receipt, indent=4))
def convert_currency(amount, conversion_rate):
    """Converts USD to another currency based on the conversion rate."""
    return round(amount * conversion_rate, 2)

# Real-world example:
usd_amount = 100
conversion_rate_to_euro = 0.85  # 1 USD = 0.85 Euro
print("Converted Amount in Euros:", convert_currency(usd_amount, conversion_rate_to_euro))

# Currencies = {"USD": 1.17, "EUR": 1.00}
# def conv(summ: float, current: str, received: str):
#     heft = summ / Currencies[current]
#     return round(heft * Currencies[received], 2)
# print(conv(100, "USD", "EUR"))

def Currency(volume, USD = 1.17):
    convert_in_EUR = volume / USD
    return round(convert_in_EUR, 2)
print(Currency(100))
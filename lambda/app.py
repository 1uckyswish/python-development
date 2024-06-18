items = [
    ("product1", 88),
    ("product2", 20),
    ("product3", 14),
    ("product4", 50),
]

prices = []

for item in items:
    prices.append(items[1])

prices2 = list(map(lambda item: item[1], items))

print(prices2)

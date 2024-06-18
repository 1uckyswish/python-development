items = [
    ("product1", 88),
    ("product2", 20),
    ("product3", 14),
    ("product4", 50),
]


filtered = list(filter(lambda item: item[1] <= 20, items))

print(filtered);

prices = [item for item in items if item[1] <= 20]

print(prices)
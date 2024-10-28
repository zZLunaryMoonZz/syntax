#price = list(map(int, input('Введите цены:').split(', ')))
price = [5, 10, 15, 25, 20]   

low_price = price.index(min(price))               #index[int]
high_price = price.index(max(price))              #index[int]

price[low_price], price[high_price] = max(price), min(price)

print(price)
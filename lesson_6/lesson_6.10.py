#price_str = input('Введите цены:').split(', ')
#price = list(map(int, price_str)) #делаем список int
price = [10, 20, 30, 40, 50]

over_sum = sum(price)     #считаем сумму
print('Средняя цена товаров:',  int(over_sum / len(price)))
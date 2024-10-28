price = list(map(int, input('Введите цены:').split(', '))) #делаем список int
price.sort(reverse = True)

print('Отсортированные цены:', ', '.join(map(str,price)))
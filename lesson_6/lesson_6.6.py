supplies = input("Введите товары через запятую:").split(', ')  #list[str]
new_position = int(input('Позиция для нового товара:'))        #int
new_index = new_position - 1                                   #int
new_product = input('Введите новый товар')                     #str
supplies.insert(new_index, new_product)

print('Товары на полке:', ', '.join(map(str,supplies)))
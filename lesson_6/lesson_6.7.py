supplies = input('Введите товары через запятую: ').split(', ')
position = int(input('Позиция для удаления товара:'))

#пользователь вводит позицию товара, я мы переводим ее в [int] индекс: 
index_for_del = position - 1 

supplies.pop(index_for_del)
supplies = ', '.join(supplies)
print('Товары на полке:', supplies)
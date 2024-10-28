#supplies = input('Введите товары: ').split(', ')
supplies = ['Чай', 'Мед', 'Сахар']
print('Позиции для перестановки: 1, 3')
#out_position, in_position = int(input()), int(input())
out_position, in_position = 1, 3
out_index, in_index = out_position - 1, in_position - 1 
supplies[out_index], supplies[in_index] = supplies[in_index], supplies[out_index]

print(supplies)

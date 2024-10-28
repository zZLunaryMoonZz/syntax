a = input("Введите цены: ")
b = a.split(', ')
print (a)
c = b[1::2]
print(f"Цены без скидки: ", ', '.join(c))
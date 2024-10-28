a = input("Введите строку: ")
b = a.split()

c = []

for word in b:
    c.append(word[::-1])

print(" ".join(c))
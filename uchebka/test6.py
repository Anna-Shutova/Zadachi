mice = int(input("Введите количество мышей: "))
names = []
for i in range(mice):
    name = input("Введите имя мышки: ")
    names.append(name)

print(*names)
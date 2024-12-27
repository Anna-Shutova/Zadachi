number = int(input("Введите число больше 9: "))
edinitca = number % 10
desyatki = (number // 10) % 10
print(f"В числе {number}, единиц - {edinitca}, десятков - {desyatki}")

number = input("Введите двузначное число: ")
print(number[::-1])

number1 = int(input("Другой метод, Введите число: "))
print(f"{number1 % 10}{number1 // 10}")

number = input("Введите трехзначное число: ")
num2 = number[1] + number[0] + number[2]
print(f"Новое число:  {num2}")


# Другой вариант
number = int(input("Введите трехзначное число: "))
num1 = number // 100
num2 = (number // 10) % 10
num3 = number % 10
print(f"{num2}{num1}{num3}")

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

# все числа диапазона
user_list = [i for i in range(num1, num2 + 1)]
print(user_list)

# от максимального к минимальному
print(*user_list[::-1])

# кратные семи
print(*[i for i in user_list if i % 7 == 0])

# количество кратных пяти
print(len([i for i in user_list if i % 5 == 0]))


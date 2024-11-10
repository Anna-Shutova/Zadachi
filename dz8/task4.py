summa = 0
number = int(input("Введите число: "))
maximum = number
minimum = number

while number != 7:
    number = int(input("Введите число: "))
    summa += number
    print("Сумма: ", summa)
    if number < minimum:
        minimum = number:
    elif number > maximum and number != 7:
        maximum = number
    elif number == minimum or number == maximum:
        continue
    else

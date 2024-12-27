number = int(input("Введите трехзначное число: "))
desyatki = (number // 10) % 10
sotie = number // 100

print(f"В числе {number}, десятков - {desyatki}, сотни - {sotie}")

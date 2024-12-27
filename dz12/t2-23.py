number = int(input("Введите четырехзначное число: "))
sotie = number // 100 % 10
thousands = number // 1000

print(f"В числе {number}, сотни - {sotie}, тысячи - {thousands}")

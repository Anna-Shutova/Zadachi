number = int(input("Введите трехзначное число: "))
edinitca = number % 10
desyatki = (number // 10) % 10
sotie = number // 100
summa = edinitca + desyatki + sotie
proizvedenie = edinitca * desyatki * sotie
print(f"в числе {number}, \n единиц - {edinitca}, \n десятки - {desyatki}, \n"
      f"сумма - {summa}, \n произведение - {proizvedenie}")

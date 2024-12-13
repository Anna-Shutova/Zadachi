number = int(input("Введите двузначное число: "))
desyatki = number // 10
edinitca = number % 10
summa = desyatki + edinitca
print(f"В числе {number},\n десятки - {desyatki},\n",
      f"единицы - {edinitca},\n сумма - {summa}")

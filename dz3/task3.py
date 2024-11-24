metres = int(input("Введите метры: "))
sm = metres * 100
dm = metres * 10
mm = metres * 1000
miles = round(metres / 1600, 2)
print(metres, sm, dm, mm, miles)
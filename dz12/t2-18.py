number = int(input("Введите трехзначное число: "))
n1 = str(number // 100)
n2 = str((number // 10) % 10)
n3 = str(number % 10)
result1 = n1 + n2 + n3
result2 = n1 + n3 + n2
result3 = n2 + n1 + n3
result4 = n2 + n3 + n1
result5 = n3 + n1 + n2
result6 = n3 + n2 + n3
print(result1, result2, result3, result4, result5, result6)

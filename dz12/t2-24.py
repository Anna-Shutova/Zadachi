# step1:
a = '237'
a = a.replace('2', '')

# step2:
a = int(a) * 10

# step3:
a = str(a)
a = a.replace('0', '2')
print(a)

# vvod = int(input('Введите длину стороны квадрата: '))


# for i in range(vvod):
#     for j in range(vvod):
#         print(" * ", end='')
#     print("\n")

# def draw_triangle(fill, base=10):
#     n = 1
#     for i in range(base):
#         i = [fill] * n
#         print(''.join(i))
#         n += 1


# draw_triangle('*')

n = 5

for i in range(n):
    for j in range(n):
        if j >= n - 1 - i:
            print('*', end='')
        else:
            print('', end='')
    print()
    
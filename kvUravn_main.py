#Решение квадратного уравнения
a = float(input('Введите значение a: '))
b = float(input('Введите значение b: '))
c = float(input('Введите значение c: '))

d= b**2 - 4*a*c
if d< 0:
    print('Корней нет')
elif d == 0:
    x = -b / (2 * a)
    print('x = ' + str(x))
else:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print('x1 = ' + str(x1))
    print('x2 = ' + str(x2))

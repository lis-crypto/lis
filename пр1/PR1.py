a = int(input('Введите значение a: '))
b = int(input('Введите значение b: '))
c = int(input('Введите значение c: '))
# Задание №1
a, b = b, a
print(a, b)
# Задание №2
print("a + b = ",
      a + b)
# Задание №3
print(a,'* x^2 +',b,'* x +',c)
D = b * b - 4 * a * c
if D >= 0:
    if D == 0:
        if a != 0:
            x = -b / (2 * a)
            print("Значение корня = ", x)
        else:
            print("Нет решения")
    else:
        if a != 0:
            x1 = (-b + D ** 0.5) / (2 * a)
            x2 = (-b - D ** 0.5) / (2 * a)
            print("Значения корней = ", x1, x2)
        else:
            print("Нет решения")
else:
    print("Нет решения")
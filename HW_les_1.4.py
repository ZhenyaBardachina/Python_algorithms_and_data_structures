# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)


print('Введите три различных целых числа')
a = int(input('Первое число: '))
b = int(input('Второе число: '))
c = int(input('Третье число: '))
if a < b < c or c < b < a:
    print(b)
elif a < c < b or b < c < a:
    print(c)
else:
    print(a)

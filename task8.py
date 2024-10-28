# Заполнить массив длины N случайными числами в диапазоне от 10 до 100000 и
# отобрать в другой массив все числа, которые состоят из одинаковых цифр.
# Используйте для этого логическую функцию.
# Пример: ввод N = 4
# [12, 77, 5555, 97]
# Вывод: [77, 5555]
import random
def get_random_list(n):
    listr = []
    while(n>0):
        n-=1
        listr.append(int(random.random()*99990+10))
    return listr
def equale(l):
    l2 = [];
    for i in l:
        if i>10000 and i%11111==0:
            l2.append(i)
        elif 10000>i>1000 and i%1111==0:
            l2.append(i)
        elif 1000>i > 100 and i % 111 == 0:
            l2.append(i)
        elif 100>i>10 and i%11==0:
            l2.append(i)
    return l2


n = int(input("Enter a number: "))
l = get_random_list(n)
print(l)
l2 = equale(l)
print(l2)
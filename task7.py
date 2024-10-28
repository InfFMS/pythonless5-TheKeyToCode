# Заполнить массив длины N случайными числами в интервале [-100,100] и
# переставить элементы так, чтобы все положительные элементы
# стояли в начала массива, а все отрицательные и нули в конце.
# Пример: ввод N = 6
# [20, -90, 15, -34, 10, 0]
# Вывод: [20, 15, 10, -90, -34, 0]
import random
def get_random_list(n):
    listr = []
    while(n>0):
        n-=1
        listr.append(int(random.random()*200-100))
    return listr
n = int(input("Enter a number: "))
l = get_random_list(n)
print(l)
l.sort(reverse = True)
print(l)
# Заполните массив длины N случайными числами в интервале [0,5].
# Определить, есть ли в нем элементы с одинаковыми значениями, стоящие рядом.
# Если есть, то выведете значение и индекс повторяющихся элементов
# Если нет, то написать "Нет"
# Пример: ввод N = 7
# [1, 2, 3, 3, 2, 2, 1]
# Вывод:
# значение:3 индексы 2 и 3
# значение:2 индексы 4 и 5
import random
def get_random_list(n):
    listr = []
    while(n>0):
        n-=1
        listr.append(int(random.random()*5))
    return listr
def has_ecuale_numbers_near(l):
    o = False
    for i in range(0,len(l)-1):
        if(l[i]==l[i+1]):
            o = True
            print("Indexes: " + str(i)  + " & " + str(i+1) + ", Value: " + str(l[i]))
    return o
n = int(input("Enter a number: "))
l = get_random_list(n)
print("1. Список: [", ", ".join(str(element) for element in l) + "]")
print("2. " + str(has_ecuale_numbers_near(l)))

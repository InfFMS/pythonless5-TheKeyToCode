# Заполните массив длины N случайными числами в интервале [0,100].
# Определить, есть ли в нем элементы с одинаковыми значениями,
# не обязательно стоящие рядом.
# Если есть, то выведете значение и индекс повторяющихся элементов
# Если нет, то написать "Нет"
# Пример: ввод N = 6
# [1, 2, 3, 2, 5, 10]
# Вывод:
# значение:2 индексы 1 и 3
import random
def get_random_list(n):
    listr = []
    while(n>0):
        n-=1
        listr.append(int(random.random()*100))
    return listr
def has_ecuale_numbers_near(l):
    o = False
    for i in range(0,len(l)-1):
        for j in range(i+1,len(l)):
            if(l[i]==l[j]):
                o = True
                print("Indexes: " + str(i)  + " & " + str(j) + ", Value: " + str(l[i]))
    return o
n = int(input("Enter a number: "))
l = get_random_list(n)
print("1. Список: [", ", ".join(str(element) for element in l) + "]")
print("2. " + str(has_ecuale_numbers_near(l)))

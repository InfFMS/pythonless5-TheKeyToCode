# При анализе данных, собранных в рамках научного эксперимента,
# бывает полезно удалить самое большое и самое маленькое значение.
# Сымитруем данные списком длины N со случайными числами в диапазоне от 0 до 1000
# Удалите из этого списка все значения, которые на 30 % отличаются
# от среднего значения списка
import random

def get_random_list(n):
    listr = []
    while(n>0):
        n-=1
        listr.append(int(random.random()*1000))
    return listr
def sred_value(l):
    s = 0
    for i in l:
        s+=i
    return s/len(l)
def delete_from_30(l,s_value):
    i = 0
    while i < len(l):
        if l[i]>s_value * 1.3 or l[i]<s_value*0.7:
            l.pop(i)
            i-=1
        i+=1
    return l
n = int(input("Enter a number: "))
l = get_random_list(n)
print("1. Список: [", ", ".join(str(element) for element in l) + "]")
sv = sred_value(l)
print("2. " + str(delete_from_30(l, sv)))

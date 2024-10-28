# Заполните список длины N случайными числами в диапазоне от 0 до 1000
# Выведите:
# 1.длину списка;
# 2.последний элемент списка;
# 3.список в обратном порядке (вспоминаем срезы);
# 4.YES, если список содержит трехзначное число, состоящее из одинаковых цифр
# NO в противном случае;
# 5.список с удаленными первым и последним элементами.
import random
def get_random_list(n):
    listr = []
    while(n>0):
        n-=1
        listr.append(int(random.random()*1000))
    return listr
def is_has_threecount_number(l):
    for i in l:
        if(99<i<1000):
            return True
    return False
n = int(input("Ведите число: "))
rlist = get_random_list(n)
print("0. Список: [", ", ".join(str(element) for element in rlist) + "]")
print("1. Длина списка: " + str(n))
print("2. Последний элемент списка: " + str(rlist[-1]))
print("3. список в обратном порядке: [" + ", ".join(str(element) for element in rlist[::-1]) + "]")
if(is_has_threecount_number(rlist)):
    print("4. YES")
else:
    print("4. NO")
print("5.список с удаленными первым и последним элементами: [" + ", ".join(str(element) for element in rlist[1:-1]) + "]")

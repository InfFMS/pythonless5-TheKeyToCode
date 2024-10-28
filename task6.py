# Массив имеет четное число элементов N.
# Заполнить массив случайными числами и
# выполнить реверс отдельно в первой половине и второй половине.
# Пример: ввод N = 6
# [1,2,3,4,5,6]
# Вывод: [3,2,1,6,5,4]
import random
def get_random_list(n):
    listr = []
    while(n>0):
        n-=1
        listr.append(int(random.random()*10))
    return listr
n = int(input("Enter a number: "))
l = get_random_list(n)
print(l)
l = (l[n//2-1::-1]) + l[:n//2-1:-1]
print(l)
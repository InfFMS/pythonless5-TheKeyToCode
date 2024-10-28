# Посчитайте угол между двумя векторами размерности N.
# Примечание: Вспомните определение скалярного произведения.
# Изначально вектор заполните рандомными числами.
# Пример: N =3
# вектор a = [0, 1, 0]
# вектор b = [1, 0, 0]
# Угол = 90
import random
from math import sqrt
from math import acos

def get_random_list(n):
    listr = []
    while(n>0):
        n-=1
        listr.append(int(random.random()*20-10))
    return listr
n = int(input('Enter a number: '))
a = get_random_list(n)
b = get_random_list(n)
print(a,"\n",b)
sum =0
for i in range(n):
    sum += a[i] * b[i]
mod_a = 0
mod_b = 0
for i in range(n-1):
    mod_a += sqrt(a[i] ** 2 + a[i + 1] ** 2)
    mod_b += sqrt(b[i] ** 2 + b[i + 1] ** 2)
alpha = acos((sum/mod_a)/mod_b)*180/3.1415926535897932384626433832795
print(alpha)

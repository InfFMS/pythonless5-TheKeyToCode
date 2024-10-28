# Напишите программу, которая удаляет дубликаты из списка длины N.
# Пример работы:
# Пример: ввод N = 8
# [10, 20, 10, 20, 30, 40, 30, 50]
# После удаления дублей:  [10, 20, 30, 40, 50]
def addif(l, a):
    for i in l:
        if i==a :
            return False
    l.append(a)
    return True
n = int(input('Enter a count of numbers: '))
l=[]
while n>0 :
    j = int(input('Enter a number: '))
    addif(l,j)
    n-=1
print(l)
# Введите массив длины N с клавиатуры и найдите (за один проход)
# количество элементов, имеющих максимальное значение.

n = int(input('Enter a count of number: '))
n-=1
m = int(input('Enter a number: '))
c = 1
while n>0 :
    i = int(input('Enter a number: '))
    if i > m :
        m = i
        c = 1
    elif i == m:
        c += 1
    n-=1
print("Max: ", m, ", Count: ", c)
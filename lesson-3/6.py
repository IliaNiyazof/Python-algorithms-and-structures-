# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным
# элементами. Сами минимальный и максимальный элементы в сумму не включать.

from random import random

arr = []
for i in range(10):
    arr.append(int(random()*10))
a = 0
b = max(arr)
c = min(arr)
arr.remove(b)
arr.remove(c)
for i in arr:
    a += i
print(a)
print(arr)
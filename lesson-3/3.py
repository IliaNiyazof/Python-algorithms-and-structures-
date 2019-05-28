# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import random

arr = []
for i in range(10):
    arr.append(int(random()*10))
    a = min(arr)
    b = max(arr)
print(arr)
print(a, b)
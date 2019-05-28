# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
# надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.
from random import random

arr = []
even = []
for i in range(15):
    arr.append(int(random() * 100))
    if arr[i] % 2 == 0:
        even.append(i)
print(arr)
print('Индексы четных элементов: ', even)
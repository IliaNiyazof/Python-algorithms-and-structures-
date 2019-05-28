# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
from random import random

arr = []
for i in range(10):
    arr.append(int(random() * 100) - 50)
    a = max(arr)

i = 0
index = -1
while i < 10:
    if arr[i] < 0 and index == -1:
        index = i
    i += 1

print(index, ':', arr[index])
print(arr)
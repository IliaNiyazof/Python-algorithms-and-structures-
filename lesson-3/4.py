# Определить, какое число в массиве встречается чаще всего
from random import random

N = 20
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 25)
print(arr)

num = arr[0]
max = 1
for i in range(N):
    frq = 1
    for k in range(i + 1, N):
        if arr[i] == arr[k]:
            frq += 1
    if frq > max:
        max = frq
        num = arr[i]

if max > 1:
    print(max, 'раз(а) встречается число', num)
else:
    print('Нету одинаковых')
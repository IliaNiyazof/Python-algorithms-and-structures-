# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный
# случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random
from memory_profiler import profile
# @profile

# list = [random.randint(1, 50) for i in range(5)]
list = [round(random.uniform(0, 50), 1) for i in range(5)]
print(list)

def merge(list):
    if len(list) <= 1:
        return list

    left = merge(list[:len(list) // 2])
    right = merge(list[len(list) // 2:])
    i, j = 0, 0

    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            list[i + j] = left[i]
            i += 1
        else:
            list[i + j] = right[j]
            j += 1

    while len(left) > i:
        list[i + j] = left[i]
        i += 1
    while len(right) > j:
        list[i + j] = right[j]
        j += 1

    return list

merge(list)
print(list)
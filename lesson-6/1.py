# Посчитать четные и нечетные цифры введенного натурального числа. Например,
# если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
from memory_profiler import profile
import sys
@profile
def f(a, event, odd):
    while a > 0:
        if a % 2 == 0:
            event += 1
        else:
            odd += 1
        a = a // 10
    return ("четных - %d, нечетных - %d" % (event, odd))
p = f(789,0,0)

@profile
def number(s, event, odd):
    if s == 0:
        return (('Четных чисел - %d' % event),('Нечётных чисел - %d' % odd))
    else:
        if s % 2 == 0:
            event += 1
            return (number(s // 10, event, odd))
        else:
            odd += 1
            return (number(s // 10, event, odd))
b = number(789,0,0)
print(b)

#как мы видим из работы, рекурсия занимает больше памяти, чем обычный цикл,
#это связано с тем, что в рекурсии мы несколько раз возращаем значения,
#что занимает некоторую облать памяти.
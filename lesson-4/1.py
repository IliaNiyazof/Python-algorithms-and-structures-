# Посчитать четные и нечетные цифры введенного натурального числа. Например,
# если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
# как вы видим из программы рекурсия работает дольше чем цикл(рекурсия - 2,56, цикл - 1,00)
# это связано с тем, что циклы используют для подсчета числа исполнений итератор,
# а рекурсивные функции для определения момента выхода должны выполнять сравнение результатов
import timeit

a = int(input('Ведите число: '))
event = odd = 0
def f(a, event, odd):
    while a > 0:
        if a % 2 == 0:
            event += 1
        else:
            odd += 1
        a = a // 10
print(timeit.timeit("f(a,event,odd)", setup="from __main__ import f,a,event,odd"))


s = int(input('Ведите число: '))
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
print(timeit.timeit("number(s,event,odd)", setup="from __main__ import number,s,event,odd"))

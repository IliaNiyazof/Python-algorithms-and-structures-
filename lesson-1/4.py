# Написать программу, которая генерирует в указанных пользователем границах
# случайное целое число,
# случайное вещественное число,
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
from random import random

a = int(input('Введите левое ограничение: '))
b = int(input('Введите правое ограничение: '))
c = int(random() * (a+b))
print(c)

a = float(input('Введите левое не целое ограничение: '))
b = float(input('Введите правое не целое ограничение: '))
c = random() * (a+b)
print(c)

a = ord(input('Введите символ левого ограничения: '))
b = ord(input('Введите символ правого ограничения: '))
c = int(random() * (b-a)) + a
print(chr(c))

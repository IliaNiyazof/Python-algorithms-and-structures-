import collections
import functools

number = collections.defaultdict(list)
for i in range(2):
    b = input("Введите %i-е натуральное шестнадцатиричное число: " % (i+1))
    number["%a-%a" % (i+1, b)] = list(b)
print(number)

sum = sum([int(''.join(i), 16) for i in number.values()])
print("Сумма: ", list('%a' % sum))

mult = functools.reduce(lambda a, b: a * b, [int(''.join(i), 16) for i in number.values()])
print("Произведение: ", list('%a' % mult))

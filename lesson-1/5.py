# Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

a = ord(input('1-я буква: '))
b = ord(input('2-я буква: '))
a = a - ord('a') + 1
b = b - ord('b') + 2
print('Позиции: {} и {}'.format(a, b))
print('Между буквами символов:', abs(a - b))

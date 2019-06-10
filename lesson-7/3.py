import random
a = 4
size = 2 * a + 1
lst3 = [random.randint(1, 50) for i in range(size)]

print(f'Исходный НЕотсортированный список:\n {lst3}\n')


def median(lst):
    # нахождение медианы для четного кол-ва элементов
    if len(lst) % 2 == 0:
        center = []

        for i in lst:
            b = 0

            for j in lst:

                if i < j:
                    b += 1

            if len(lst) == b * 2 + 2 or len(lst) == b * 2:
                center.append(i)
        return sum(center) / 2

    # нахождение медианы для НЕ четного кол-ва элементов
    if len(lst) % 2 != 0:
        for i in lst:
            num = i
            b = 0

            for j in lst:

                if i < j:
                    b += 1

            if len(lst) == 2 * b + 1:
                return num


print(f'Медиана НЕотсортированного списка: {median(lst3)}\n')

print(f'Отсортированный список: \n{sorted(lst3)}')
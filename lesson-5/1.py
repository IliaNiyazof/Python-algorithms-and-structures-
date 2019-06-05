import collections
n = int(input("Введите количество предприятий для расчета прибыли: "))
d = dict()
a = 1
for i in range(n):
    name = input("Введите название предприятия: ")
    money = input("через пробел введите прибыль предприятия\n"
               "за каждый квартал(Всего 4 квартала): ")
    moneys = money.split(" ")
    d[name] = moneys
    a += 1
    print()

pred = collections.Counter(d)

pr = []
b = 0
t = 0
for i in pred:
    sum = 0
    for j in pred[i]:
        sum += int(j)
    pred[i] = sum
    t += sum
    b += 1
sec = t / b

print("Средняя годовая прибыль всех предприятий: " + str(sec))

big = []
small = []
for i in pred:
    if int(pred[i]) >= sec:
        big.append(i)
    else:
        small.append(i)
print("Предприятия, у которых прибыль выше среднего: ", end="")
for i in big:
    print(i, end=" ")
print()
print("Предприятия, у которых прибыль ниже среднего : ", end="")
for i in small:
    print(i, end=" ")
print()

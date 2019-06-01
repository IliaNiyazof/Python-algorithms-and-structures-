import timeit
def number(i):
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_number = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_number = False
                break
            t += 1
        if is_number:
            if count == i:
                break
            count += 1
        n += 1
    return n

print(number(1000))

def eratosfen(i):
    n = 2
    l = 10000
    s = [x for x in range(l)]
    while n < 1:
        if s[n] != 0:
            m = n*2
            while m < 1:
                s[m] = 0
                m += n
        n += 1
    return[p for p in s if p != 0][i - 1]

i = 1000

print(timeit.timeit("number(i)", setup="from __main__ import number,i", number=100))
print(timeit.timeit("eratosfen(i)", setup="from __main__ import eratosfen,i", number=100))

'''
для поиска 10 - го числа
простое - 0,005
решето - 0,23
для поиска 100 - го числа
простое - 0,79
решето - 0,13
для поиска 1000 - го числа
простое - 98,71
решето - 0,19

Решето лучше подходит для поиска больших чисел, так как он отбрасывает ненужные числа и не проверяет их,
а цикл проверяет каждое число 

'''
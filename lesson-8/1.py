# взял за пример вашу программу. Доработал код, теперь можно вводить буквы в любом регистре,
# они будут переводиться в нижний, и повторяющиеся буквы больше не будут повторяться, лишь те которых нету
# так же та подстрока которая будет имет длину 3 будет переводиться в кодировку Хаффмана
# получилось много вложенных if немного мешает чтению кода.
import hashlib
string = input("Введите строку из латинских букв: ").lower()
r = set()
b = []
length = len(string)
for i in range(length):
    if i == 0: # проверка N
        N = len(string) - 1
    else:
        N = len(string)

    for j in range(N, i, -1):
        if (string[i:j]) not in r:
            r.add(string[i:j]) # добавляю подстроку в r
            print(string[i:j])
            if len(string[i:j]) == 3: # условие записи в кодировку
                b.append(hashlib.sha1(string[i:j].encode('utf-8')).hexdigest())
print(b)
print(r)
print("Количество различных подстрок в строке '%string' равно %d" % (string, len(r)))

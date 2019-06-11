# Закодируйте любую строку из трех слов по алгоритму Хаффмана.
import hashlib
a = input("Ведите строку из трех слов: ")
print(hashlib.sha1(b'{a}').hexdigest())
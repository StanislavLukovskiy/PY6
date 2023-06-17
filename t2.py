# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)


n = int(input("Введите количество элементов: "))
n_min = int(input("Введите минимальное значение: "))
n_max = int(input("Введите максимальное значение: "))

from random import randint
list_1 = [randint(-1, 10) for i in range(n)]
print(list_1)

list_2 = [i for i in range(len(list_1)) if n_min <= list_1[i] <= n_max]
print(list_2)
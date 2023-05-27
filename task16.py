# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1
import random

n = int(input('enter n: '))
list = []
for i in range(n):
    list.append(random.randint(1, n))
print(list)
x = int(input("enter x: "))
count = 0
for j in range(n):
    if list[j] == x:
        count += 1
print(count)
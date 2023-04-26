# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint
a = int(input("Введите количество чисел в строке: "))
numbers = []
for i in range(a):
    numbers.append(randint(1, 10))
n = int(input("Введите число: "))
min = abs(n - numbers[0])
index = 0
for i in range(1, a):
    count = abs(n - numbers[i])
    print(count)
    if count < min:
        min = count
        index= i
print(f"Число {numbers[index]} в списке наиболее близко по величине к числу {n}")


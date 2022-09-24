# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

from math import prod

def coordinati():
    result = [0, 0]
    print(prod(result))
    while not prod(result):
        result[0] = int(input('Введите координату х: '))
        result[1] = int(input('Введите координату y: '))
    return result

def findQuarter(array):
    if array[0] * array[1] > 0:
        if array[0] > 0: print(1)
        else: print(3)
    else:
        if array[0] > 0: print(4)
        else: print(2)

findQuarter(coordinati())

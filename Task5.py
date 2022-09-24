# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def intCoord():
    coord = [0,0]
    coord[0] = int(input('Введите х: '))
    coord[1] = int(input('Введите y: '))
    return coord

def findDist(a,b):
    sum = 0
    for i in range(len(a)):
        sum += (a[i] - b[i]) ** 2
    sum = sum ** (0.5)
    return sum

print(round(findDist(intCoord(), intCoord()), 2))




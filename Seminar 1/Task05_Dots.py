# Напишите программу, которая принимает на вход координаты двух точек
#  и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

def distance(list_a: list, list_b: list) -> float:
    return math.sqrt((list_a[0] - list_b[0])**2 + (list_a[1] - list_b[1])**2)

print('Введите координаты точки А:')
A = [int(input()) for i in range(0,2)]
print('Введите координаты точки В:')
B = [int(input()) for i in range(0,2)]
print(f'Расстояние между точками: {round(distance(A, B), 2)}')
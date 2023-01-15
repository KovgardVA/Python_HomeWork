# Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл 
# многочлен степени k.

from random import randint
from polynom import fill

k = int(input('Введите натуральную степень многочлена: '))
fill(k, 'poly.txt')

# k = int(input())
# result = ''

# for i in range(k, -1, -1):
#     coef = randint(0, 100)
#     if coef == 0:
#         continue
#     if coef == 1:
#         if i == 1:
#             result += 'X + '
#         elif i == 0:
#             result += f'{coef} '
#         else:
#             result += f'X**{i} + '
#     else:
#         if i == 1:
#             result += f'{coef}*X + '
#         elif i == 0:
#             result += f'{coef} '
#         else:
#             result += f'{coef}*X**{i} + '
# result += '= 0'
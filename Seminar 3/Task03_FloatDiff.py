# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.

my_list = [1.1, 1.2, 3.1, 5, 10.01]
float_list = []

for i in my_list:
    if isinstance(i, float):
        float_list.append(i - int(i))

print \
    (
        'Список:', my_list,
        '\nРазница между максимальным и минимальным значением дробной части:',
        round(max(float_list) - min(float_list), 2)
    )

import random

# def fract(num):
#     return round(num % 1, 2)
# list_num = list(map(fract, list_num))
# Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.

from random import randint

list_num = [randint(0,5) for i in range(randint(5,10))]
list_unique = []

for i in list_num:
    if i not in list_unique:
        list_unique.append(i)

print(f'В нашем списке: {list_num} -\
    \nимеются данные неповторяющиеся элементы: {list_unique}')

# for i in list_num:
#     if list_num.count(i) == 1:
#         list_unique.append(i)
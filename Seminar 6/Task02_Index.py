# Определить индексы элементов массива (списка), значения которых 
# принадлежат заданному диапазону (т.е. не меньше заданного минимума 
# и не больше заданного максимума)

# list_num = [int(input()) for i in range(5)]  # Ручной ввод
list_num = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_num = int(input('Задайте минимальное значение: '))
max_num = int(input('Задайте максимальное значение: '))
list_indx = []

for index, value in enumerate(list_num):
    if min_num <= value <= max_num:
        list_indx.append(index)
print(list_indx)
# Задайте список из нескольких чисел. Напишите программу, которая найдёт 
# сумму элементов списка, стоящих на нечётной позиции.

# from random import randint

# list_num = [randint(0,20) for i in range(randint(5,10))]
my_list = [2, 3, 5, 9, 3]
odd_sum = 0

for i in range(1, len(my_list) - 1, 2):
    odd_sum += my_list[i]

print \
    (
        f'Наш список: {my_list}'
        f'\nСумма элементов списка, стоящих на нечетных позициях : {odd_sum}'
    )
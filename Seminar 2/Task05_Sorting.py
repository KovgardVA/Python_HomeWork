# Реализуйте алгоритм перемешивания списка.

import random

def sorting(list_to_sort):
    for i in range(list_length):
        temp = 0
        first_index = random.randint(0, list_length - 1)
        second_index = random.randint(0, list_length - 1)
        if first_index != second_index:
            temp = list_to_sort[first_index]
            list_to_sort[first_index] = list_to_sort[second_index]
            list_to_sort[second_index] = temp
    return list_to_sort

min_number = -10
max_number = 10
list_length = 10

list = [random.randint(min_number, max_number) for i in range(list_length)]
print(list)

print(sorting(list))
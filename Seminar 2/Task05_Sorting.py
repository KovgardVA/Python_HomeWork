# Реализуйте алгоритм перемешивания списка.

import random

def sorting(list_to_sort):
    for i in range(list_length):
        first_index = random.randint(0, list_length - 1)
        second_index = random.randint(0, list_length - 1)
        if first_index != second_index:
            list_to_sort[first_index], list_to_sort[second_index] = list_to_sort[second_index], list_to_sort[first_index]
    return list_to_sort

min_number = -10
max_number = 10
list_length = 10

list_num = [random.randint(min_number, max_number) for i in range(list_length)]
print(list_num)

print(sorting(list_num))

# random.shuffle(list_num)

# def random_num(max_num):
#     random_num = datetime.datetime.now().microsecond / 10**6
#     return random_num * max_num

# print(datetime.datetime.now().microsecond)
# for i in range(len(list_num) - 1, -1, -1):
#     j = int(random_num(i + 1))
#     list_num[i], list_num[j] = list_num[j], list_num[i]
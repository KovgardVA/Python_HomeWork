# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

my_odd_list = [2, 3, 4, 5, 6]
my_even_list = [2, 3, 5, 6]

def product_pair(array):
    product_list = []
    i = 0
    while i < -(-len(array) // 2):
        product_list.append(array[i] * array[len(array) - 1 - i])
        i += 1
    return product_list

print \
    (
        'В нечетном списке:', my_odd_list,
        'Произведение пар чисел:', product_pair(my_odd_list),
        'В нечетном списке:', my_even_list,
        'Произведение пар чисел:', product_pair(my_even_list), sep='\n'
    )
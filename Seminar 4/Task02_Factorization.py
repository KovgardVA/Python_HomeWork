# Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N.

def factorization(num):
    fact_list = []
    simple_num = 2
    while simple_num <= int(num**0.5):
        while num % simple_num == 0:
            fact_list.append(simple_num)
            num //= simple_num
        simple_num += 1
    if num > 1:
        fact_list.append(num)
    return fact_list

n = int(input('Введите натуральное число: '))
n_list = factorization(n)
print(f'Разложение числа на простые множители: {n_list}')

# Простым называется натуральное число, которое делится только на единицу и на себя.

# Eсли число N равно произведению двух других, то одно из них не больше корня из N,
# а другое не меньше корня из N.
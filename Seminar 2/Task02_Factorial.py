# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

def input_number(input_text):
    is_number = False
    while not is_number:
        try:
            number = int(input(f"{input_text}"))
            is_number = True
        except ValueError:
            print('Ошибка. Требуется ввод числа')
    return number

def factorial(number):
    list_num = [1]
    for i in range(2, number + 1):
        list_num.append(i * list_num[i - 2])
    return list_num

num = input_number('Введите число: ')
print(factorial(num))
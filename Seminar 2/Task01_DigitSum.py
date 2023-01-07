# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

def digitSum(num):
    sum = 0
    for i in num:
        if i != '.' and i != '-':
            sum += int(i)
    return sum

number = input('Введите число: ')
print(f'Сумма всех цифр числа: {digitSum(number)}')

# for i in num:
#     if i.isdigit():
#         sum += int(i)

# num = float(input())
# len_num = len(str(num))
# while num != int(num):
#     num = round(num * 10, len_num)
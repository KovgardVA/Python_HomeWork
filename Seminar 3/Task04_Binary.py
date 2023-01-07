# Напишите программу, которая будет преобразовывать десятичное число 
# в двоичное.

num = int(input('Введите целое число: '))
binary_list = []
binary_num = 0

while num > 0:
    binary_list.append(num % 2)
    num //= 2
for i in range(len(binary_list) - 1, -1, -1):
    binary_num *= 10
    binary_num += binary_list[i]

print('Число в двоичной системе:', binary_num)

# def dec_to_bin(num, result = ''):
#     if num == 0:
#         return result[::-1]
#     result += str(num % 2)
#     return dec_to_bin(num // 2, result)

# print(bin(n)[2:])
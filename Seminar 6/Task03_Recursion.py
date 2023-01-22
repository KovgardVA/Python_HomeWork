# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
def exp(num, pow):
    if pow == 1: return num
    if pow == 0: return 1
    return num*exp(num, pow - 1)

number = int(input('Введите число: '))
power = int(input('Введите степень: '))
result = exp(number, power)
print(f'{number} в степени {power} равняется {result}.')
# Вычислить число c заданной точностью d
# 10^{-1} ≤ d ≤10^{-10}

from math import pi

max_accuracy = -1
min_accuracy = -10

def power_num(num):
    for i in range(max_accuracy, min_accuracy - 1, -1):
        if 10**i == num:
            return -i

d = float(input('Задайте точность: '))
print('Число Пи с заданной точность', d, '=', round(pi, power_num(d)))

# n = input()
# length = len(n.split('.')[1])
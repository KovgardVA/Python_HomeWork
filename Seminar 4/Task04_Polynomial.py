# Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл 
# многочлен степени k.

from random import randint

k = int(input('Введите натуральную степень многочлена: '))
k_list = [randint(0,100) for i in range(k + 1)]
last_k = len(k_list)

path = 'poly.txt'
data = open(path, 'w')

for i in range(last_k, 0, -1):
    if i == 2:
        if k_list[last_k - i] != 0:
            data.writelines(f'{k_list[last_k - i]}*X ')
            if k_list[last_k - i + 1] != 0:
                data.writelines('+ ')
    elif i == 1:
        if k_list[last_k - i] != 0:
                data.writelines(f'{k_list[last_k - i]} ')
        data.writelines('= 0')
    else:
        if k_list[last_k - i] != 0:
            data.writelines(f'{k_list[last_k - i]}*X^{i - 1} ')
            if k_list[last_k - i + 1] != 0:
                data.writelines('+ ')

data.close()

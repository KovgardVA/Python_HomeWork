# Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл 
# многочлен степени k.

from random import randint

def fill_poly(file, coef):

    k_list = [randint(0,100) for i in range(coef + 1)]
    last_k = len(k_list)

    data = open(file, 'w')

    for i in range(last_k, 0, -1):
        number = k_list[last_k - i]
        if i == 2:
            if number != 0:
                data.writelines('X ' if number == 1 else f'{number}*X ')
                if k_list[last_k - i + 1] != 0:
                    data.writelines('+ ')
        elif i == 1:
            if number != 0:
                    data.writelines(f'{number} ')
            data.writelines('= 0')
        else:
            if number != 0:
                data.writelines('X^{i - 1} ' if number == 1 else f'{number}*X^{i - 1} ')
                if k_list[last_k - i + 1] != 0:
                    data.writelines('+ ')

    data.close()

fill_poly('poly.txt', int(input('Введите натуральную степень многочлена: ')))
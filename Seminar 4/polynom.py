from random import randint
import re

# Запись в файл многочлена с заданной степенью
def fill(power, file):
    k_list = [randint(0,100) for i in range(power + 1)]
    last_k = len(k_list) # Индекс крайнего члена для обратной сборки
    data = open(file, 'w')
    for i in range(last_k, 0, -1):
        number = k_list[last_k - i] # Коэффициент
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
                data.writelines('X**{i - 1} ' if number == 1 else f'{number}*X**{i - 1} ')
                if k_list[last_k - i + 1] != 0:
                    data.writelines('+ ')
    data.close()

# Запись в файл многочлена с заданными коэффициентами
def write(coef, file):
    data = open(file, 'w')
    for i in coef:
        number = i[0]
        exp = i[1]
        if exp == 1:
            data.writelines('X ' if number == 1 else f'{number}*X + ')
        elif exp == 0:
            data.writelines(f'{number} ')
        else:
            data.writelines('X**{i - 1} ' if number == 1 else f'{number}*X**{exp} + ')
    data.writelines('= 0')
    data.close()
        
# Чтение многочлена с файла
def read(path):
    data = open(path, 'r')
    line = data.readline()
    data.close()
    return line

# Кортеж (коэффициент, степень)
def coef(line):
    sep_null = -3 # Отрезаем '= 0'
    line = re.sub('[*]', ' ', line[:sep_null]).split('+') # Список всех иксов
    line = [char.split() for char in line] # (коэффициент, Х, степень)
    for i in line: # Для Х**1 добавляем 1, для X**0 добавляем 0
        if i[0] == 'X': i.insert(0, 1)
        if i[-1] == 'X': i.append(1)
        if len(i) == 1: i.append(0)
    line = [tuple(int(x) for x in j if x != 'X') for j in line] # Формируем кортеж
    return line

# Сумма 
def sum(first_coef, second_coef):
    temp = [0] * (max(first_coef[0][1], second_coef[0][1]) + 1)
    for i in first_coef + second_coef:
        temp[i[1]] += i[0]
    result = [(temp[i], i) for i in range(len(temp)) if temp[i] != 0]
    result.sort(key = lambda r: r[1], reverse= True) # Разворот
    return result
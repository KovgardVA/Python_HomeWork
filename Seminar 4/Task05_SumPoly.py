# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

import polynom

first_file = 'poly_1.txt'
second_file = 'poly_2.txt'
sum_file = 'sum.txt'
poly_power = [3, 2]

# Создаем файлы с рандомными многочленами
polynom.fill(poly_power[0], first_file)
polynom.fill(poly_power[1], second_file)

# Считываем многочлены с файла и вытаскиваем оттуда коэффициенты
first_poly = polynom.coef(polynom.read(first_file))
second_poly = polynom.coef(polynom.read(second_file))
# Суммируем подобные коэффициенты
sum_poly = polynom.sum(first_poly, second_poly)
# Записываем новый многочлен в файл
polynom.write(sum_poly)
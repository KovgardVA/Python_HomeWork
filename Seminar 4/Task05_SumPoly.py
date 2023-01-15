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


# pol1 = '12*x**8 + 2*x**6 + 2*x**4 + 3*x**3 + 2*x**2 + 3'
# pol2 = '34*x**25 + 20*x**1 + 10*x**7 + 8*x**4 + 1*x**3 + 6*x**1 + 5'

# pol1 = pol1.split('+')
# pol2 = pol2.split('+')

# for i, val in enumerate(pol1):
#     pol1[i] = list(map(int, val.split('*x**')))
# for i, val in enumerate(pol2):
#     pol2[i] = list(map(int, val.split('*x**')))

# result = pol1 + pol2
# result = sorted(result, key=lambda x: x[1] if len(x) > 1 else 0, reverse=True)

# cur_indx = 0
# result_list = []
# while cur_indx < len(result) - 1:
#     cur_num = result[cur_indx]
#     next_num = result[cur_indx + 1]
#     if len(cur_num) > 1 and len(next_num) > 1:
#         if cur_num[1] == next_num[1]:
#             sum_coef = cur_num[0] + next_num[0]
#             result_list.append([sum_coef, cur_num[1]])
#             cur_indx += 1
#         else:
#             result_list.append(result[cur_indx])
#     elif len(cur_num) > 1 and len(next_num) == 1:
#         result_list.append(result[cur_indx])
#     elif len(cur_num) == 1 and len(next_num) == 1:
#         result_list.append([cur_num[0] + next_num[0]])
#         cur_indx += 1
#     cur_indx += 1
# if cur_indx < len(result):
#     result_list.append(result[-1])
# Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

num = int(input('Введите первое число прогрессии: '))
d = int(input('Введите разность между членами прогрессии: '))
amount = int(input('Введите количество элементов прогрессии: '))

arif_prog = [num + i * d for i in range(amount)]
print('Получившаяся прогрессия: ', end='')
for i in arif_prog: print(i, end=' ')
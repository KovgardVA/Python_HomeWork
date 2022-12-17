# Напишите программу, которая принимает на вход координаты точки (X и Y),
#  причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#  в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def check_coords(int_x, int_y) -> bool:
    if (int_x != 0 and int_y !=0): return True
    else: return False

def check_quater(int_x, int_y):
    if int_x > 0 and int_y > 0: return 1
    elif int_x < 0 and int_y > 0: return 2
    elif int_x < 0 and int_y < 0: return 3
    else: return 4

x = int(input('Введите координату X: '))
y = int(input('Введите координату Y: '))
if check_coords(x, y):
    quater = check_quater(x, y)
    print(f'Координаты находятся в четверти под номером {quater}.')
else: print('Вы ввели начало координат!')
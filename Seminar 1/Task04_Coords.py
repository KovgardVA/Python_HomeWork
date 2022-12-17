import math

def check_quater(int_quater: int) -> bool:
    if (0 < int_quater < 5): return True
    else: return False

def coords_range(int_quater):
    if int_quater == 1:
        x_range = [0, math.inf]
        y_range = [0, math.inf]
    elif int_quater == 2:
        x_range = [-math.inf, 0]
        y_range = [0, math.inf]
    elif int_quater == 3:
        x_range = [-math.inf, 0]
        y_range = [-math.inf, 0]
    else:
        x_range = [0, math.inf]
        y_range = [-math.inf, 0]
    return x_range, y_range

quater = int(input('Введите номер четверти: '))
if check_quater(quater):
    print(f'X ∈ {coords_range(quater)[0]}, Y ∈ {coords_range(quater)[1]}')
else: print('Такой четверти не существует')
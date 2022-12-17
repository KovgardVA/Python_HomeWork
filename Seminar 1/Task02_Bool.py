# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z)
#  = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def predicat(int_x, int_y, int_z) -> bool:
    if not(int_x or int_y or int_z) == (not int_x and not int_y and not int_z):
        return True
    else: return False


for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            print(f'{x} {y} {z} -- {predicat(x, y, z)}')
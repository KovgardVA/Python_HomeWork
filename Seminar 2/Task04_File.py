# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях.
#   Позиции хранятся в файле file.txt в одной строке одно число.

my_number = 5
product = 1
list = []

for i in range(-my_number, my_number + 1):
    list.append(i)
print(f'Наш массив: \n{list}')

path = 'file.txt'
data = open(path, 'r')
for line in data:
    product *= list[int(line)]
data.close()
print(f'Произведение: \n{product}')
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях.
#   Позиции хранятся в файле file.txt в одной строке одно число.

my_number = 5
product = 1
list_num = []

for i in range(-my_number, my_number + 1):
    list_num.append(i)
print(f'Наш массив: \n{list_num}')

path = 'file.txt'
data = open(path, 'r')
for line in data:
    product *= list_num[int(line)]
data.close()
print(f'Произведение: \n{product}')

# list_num = [i for i in range(-n,n+1)]

# file = open('file.txt', 'r')
# a = file.readlines()
# print(a)
# for i in range(len(a)):
#     a[i] = int(a[i].strip())
# print(a)
# list_num = list(map(str.strip, a))
# print(list_num)
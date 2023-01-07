# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ 
# и выведите на экран их сумму.

max_number = 4
dictionary = {}
sum = 0

for i in range (1, max_number + 1):
    dictionary[i] = round((1 + 1/i)**i, 2)
    sum += dictionary[i]

print(dictionary, sum, sep='\n')
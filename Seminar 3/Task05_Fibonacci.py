# Задайте число. Составьте список чисел Фибоначчи, в том числе для 
# отрицательных индексов.

def fibonacci(num):
    fib = [0]
    for i in range(1, num + 1):
        if i == 1:
            fib.append(1)
        else:
            fib.append(fib[i - 1] + fib [i - 2])
    return fib

def negafibonacci(num):
    fib_list = fibonacci(num)
    nega_fib_list = []
    for i in range(num):
        nega_fib_list.append((-1)**(i)*fib_list[i + 1])
    nega_fib_list.reverse()
    nega_fib_list.extend(fib_list)
    return nega_fib_list

num = int(input('Введите число: '))
print(negafibonacci(num))

# def positive_fib(n):
#     positive_list = [0, 1]
#     for i in range(n - 1):
#         positive_list.append(positive_list[-2] + positive_list[-1])
#     return positive_list

# def negative_fib(n):
#     negative_list = [0, 1]
#     for i in range(n - 1):
#         negative_list.append(negative_list[-2] - negative_list[-1])
#     return negative_list

# numbers = negative_fib(num)[::-1] + positive_fib(num)[1:]
# RLE алгоритм:

def rle_encode(data):
    '''Модуль сжатия данных'''
    rle = ''
    counter = 1
    for i in range(1, len(data)):
        if data[i] != data[i - 1]:
            rle += str(counter) + data[i - 1]
            counter = 1
        else:
            counter += 1
    else:
        rle += str(counter) + data[i]
    return rle

def rle_decode(rle):
    '''Модуль восстановления данных'''
    data = ''
    for i in range(1, len(rle), 2):
        data += rle[i]*int(rle[i-1])
    return data

data = input('Введите данные для сжатия: ')
rle = rle_encode(data)
print(f'Сжатые данные: {rle}')
print(f'Восстановленные данные: {rle_decode(rle)}')
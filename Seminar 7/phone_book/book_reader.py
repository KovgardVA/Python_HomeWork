def read_info():
    with open('phone_book.csv', 'r') as file:
        for str in file:
            print(str, end='')

def read_name():
    temp = []
    with open('phone_book.csv', 'r') as file:
        for str in file:
            temp.append(str.split(';'))
    for i in temp:
        print(i[1], i[2])
def read_info():
    with open('phone_book.csv', 'r') as file:
        for str in file:
            print(str)
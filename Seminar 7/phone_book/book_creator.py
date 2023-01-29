import data_provider as prov

def add_id():
    data = prov.get_id()
    with open('phone_book.csv', 'a') as file:
        file.writelines('{};'.format(data))

def add_name():
    data = prov.get_name()
    with open('phone_book.csv', 'a') as file:
        file.writelines('{};'.format(data))

def add_surname():
    data = prov.get_surname()
    with open('phone_book.csv', 'a') as file:
        file.writelines('{};'.format(data))

def add_phone():
    data = prov.get_phone()
    with open('phone_book.csv', 'a') as file:
        file.writelines('{};'.format(data))

def add_comment():
    data = prov.get_comment()
    with open('phone_book.csv', 'a') as file:
        file.writelines('{}\n'.format(data))

def add_info():
    add_id()
    add_name()
    add_surname()
    add_phone()
    add_comment()
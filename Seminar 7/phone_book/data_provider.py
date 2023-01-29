def get_id():
    id = ''
    while not id.isdigit():
        id = input('Введите индентификационный номер: ')
    return int(id)

def get_name():
    name = ''
    while not name.isalpha():
        name = input('Введите имя: ')
    return name.title()

def get_surname():
    surname = ''
    while not surname.isalpha():
        surname = input('Введите фамилию: ')
    return surname.title()

def get_phone():
    phone = ''
    while not phone.isdigit():
        phone = input('Введите номер телефона: ')
    return phone

def get_comment():
    return input('Введите комментарий: ')
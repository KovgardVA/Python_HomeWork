def get_string(comment):
    temp = ''
    while not temp.isalpha():
        temp = input(comment)
    return temp.title()

def get_num(comment):
    num = ''
    while not num.isdigit():
        num = input(comment)
    return num

def is_in(data, file):
    if data in file: return True
    else: return False

def new_data(text, checking_file):
    data = ''
    while not is_in(data, checking_file):
        data = input(text)
    return data

def action_menu(menu):
    print(menu)
    num = int(input('Введите желаемое действие: '))
    return num

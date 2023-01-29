import user_interface as ui

def add_info():
    data = ''
    data += str(ui.get_num('Введите индентификационный номер: ')) + ';'
    data += str(ui.get_string('Введите имя: ')) + ';'
    data += str(ui.get_string('Введите фамилию: ')) + ';'
    data += str(ui.get_num('Введите номер телефона: ')) + ';'
    data += str(ui.get_string('Введите комментарий: ')) + '\n'
    with open('phone_book.csv', 'a') as file:
        file.write(data)
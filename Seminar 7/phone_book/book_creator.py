import data_provider as prov

def add_info():
    data = ''
    data += str(prov.get_id()) + ';'
    data += str(prov.get_name()) + ';'
    data += str(prov.get_surname()) + ';'
    data += str(prov.get_phone()) + ';'
    data += str(prov.get_comment()) + '\n'
    with open('phone_book.csv', 'a') as file:
        file.write(data)
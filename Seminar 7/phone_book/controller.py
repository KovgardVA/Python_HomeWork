import book_creator as bw
import book_reader as br
import user_interface as ui

NAME = 1
ID = 0

def button():
    if ui.mode_question():
        while ui.user_question('Желаете начать заполнение?\n(y/n): '):
            bw.add_info()
        if ui.user_question('Желаете провести сортировку?\n(y/n): '):
            br.phone_book_sort(mode= ID)
            br.read_info('sorted_book.csv')
    else: 
        if ui.user_question('Желаете вывести только имя и фамилию?\n(y/n): '):
            br.read_name()
        else: br.read_info('phone_book.csv')
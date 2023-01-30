import module as m
from view import action_menu
from data_provider import menu

func_dict = {
        0: exit,
        1: m.show_student,
        2: m.show_mark,
        3: m.add_student,
        4: m.add_subject,
        5: m.add_mark
    }

def execute(command):
    return func_dict[command]()

def console_menu():
    while True:
        action = action_menu(menu)
        execute(action)
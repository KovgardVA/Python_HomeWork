def user_question(text):
    action = None
    while action not in ('y', 'n'):
        action = input(text).lower()
    if action == 'y': return True
    else: return False

def mode_question():
    mode = None
    while mode not in ('r', 'w'):
        mode = input('Желаете заполнить или прочитать файл?\n(w/r): ').lower()
    if mode == 'w': return True
    else: return False
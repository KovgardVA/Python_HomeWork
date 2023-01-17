# Игра в крестики-нолики:

from random import randint

def instruction():
    '''Выводит на экран инструкцию для игрока.'''
    print(
'''Добро пожаловать в игру "Крестики-нолики"!\n
В данной игре Вы сразитесь с компьютером за право победителя, поочередно
ставя крестик или нолик на поле 3 на 3. Для победы требуется составить
линию из трех элементов. Чтобы сделать ход, введите число от 0 до 8.\n
Числа соответствуют полям доски:
         0 | 1 | 2 
        -----------
         3 | 4 | 5 
        -----------
         6 | 7 | 8 \n'''
    )

def ask_yes_no(question):
    '''Задает вопрос да или нет в соответствии с вопросом.'''
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    '''Просит ввести число из диапозона.'''
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def first_move():
    '''Определяет, кто ходит первым с помощью кубика.'''
    human, computer = 0, 0
    input('Нажмите Enter, чтобы бросить кубик и определить первый ход...')
    while human == computer:
        human = randint(1, 6)
        computer = randint(1, 6)
        if human == computer:
            print(f'\nВаш бросок: {human}, бросок компьютера: {computer}')
            input('Ой, ничья! Нажмите Enter, чтобы перебросить...')
        elif human > computer:
            print(f'\nВаш бросок: {human}, бросок компьютера: {computer}')
            print('Первый ход за Вами! Вы играете крестиками.')
            human, computer = X, O
        elif computer > human:
            print(f'\nВаш бросок: {human}, бросок компьютера: {computer}')
            print('Первый ход за компьютером! Вы играете ноликами.')
            human, computer = O, X
    return human, computer

def new_board():
    '''Создает новую игровую доску.'''
    board = []
    for field in range(NUM_FIELDS):
        board.append(EMPTY)
    return board

def display_board(board):
    '''Отображает игровую доску.'''
    print('\n\t', board[0], '|', board[1], '|', board[2])
    print('\t', '-' * 9)
    print('\n\t', board[3], '|', board[4], '|', board[5])
    print('\t', '-' * 9)
    print('\n\t', board[6], '|', board[7], '|', board[8], '\n')

def legal_moves(board):
    '''Создает список доступных ходов.'''
    moves = []
    for field in range(NUM_FIELDS):
        if board[field] == EMPTY:
            moves.append(field)
    return moves

def winner(board):
    '''Определяем победителя.'''
    WAYS_TO_WIN = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7),\
        (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board [row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None

def human_move(board, human):
    '''Получаем ход игрока.'''
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number('Твой ход. Выберите одно из полей от 0 до 8: ',\
            0, NUM_FIELDS)
        if move not in legal:
            print('Ой, это поле уже занято! Выберете другое...\n')
    return move

def computer_move(board, computer, human):
    '''Алгоритм хода компьютера'''
    board = board[:] # локальяная копия
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print('Компьютер выбирает номер: ', end='')
    # Если следующий ход победный
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
    # Если в следующий ход победит игрок
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY
    # В остальных случаях
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

def next_turn(turn):
    '''Чередование хода.'''
    if turn == X: return O
    else: return X

def congrat_winner(the_winner, computer, human):
    '''Конец программы. Определение победителя или объявление ничьей.'''
    if the_winner != TIE:
        print(f'Три {the_winner} в ряд!\n')
    else: print('Ничья!')
    if the_winner == computer:
        print('Увы, Вас победил компьютер :-(')
    elif the_winner == human:
        print('Поздравляем с победой над компьютером!')

def main():
    instruction()
    if ask_yes_no('Желаете начать игру? (Y/N)\n') == 'n':
        print('\nОчень жаль, сыграем в следующий раз...')
        return None
    human, computer = first_move()
    turn = X # Первым ходит крестик
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

X = 'X'
O = 'O'
EMPTY = ' '
TIE = 'Ничья'
NUM_FIELDS = 9

main()
input('\n\nНажмите Enter, чтобы продолжить...')
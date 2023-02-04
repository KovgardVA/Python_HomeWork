from random import randint

student_list = \
    {'Vlad Sorokin' :\
        {'Biology' : '5', 'Chemistry' : '', 'Physics' : '5'},\
    'Anna Ivanova' :\
        {'Biology' : '', 'Chemistry' : '3', 'Physics' : '4'},\
    'Nikolay Novikov' :\
        {'Biology' : '4 3', 'Chemistry' : '3', 'Physics' : '2 4'}
    }

subject_list = ['Biology', 'Chemestry', 'Physics', 'Math', 'English', 'GYM', 'History', 'Economy', 'Russian']

menu = ('| 0. Выход | 1. Просмотр списка учеников | 2. Просмотр оценок | 3. Добавление ученика | 4. Добавление предмета | 5. Добавление оценки |')
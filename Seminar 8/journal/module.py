from view import get_num, get_string, new_data
from data_provider import student_list, subject_list

def add_student():
    global student_list
    global subject_list
    name = get_string('Введите имя ученика: ')
    surname = get_string('Введите фамилию ученика: ')
    full = name + ' ' + surname
    student_list[full] = dict.fromkeys(subject_list, '')
    return student_list

def show_student():
    global student_list
    print('\n')
    for i in student_list:
        print(i)
    print('\n')

def show_subject():
    global subject_list
    print('\n')
    for item in subject_list:
        print(item, end=' ')
    print('\n')

def add_subject():
    global student_list
    global subject_list
    subj = get_string('Введите название предмета: ')
    subject_list.append(subj)
    for (k, v) in student_list.items():
        v[subj] = ''
    return student_list, subject_list

def add_mark():
    global student_list
    global subject_list
    show_student()
    stud = new_data('Введите имя и фамилию ученика: ', student_list.keys())
    show_subject()
    subj = new_data('Введите название предмета: ', subject_list)
    mark = get_num('Введите оценку: ')
    student_list[stud][subj] += (' ' + mark)
    return student_list

def show_mark():
    global student_list
    stud = new_data('Введите имя и фамилию ученика: ', student_list.keys())
    marks = student_list[stud]
    for (k, v) in marks.items():
        print('{}: {}'.format(k, v))
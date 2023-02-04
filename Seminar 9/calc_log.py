import telebot

def log(message):
    file = open('log.csv', 'a', encoding="utf-8")
    file.write('{};{};{}\n'.format(message.date, message.from_user.first_name, message.text))
    file.close()
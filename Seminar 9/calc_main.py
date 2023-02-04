import telebot
from telebot import types
from calc_log import log

TOKEN = '6048112543:AAEpsUduWoYEXiVTjTpW_WZBNdk83TaR7Ts'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Добро пожаловать! Операции с какими цислами вы хотите произвести?\n/rational\n/complex')

@bot.message_handler(commands=['rational', 'complex'])
def button(message):
    chat_id = message.chat.id
    if message.text == '/rational':
        ratio_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        sum = types.KeyboardButton('+')
        diff = types.KeyboardButton('-')
        mult = types.KeyboardButton('*')
        div = types.KeyboardButton('/')
        rem = types.KeyboardButton('%')
        div_int = types.KeyboardButton('//')
        ratio_markup.add(sum, diff, mult, div, rem, div_int)
        bot.send_message(chat_id, 'Выберите действие', reply_markup=ratio_markup)
    else:
        bot.send_message(chat_id, 'Stay tuned!')
        start_handler(message)

@bot.message_handler(content_types='text')
def controller(message):
    chat_id = message.chat.id
    if message.text == '+':
        msg = bot.send_message(chat_id, 'Введите числа через пробел')
        bot.register_next_step_handler(msg, sum_num)
    if message.text == '-':
        msg = bot.send_message(chat_id, 'Введите числа через пробел')
        bot.register_next_step_handler(msg, diff_num)
    if message.text == '*':
        msg = bot.send_message(chat_id, 'Введите числа через пробел')
        bot.register_next_step_handler(msg, mult_num)
    if message.text == '/':
        msg = bot.send_message(chat_id, 'Введите числа через пробел')
        bot.register_next_step_handler(msg, div_num)
    if message.text == '%':
        msg = bot.send_message(chat_id, 'Введите числа через пробел')
        bot.register_next_step_handler(msg, rem_num)
    if message.text == '//':
        msg = bot.send_message(chat_id, 'Введите числа через пробел')
        bot.register_next_step_handler(msg, int_div_num)
    log(message)

def sum_num(message):
    items = message.text.split()
    if len(items) != 2:
        msg = bot.send_message(message.chat.id, 'Введите два числа')
        bot.register_next_step_handler(msg, int_div_num)
        return
    else:
        number_1 = int(items[0])
        number_2 = int(items[1])
        bot.send_message(message.chat.id, f'Сумма: {number_1 + number_2}')
    log(message)

def mult_num(message):
    items = message.text.split()
    if len(items) != 2:
        msg = bot.send_message(message.chat.id, 'Введите два числа')
        bot.register_next_step_handler(msg, int_div_num)
        return
    else:    
        number_1 = int(items[0])
        number_2 = int(items[1])
        bot.send_message(message.chat.id, f'Произведение: {number_1 * number_2}')
    log(message)

def div_num(message):
    items = message.text.split()
    if len(items) != 2:
        msg = bot.send_message(message.chat.id, 'Введите два числа')
        bot.register_next_step_handler(msg, int_div_num)
        return
    else:    
        number_1 = int(items[0])
        number_2 = int(items[1])
        bot.send_message(message.chat.id, f'Частное: {number_1 / number_2}')
    log(message)

def diff_num(message):
    items = message.text.split()
    if len(items) != 2:
        msg = bot.send_message(message.chat.id, 'Введите два числа')
        bot.register_next_step_handler(msg, int_div_num)
        return
    else:    
        number_1 = int(items[0])
        number_2 = int(items[1])
        bot.send_message(message.chat.id, f'Разность: {number_1 - number_2}')
    log(message)

def rem_num(message):
    items = message.text.split()
    if len(items) != 2:
        msg = bot.send_message(message.chat.id, 'Введите два числа')
        bot.register_next_step_handler(msg, int_div_num)
        return
    else:    
        number_1 = int(items[0])
        number_2 = int(items[1])
        bot.send_message(message.chat.id, f'Остаток от деления: {number_1 % number_2}')
    log(message)

def int_div_num(message):
    items = message.text.split()
    if len(items) != 2:
        msg = bot.send_message(message.chat.id, 'Введите два числа')
        bot.register_next_step_handler(msg, int_div_num)
        return
    else:    
        number_1 = int(items[0])
        number_2 = int(items[1])
        bot.send_message(message.chat.id, f'Целочисленное частное: {number_1 // number_2}')
    log(message)

bot.polling(none_stop=True)
import telebot
from telebot import types
from calc_log import log
from calc_func import *

TOKEN = '6048112543:AAEpsUduWoYEXiVTjTpW_WZBNdk83TaR7Ts'
bot = telebot.TeleBot(TOKEN)

mode = None
COMPLEX = 'complex'
RATIO = 'ratio'
NUM_1 = 0
SIGN = 1
NUM_2 = 2

@bot.message_handler(commands=['start'])
def start_keyb(message):
    chat_id = message.chat.id
    mrk_modes = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mode_1 = types.KeyboardButton('Рациональные')
    mode_2 = types.KeyboardButton('Комплексные')
    mrk_modes.add(mode_1, mode_2)
    bot.send_message(chat_id, 'Операции с какими цислами вы хотите произвести?', reply_markup=mrk_modes)

@bot.message_handler(content_types='text')
def button(message):
    global mode

    chat_id = message.chat.id
    if message.text == 'Рациональные':
        mode = RATIO
        bot.send_message(chat_id, 'Введите выражение через пробелы')
        bot.register_next_step_handler(message, controller)
    elif message.text == 'Комплексные':
        mode = COMPLEX
        bot.send_message(chat_id, 'Введите выражение через пробелы')
        bot.register_next_step_handler(message, controller)
    log(message)

def controller(message):
    chat_id = message.chat.id

    math_exp = message.text.split()
    if len(math_exp) != 3:
        bot.send_message(chat_id, 'Выражение неверно. Попробуйте еще раз')
        bot.register_next_step_handler(message, controller)
        return
    
    math_sign = math_exp[SIGN]
    if mode == RATIO:
        a = int(math_exp[NUM_1])
        b = int(math_exp[NUM_2])
    elif mode == COMPLEX:
        a = complex(math_exp[NUM_1])
        b = complex(math_exp[NUM_2])
    
    if math_sign == '+':
        result = get_sum(a, b)
    elif math_sign == '-':
        result = get_diff(a, b)
    elif math_sign == '*':
        result = get_prod(a, b)
    elif math_sign == '/':
        result = get_quot(a, b)
    elif mode == COMPLEX and (math_sign == '//' or math_sign == '%'):
        bot.send_message(chat_id, 'Невозможное выражение для комплексных чисел. Повторите ввод')
        bot.register_next_step_handler(message, controller)
        return
    elif math_sign == '//':
        result = get_int_quot(a, b)
    elif math_sign == '%':
        result = get_rem(a, b)

    bot.send_message(chat_id, f'Результат вычислений: {result}')
    start_keyb(message)
    log(message)

bot.polling(none_stop=True)
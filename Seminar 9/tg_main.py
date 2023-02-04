import telebot
from telebot import types
import random

sweets = 2021
MAX_SWEET = 28
USER = 'пользователь'
BOT = 'бот'
user_sweet = 0
flag = USER
RULES = 'На столе лежит {} конфета. Ирок и бот делают ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем {} конфет. Победа достается игроку, если тот заберет последние конфеты.'.format(sweets, MAX_SWEET)

bot = telebot.TeleBot('6026294172:AAFZzeoZbOXj_Thx8dB1iV5S1KzZwxXX-9w')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '/play')

@bot.message_handler(commands=['play'])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    rules = types.KeyboardButton('Правила игры')
    game = types.KeyboardButton('Начать игру')
    markup.add(rules)
    markup.add(game)
    bot.send_message(message.chat.id, 'Выберите действие :)', reply_markup=markup)

@bot.message_handler(content_types='text')
def controller(message):
    global flag

    if message.text == 'Правила игры':
        bot.send_message(message.chat.id, RULES)
        button(message)
    elif message.text == 'Начать игру':
        first_turn = random.choice([BOT, USER])
        flag = USER if first_turn == USER else BOT

        bot.send_message(message.chat.id, 'Первым ходит - {}. /ok'. format(flag))
        bot.register_next_step_handler(message, game)

@bot.message_handler(commands=['ok'])
def game(message):
    global sweets
    global flag

    if sweets > 0:
        if flag == USER:
            bot.send_message(message.chat.id, f'Возьми от 0 до {MAX_SWEET} конфет')
            bot.register_next_step_handler(message, user_turn)
        else:
            bot_turn(message)
    else:
        winner = USER if flag == BOT else BOT
        bot.send_message(message.chat.id, f'Победитель - {winner}!')
        button(message)

@bot.message_handler(content_types='text')
def user_turn(message):
    global sweets
    global flag

    user_sweet = int(message.text)
    sweets -= user_sweet
    if sweets > 0:
        bot.send_message(message.chat.id, f'Остаток конфет - {sweets}')
    else:
        bot.send_message(message.chat.id, 'Конфеты закончились.')
    flag = BOT
    game(message)

def bot_turn(message):
    global sweets
    global flag

    bot_sweet = random.randint(1, 28)
    bot.send_message(message.chat.id, f'Жадный бот забрал {bot_sweet} конфет')
    sweets -= bot_sweet
    if sweets > 0:
        bot.send_message(message.chat.id, f'Остаток конфет - {sweets}')
    else:
        bot.send_message(message.chat.id, 'Конфеты закончились.')
    flag = USER
    game(message)

bot.polling(none_stop=True)
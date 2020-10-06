import telebot
from telebot import types

token = 'token'
bot = telebot.TeleBot(token)

def physics_start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add('Кинематика', 'Динамика')
    bot.send_message(message.from_user.id, 'Выберите тему', reply_markup=markup)
    bot.register_next_step_handler(message, physics_first_menu)

def send_kinematic_data(message):
    bot.send_message(message.from_user.id, 'https://i.pinimg.com/736x/72/3a/16/723a1601535a421b6de2a63e2a6dc426--learn-physics-manual.jpg')
    pass

def send_dinamic_data(message):
    bot.send_message(message.from_user.id, 'https://w512.ru/shpora/images2/f34.jpg')
    pass

def physics_first_menu(message):
    if message.text == 'Кинематика':
        send_kinematic_data(message)
    if message.text == 'Динамика':
        send_dinamic_data(message)



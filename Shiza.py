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


def main():
    dict_of_funcs = {}
    description_position = 0
    globals_copy = globals().copy()
    for key in globals_copy:
        if(isinstance(globals_copy[key], FunctionType)):
            dict_of_funcs[key] = globals_copy[key].__defaults__
    help_message = ""
    for func in dict_of_funcs:
        if(func not in ('main', 'error_handler')):
            help_message+= f"{func} —— {dict_of_funcs[func][description_position]}\n"
    from nasa_api import get_photo, get_weather
    @bot.message_handler(content_types = ['text'])
    def handler(message):
        function_name = message.text[1:]
        try:
            function = globals_copy[function_name]
            function(message)
        except KeyError:
            bot.send_message(message.chat.id, "Неизвестная команда. Напишите команду '/help' для списка команд")
    bot.infinity_polling(True)

def error_handler(func):
    try:
        func()
    except Exception as error:
        #bot.send_message(message.chat.id, f"Произошла ошибка: {error}")
        pass
import telebot
from telebot import types

token = 'token'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types = ['text'])
def physics_start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add('Кинематика', 'Динамика')
    markup.add('Электродинамика', 'Термодинамика')
    bot.send_message(message.from_user.id, 'Выберите тему', reply_markup=markup)
    bot.register_next_step_handler(message, physics_first_menu)


def send_kinematic_data(message):
    bot.send_message(message.from_user.id, 'https://i.pinimg.com/736x/72/3a/16/723a1601535a421b6de2a63e2a6dc426--learn-physics-manual.jpg', reply_markup = types.ReplyKeyboardRemove())
    pass

def send_dinamic_data(message):
    bot.send_message(message.from_user.id, 'https://w512.ru/shpora/images2/f34.jpg', reply_markup = types.ReplyKeyboardRemove())
    pass

def send_thermodynamics_data(message):
    bot.send_message(message.from_user.id, 'https://www.examen.ru/assets/images/2014/formuly/fiz/7_04.png', reply_markup = types.ReplyKeyboardRemove())
    pass

def send_electrodynamics_data(message):
    bot.send_message(message.from_user.id, 'https://math-phys.ru/images/math-phys/trainer/trainer_ege_phys_10b.jpg', reply_markup = types.ReplyKeyboardRemove())
    pass

def physics_first_menu(message):
    if message.text == 'Кинематика':
        send_kinematic_data(message)
    if message.text == 'Динамика':
        send_dinamic_data(message)
    if message.text == 'Термодинамика':
        send_thermodynamics_data(message)
    if message.text == 'Электродинамика':
        send_electrodynamics_data(message)




bot.infinity_polling(True)



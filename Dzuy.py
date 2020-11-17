import telebot
from telebot import types

token = 'token'
bot = telebot.TeleBot(token)

bibl = {'Биты': 0, 'Байты': 3, 'Килобиты': 10, 'Килобайты': 13, 'Мегабиты': 20, 'Мегабайты': 23, 'Гигабиты': 30, 'Гигабайты': 33, 'Терабиты': 40, 'Терабайты': 43}
cart = tuple(bibl.keys())

@bot.message_handler(commands=['info'])
def choice(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add("Физика", "Информатика")
    bot.send_message(message.chat.id, "По физике или по информатике?", reply_markup=markup)
    bot.register_next_step_handler(message, choice_inf_phy)

def choice_inf_phy(message):
    if message.text == 'Физика':
        phy_info(message)
    if message.text == 'Информатика':
        inf_info(message)

def phy_info(message):
    bot.send_message(message.chat.id, "Phy", reply_markup=types.ReplyKeyboardRemove())

def inf_info(message):
    bot.send_message(message.chat.id, "Долю секунды...", reply_markup=types.ReplyKeyboardRemove())
    markup = types.ReplyKeyboardMarkup()
    markup.add("Шестнадцатеричные цифры", "Степени двойки", "Веса информации",
               "Максимальное число")
    bot.send_message(message.chat.id, "Что ты хочешь узнать?", reply_markup=markup)
    bot.register_next_step_handler(message, send_inf_png)

def send_inf_png(message):
    if message.text == 'Шестнадцатеричные цифры':
        img = open('InfInf/16.png', 'rb')
        bot.send_photo(message.chat.id, img, reply_markup=types.ReplyKeyboardRemove())
    if message.text == 'Степени двойки':
        img = open('InfInf/Step2.png', 'rb')
        bot.send_photo(message.chat.id, img, reply_markup=types.ReplyKeyboardRemove())
    if message.text == 'Веса информации':
        img = open('InfInf/BBKMT.png', 'rb')
        bot.send_photo(message.chat.id, img, reply_markup=types.ReplyKeyboardRemove())
    if message.text == 'Максимальное число':
        img = open('InfInf/max.png',  'rb')
        bot.send_photo(message.chat.id, img, reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(commands=['calc'])
def calc_input_from(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(*cart)
    bot.send_message(message.chat.id, "Из чего?", reply_markup=markup)
    bot.register_next_step_handler(message, calc_input_to)

def calc_input_to(message):
    Input = message.text
    markup = types.ReplyKeyboardMarkup()
    markup.add(*cart)
    bot.send_message(message.chat.id, "Во что?", reply_markup=markup)
    bot.register_next_step_handler(message, calc_input_hm, Input)

def calc_input_hm(message, Input):
    Output = message.text
    bot.send_message(message.chat.id, "Сколько?", reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, calc_output, Input, Output)

def calc_output(message, Input, Output):
    try:
        output_send = float(message.text)
        input_s = bibl[Input]
        output_s = bibl[Output]
    except Exception:
        bot.send_message(message.chat.id, "Не катит")
    else:
        output_send = 2**input_s * output_send / 2**output_s
        output_send = str(output_send) + " = 2^" + str(input_s) + " * " + str(output_send)
        bot.send_message(message.chat.id, output_send)

bot.infinity_polling(True)
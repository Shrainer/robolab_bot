import telebot
from telebot import types

token = 'token'
bot = telebot.TeleBot(token)

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

bot.infinity_polling(True)
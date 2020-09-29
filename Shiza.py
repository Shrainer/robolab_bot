import telebot
from telebot import types

token = 'token'
bot = telebot.TeleBot(token)

def physics(message, description = ""):
  markup = types.ReplyKeyboardMarkup()
  markup.add('Кинематика' , 'Динамика')

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

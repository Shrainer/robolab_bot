import telebot
from types import FunctionType
from functions import *

token = 'token'
bot = telebot.TeleBot(token)

def error_handler(func):
	def wrapper(*args):
		try:
			func(*args)
		except Exception as error:
			print(f"Произошла ошибка: {error}")
	return wrapper

def type_and_reply(chat_id, text, step_handler):
	message = bot.send_message(chat_id, text)
	if(step_handler):
		global handler_function
		handler_function = step_handler
		bot.register_next_step_handler(message, register_step)

@error_handler
def register_step(message):
	global handler_function
	text = handler_function(message.text)
	bot.send_message(message.chat.id, text)

def main():
	@bot.message_handler(content_types = ['text'])
	def handler(message):
		function_name = message.text[1:]
		try:
			function = dict_of_funcs[function_name][0]
			output = function()
			type_and_reply(message.chat.id, *output)
		except KeyError:
			bot.send_message(message.chat.id, "Неизвестная команда. Напишите команду '/help' для списка команд")
		except:
			pass
	bot.infinity_polling(True)

if __name__ == '__main__':
	main()

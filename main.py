import telebot
from types import FunctionType

token = 'token'
bot = telebot.Telebot(token)

def start(messsage, description = "Описание 1"):
	pass

def stop(message, description = "Описание 2"):
	pass

def help(message):
	global help_message
	bot.send_message(message.chat.id, help_message)
	
if __name__ == '__main__':	
	dict_of_funcs = {}
	description_position = 0
	globals_copy = globals().copy()
	for key in globals_copy:
		if(isinstance(globals_copy[key], FunctionType)):
        	dict_of_funcs[key] = globals_copy[key].__defaults__ #составляем словарь функций и их описаний
	help_message = ""
	for func in dict_of_funcs:
		if(func != 'help'):
			help_message+= f"{func} —— {dict_of_funcs[func][description_position]}\n"
		#создаём сообщение для команды /help со всеми командами и их кратким описанием
	@bot.message_handler(content_types = ['text'])
	def handler(message):
		function_name = message.text[1:]
		try:
			function = globals_copy[function_name]
			function(message)
		except KeyError:
			bot.send_message(message.chat.id, "Неизвестная команда. Напишите команду '/help' для списка команд") 
			#если пользователь написал существующую функцию, выполняем её
	
	bot.infinity_polling(True)
												  

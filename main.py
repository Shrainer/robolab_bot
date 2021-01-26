import telebot, nasapy, os, functions, database

absolute_path = os.path.abspath(__file__)
absolute_path = absolute_path[:absolute_path.rfind("/") + 1]

token = os.environ.get('telebot_token')
bot = telebot.TeleBot(token)

api_key = os.environ.get('nasapy_token')
api = nasapy.Nasa(key = api_key)

def main():
	info_list = {'Шестнадцатеричниые цифры': f'{absolute_path}/16.png', 'Степени двойки': f'{absolute_path}/Step2.png',
	'Веса информации': f'{absolute_path}/BBKMT.png', 'Максимальное число': f'{absolute_path}/max.png'}
	physics_list = ()
	funcs = functions.functions_class(bot, api, api_key, telebot.types, database.database(), info_list, physics_list)
	@bot.message_handler(content_types = ['text'])
	def handler(message):
		function_name = message.text[1:]
		if(message.from_user.id in funcs.get_user_ids()):
			try:
				if(funcs.get_user_level(message.from_user.id) <= funcs._dict_of_funcs[function_name][2]):
					function = funcs._dict_of_funcs[function_name][0]
					function(message)
				else:
					bot.send_message(message.chat.id, "У тебя нету прав!")
			except KeyError:
				bot.send_message(message.chat.id, "Неизвестная команда. Напишите команду '/help' для списка команд")
			except Exception as e:
				print(e)
		else:
			if(function_name != "register"):
				bot.send_message(message.chat.id, "Ты не зарегистрирован, чтобы я с тобой общался, напиши '/register'")
			else:
				funcs._dict_of_funcs[function_name][0](message)
	bot.infinity_polling(True)

if __name__ == '__main__':
	main()

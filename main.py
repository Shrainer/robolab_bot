import telebot, nasapy, os, functions

absolute_path = os.path.abspath(__file__)
absolute_path = absolute_path[:absolute_path.rfind("/") + 1]

token = os.environ.get('telebot_token')
bot = telebot.TeleBot(token)

api_key = os.environ.get('nasapy_token')
api = nasapy.Nasa(key = api_key)

def main():
	registered_users = {}
	with open(f"{absolute_path}/users.txt", "r") as file:
	    for line in file.readlines():
	        id, name = line.rstrip('\n').split()
	        registered_users[int(id)] = name
	info_list = {'Шестнадцатеричниые цифры': f'{absolute_path}/16.png', 'Степени двойки': f'{absolute_path}/Step2.png',
	'Веса информации': f'{absolute_path}/BBKMT.png', 'Максимальное число': f'{absolute_path}/max.png'}
	physics_list = ()
	funcs = functions.functions_class(bot, api, api_key, telebot.types, registered_users, info_list, physics_list)
	@bot.message_handler(content_types = ['text'])
	def handler(message):
		function_name = message.text[1:]
		if(message.from_user.id in registered_users.keys()) or (message.from_user.username == "LasichAndGigond") or (function_name == "register"):
			try:
				function = funcs._dict_of_funcs[function_name][0]
				function(message)
			except KeyError:
				bot.send_message(message.chat.id, "Неизвестная команда. Напишите команду '/help' для списка команд")
			except Exception as e:
				print(e)
		else:
			bot.send_message(message.chat.id, "Ты не зарегистрирован, чтобы я с тобой общался, напиши '/register'")
	bot.infinity_polling(True)

if __name__ == '__main__':
	main()

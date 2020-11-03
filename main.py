import telebot, nasapy, functions

token = 'token'
bot = telebot.TeleBot(token)

api_key = 'key'
api = nasapy.Nasa(key = api_key)

def main():
	registered_users = {}
	with open("users.txt", "r") as file:
	    for line in file.readlines():
	        id, name = line.rstrip('\n').split()
	        registered_users[int(id)] = name
	funcs = functions.functions_class(bot, api, api_key, telebot.types.ReplyKeyboardRemove(), registered_users)
	@bot.message_handler(content_types = ['text'])
	def handler(message):
		function_name = message.text[1:]
		if(message.from_user.id in registered_users.keys()) or (message.from_user.username == "LasichAndGigond") or (function_name == "register"):
			try:
				function = funcs._dict_of_funcs[function_name][0]
				function(message)
			except KeyError:
				bot.send_message(message.chat.id, "Неизвестная команда. Напишите команду '/help' для списка команд")
			except:
				pass
		else:
			bot.send_message(message.chat.id, "Ты не зарегистрирован, чтобы я с тобой общался, напиши '/register'")
	bot.infinity_polling(True)

if __name__ == '__main__':
	main()

#F

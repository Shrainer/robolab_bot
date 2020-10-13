import telebot
from types import FunctionType
from nasa_api import get_weather, get_media, earth_photo, rover_photo

token = 'token'
bot = telebot.TeleBot(token)

def start(message):
	bot.send_message(message.chat.id, "Привет, спасибо, что написал мне)))")

def weather(message):
	average_temperature = get_weather()
	bot.send_message(message.chat.id, f"Сегогдняшняя средняя температура на Марсе: {average_temperature}C")

def photo(message):
	url_to_media = get_media()
	bot.send_message(message.chat.id, url_to_media)

def earth(message):
	url_to_photo, flag = earth_photo()
	bot.send_message(message.chat.id, url_to_photo)
	if(flag): bot.send_message(message.chat.id, "Не было сегодняшнего фото, отправил старое")

def rover(message):
	photos = rover_photo()
	message_text = ""
	for url in list(photos):
		message_text+= url + '\n'
	bot.send_message(message.chat.id, message_text)

def help(message):
	global help_message
	bot.send_message(message.chat.id, help_message)

def main():
	dict_of_funcs = {"start":(start, "Приветствие"), "weather":(weather, "Получить данные о погоде на Марсе, которые мы сами не знаем, как обрабатывать"),
	"photo":(photo, "Получить свежую фотку с Марса, но не в hd :/"), "earth":(earth, "Фотка Земли со спуника НАСА"), "rover":(rover, "Фотки с ровера какого-то"),
	"help":(help, "Функция HELP поможет вам всегда")}
	help_message = ""
	for func in dict_of_funcs:
		if(func not in ('main', 'error_handler')):
			help_message+= f"{func} —— {dict_of_funcs[func][1]}\n"
	@bot.message_handler(content_types = ['text'])
	def handler(message):
		function_name = message.text[1:]
		try:
			function = dict_of_funcs[function_name][0]
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

if __name__ == '__main__':
	@error_handler
	main()

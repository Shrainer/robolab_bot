import requests, json, numpy
from time import strftime, gmtime, time
from random import random, randint, choice

class functions_class():
    def __init__(self, bot, api, api_key, types, database, info_list, physics_list):
        self._types = types
        self._default_markup = self._types.ReplyKeyboardRemove()
        self._bot = bot
        self._api = api
        self._database = database
        self._api_key = api_key
        self._bibl = {'Биты': 0, 'Байты': 3, 'Килобиты': 10, 'Килобайты': 13, 'Мегабиты': 20, 'Мегабайты': 23, 'Гигабиты': 30, 'Гигабайты': 33, 'Терабиты': 40, 'Терабайты': 43}
        self._info_list = info_list
        self._physics_list = physics_list
        self._dict_of_funcs = {"start":(self.start, "Приветствие", 3), "weather":(self.get_weather, "Получить данные о погоде на Марсе, которые мы сами не знаем, как обрабатывать", 3),
        "photo":(self.get_media, "Получить свежую фотку дня, но не в hd :/", 3), "earth":(self.earth_photo, "Фотка Земли со спуника НАСА", 3), "rover":(self.rover_photo, "Фотки с ровера какого-то", 3),
        "help":(self.help, "Функция HELP поможет вам всегда", 3),
        "random":(self.random_number, "Рандом", 3), "rock":(self.RPS, "Играть в игру", 3),
        "register":(self.register_user, "Регистрация", 3), "info":(self.get_info, "Подсказки для школы", 3),
        "calc":(self.binary_calc, "Бинарный калькулятор", 3), "register_switch":(self.register_switch, "Включить или отключить регистрацию", 1),
        "delete_user":(self.delete_user, "Удалить пользователя из БД", 1)}
        self._is_register_open = True
        self._help_message = ""
        for func in self._dict_of_funcs:
            self._help_message+= f"/{func} —— {self._dict_of_funcs[func][1]}\n"

    """
    def error_handler(func):
        def wrapper(*args):
            try:
                func(*args)
            except Exception as error:
                print(f"Произошла ошибка: {error}")
        return wrapper
    """

    def get_user_ids(self):
        ids = numpy.array(list(self._database("SELECT user_id from UsersZXC")), int)
        ids = list(ids.flat[0:])
        return ids

    def get_user_name(self, id):
        name = list(self._database(f"SELECT user_name from UsersZXC WHERE user_id = {id}"))[0][0]
        return name

    def get_user_level(self, id):
        level = list(self._database(f"SELECT level from UsersZXC WHERE user_id = {id}"))[0][0]
        return level

    def register_handler(self, message, function, *args):
        try:
            function(message, *args)
        except Exception as error:
            print(f"Произошла ошибка: {error}")
            self._bot.send_message(message.chat.id, "Что-то пошло не так(", reply_markup = self._default_markup)

    def start(self, message):
        self._bot.send_message(message.chat.id, f"Привет, спасибо, что написал мне, {self.get_user_name(message.from_user.id)}", reply_markup = self._default_markup)

    def RPS(self, message, combinations = {"камень":"ножницы","ножницы":"бумага","бумага":"камень"}):
        def handler(message):
            text = message.text
            chat_id = message.chat.id
            player_choice = text.lower()
            if(player_choice in tuple(combinations.keys())):
                if combinations[bot_choice] == player_choice:
                    self._bot.send_message(chat_id, f"Я победил, хорошо, что я выбрал {bot_choice}!", reply_markup = self._default_markup)
                elif player_choice == bot_choice:
                    self._bot.send_message(chat_id, "Ничья", reply_markup = self._default_markup)
                else:
                    self._bot.send_message(chat_id, f"Я проиграл, зря я использоваль {bot_choice} ((", reply_markup = self._default_markup)
            else:
                self._bot.send_message(chat_id, "Ты неправильно играешь, не знаешь, как правильно писать надо?", reply_markup = self._default_markup)
        bot_choice = choice(tuple(combinations.keys()))
        markup = self._types.ReplyKeyboardMarkup()
        markup.add("Камень", "Ножницы", "Бумага")
        self._bot.send_message(message.chat.id, "Я сделал свой выбор, твоя очередь!", reply_markup = markup)
        self._bot.register_next_step_handler(message, self.register_handler, handler)

    def random_number(self, message):
        def handler(message):
            text = message.text
            a, b = text.split()
            self._bot.send_message(message.chat.id, randint(int(a), int(b)), reply_markup = self._default_markup)
        self._bot.send_message(message.chat.id, "Отправьте мне два числа через пробел, и я верну случайное в интервале", reply_markup = self._default_markup)
        self._bot.register_next_step_handler(message, self.register_handler, handler)

    def convert_bytes(self, message):
        self._bot.send_message(message.chat.id, "Выберите величину", reply_markup = self._default_markup)

    def register_user(self, message):
        def handler(message):
            user_id = message.from_user.id
            chat_id = message.chat.id
            text = message.text
            if(user_id not in self.get_user_ids()):
                self._database(f"""INSERT INTO UsersZXC (user_id, user_name, level)
                              VALUES ({user_id}, '{text}', 3)
                              """)
                self._bot.send_message(chat_id, "Я тебя зарегал вроде как", reply_markup = self._default_markup)
            else:
                self._bot.send_message(chat_id, "Ты уже зареган", reply_markup = self._default_markup)
        if(self._is_register_open):
            self._bot.send_message(message.chat.id, "Напиши мне, как тебя будут звать", reply_markup = self._default_markup)
            self._bot.register_next_step_handler(message, self.register_handler, handler)
        else:
            self._bot.send_message(message.chat.id, "Регистрация на данный момент закрыта", reply_markup = self._default_markup)

    def register_switch(self, message):
        self._is_register_open = not self._is_register_open
        self._bot.send_message(message.chat.id, "Регистрация снова открыта!" if self._is_register_open else "Администратор, вы закрыли регистрацию в бота", reply_markup = self._default_markup)

    def delete_user(self, message):
        def handler(message):
            to_delete = message.text
            self._database(f"DELETE FROM UsersZXC WHERE user_name = '{to_delete}'")
            self._bot.send_message(message.chat.id, "Удалили человечка из датабазы()", reply_markup = self._default_markup)
        all_names = numpy.array(list(self._database("SELECT user_name FROM UsersZXC")), str).flat[0:]
        markup = self._types.ReplyKeyboardMarkup()
        markup.add(*all_names)
        self._bot.send_message(message.chat.id, "Кого надобно вам удалить?", reply_markup = markup)
        self._bot.register_next_step_handler(message, self.register_handler, handler)

    def get_media(self, message):
        media = self._api.picture_of_the_day()
        self._bot.send_message(message.chat.id, media['url'], reply_markup = self._default_markup)

    def get_weather(self, message):
        data = self._api.mars_weather()
        self._bot.send_message(message.chat.id, data[list(data.keys())[0]]["AT"]['av'], reply_markup = self._default_markup)

    def earth_photo(self, message, date = strftime("%Y-%m-%d", gmtime()), counter = 1):
        year = date[:4]
        month = date[5:7]
        day = date[8:10]
        epic_photos = self._api.epic(date = date)
        if not(epic_photos):
            self.earth_photo(message, strftime("%Y-%m-%d", gmtime(time() - 86400 * counter)), counter + 1)
        else:
            random_index = int(len(epic_photos) * random())
            photo_name = epic_photos[random_index]['image']
            url_to_image = f"https://epic.gsfc.nasa.gov/archive/natural/{year}/{month}/{day}/jpg/{photo_name}.jpg"
            self._bot.send_message(message.chat.id,  f"Отправил фотографии за {date}\n\n{url_to_image}", reply_markup = self._default_markup)

    def rover_photo(self, message, date = strftime("%Y-%m-%d", gmtime()), counter = 1):
        url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={date}&api_key={self._api_key}"
        result = json.loads(requests.get(url).text)
        photos = result['photos']
        if not(photos):
            self.rover_photo(message, strftime("%Y-%m-%d", gmtime(time() - 86400 * counter)), counter + 1)
        else:
            random_num = randint(0, len(photos) - 3)
            list_of_url = [photos[i]['img_src'] for i in range(random_num, random_num + 3)]
            string = "\n\n".join(list_of_url)
            self._bot.send_message(message.chat.id, f"Это фотографии от {date} \n\n {string}", reply_markup = self._default_markup)

    def binary_calc(self, message):
        def handler(message):
            user_input = self._bibl[message.text]
            self._bot.send_message(message.chat.id, "Во что?",reply_markup=markup)
            self._bot.register_next_step_handler(message, self.register_handler, self.binary_calc_input, user_input)
        markup = self._types.ReplyKeyboardMarkup()
        markup.add(*self._bibl)
        self._bot.send_message(message.chat.id, "Из чего?", reply_markup=markup)
        self._bot.register_next_step_handler(message, self.register_handler, handler)

    def binary_calc_input(self, message, user_input):
        output = self._bibl[message.text]
        self._bot.send_message(message.chat.id, "Сколько?", reply_markup=self._default_markup)
        self._bot.register_next_step_handler(message, self.register_handler, self.binary_calc_result, user_input, output)

    def binary_calc_result(self, message, user_input, output):
        output_send = float(message.text)
        output_send = 2**user_input * output_send / 2**output
        output_send = str(output_send) + " = 2^" + str(user_input) + " * " + str(output_send)
        self._bot.send_message(message.chat.id, output_send)

    def get_info(self, message):
        def handler(message):
            if(message.text == "Информатика"):
                list_of_choice = self._info_list
            else:
                list_of_choice = self._physics_list
            self._bot.send_message(message.chat.id, "Обновляю варианты...", reply_markup=self._default_markup)
            markup = self._types.ReplyKeyboardMarkup()
            markup.add(*list(list_of_choice.keys()))
            self._bot.send_message(message.chat.id, "Что именно узнать?", reply_markup=markup)
            self._bot.register_next_step_handler(message, self.register_handler, self.send_info, list_of_choice)
        markup = self._types.ReplyKeyboardMarkup()
        markup.add("Физика", "Информатика")
        self._bot.send_message(message.chat.id, "По физике или по информатике?", reply_markup=markup)
        self._bot.register_next_step_handler(message, self.register_handler, handler)

    def send_info(self, message, list_of_choice):
        with open(list_of_choice[message.text], 'rb') as image:
            self._bot.send_photo(message.chat.id, image, reply_markup=self._default_markup)

    def help(self, message):
        self._bot.send_message(message.chat.id, self._help_message, reply_markup = self._default_markup)

#Tabs – 4 хватит

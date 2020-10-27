import nasapy, requests, json
from time import strftime, gmtime, time
from random import random, randint, choice

api_key = 'key'
api = nasapy.Nasa(key = api_key)

def start():
    return "Привет, спасибо, что написал мне)))", False

def RPS(combinations = {"камень":"ножницы","ножницы":"бумага","бумага":"камень"}):
    def handler(message):
        text = message.text
        player_choice = text.lower()
        if(player_choice in tuple(combinations.keys())):
            if combinations[bot_choice] == player_choice:
                return f"Я победил, хорошо, что я выбрал {bot_choice}!"
            elif player_choice == bot_choice:
                return "Ничья"
            else:
                return f"Я проиграл, зря я использоваль {bot_choice} (("
        else:
            return "Ты неправильно играешь, не знаешь, как правильно писать надо?"
    bot_choice = choice(tuple(combinations.keys()))
    return "Я сделал свой выбор, твоя очередь!", handler

def random_number():
    def handler(message):
        text = message.text
        a, b = text.split()
        return randint(int(a), int(b))
    return "Отправьте мне два числа через пробел, и я верну случайное в интервале", handler

def register_user():
    global registered_users
    def handler(message):
        user_id = message.from_user.id
        text = message.text
        if(user_id not in registered_users):
            with open("users.txt", "a") as file:
                file.write(f"{user_id} {text.split()[0]}\n")
            registered_users[user_id] = text
            return "Я тебя зарегал вроде как"
        else:
            return "Ты уже зареган"
    return "Напиши мне, как тебя будут звать", handler

def get_media():
    media = api.picture_of_the_day()
    return media['url'], False

def get_weather():
    data = api.mars_weather()
    return data[list(data.keys())[0]]["AT"]['av'], False

def earth_photo(date = strftime("%Y-%m-%d", gmtime()), counter = 1):
    year = date[:4]
    month = date[5:7]
    day = date[8:10]
    epic_photos = api.epic(date = date)
    if not(epic_photos):
        return earth_photo(strftime("%Y-%m-%d", gmtime(time() - 86400 * counter)), counter + 1)
    else:
        random_index = int(len(epic_photos) * random())
        photo_name = epic_photos[random_index]['image']
        url_to_image = f"https://epic.gsfc.nasa.gov/archive/natural/{year}/{month}/{day}/jpg/{photo_name}.jpg"
        return f"Отправил фотографии за {date}\n\n{url_to_image}", False

def rover_photo(date = strftime("%Y-%m-%d", gmtime()), counter = 1):
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={date}&api_key={api_key}"
    result = json.loads(requests.get(url).text)
    photos = result['photos']
    if not(photos):
        return rover_photo(strftime("%Y-%m-%d", gmtime(time() - 86400 * counter)), counter + 1)
    else:
        random_num = randint(0, len(photos) - 3)
        list_of_url = [photos[i]['img_src'] for i in range(random_num, random_num + 3)]
        string = "\n\n".join(list_of_url)
        return f"Это фотографии от {date} \n\n {string}", False

def help():
    global help_message
    return help_message, False

dict_of_funcs = {"start":(start, "Приветствие"), "weather":(get_weather, "Получить данные о погоде на Марсе, которые мы сами не знаем, как обрабатывать"),
"photo":(get_media, "Получить свежую фотку дня, но не в hd :/"), "earth":(earth_photo, "Фотка Земли со спуника НАСА"), "rover":(rover_photo, "Фотки с ровера какого-то"),
"help":(help, "Функция HELP поможет вам всегда"),
"random":(random_number, "Рандом"), "rock":(RPS, "Играть в игру"), "register":(register_user, "Регистрация")}

registered_users = {}
with open("users.txt", "r") as file:
    for line in file.readlines():
        id, name = line.rstrip('\n').split()
        registered_users[int(id)] = name
print(registered_users)

help_message = ""
for func in dict_of_funcs:
    help_message+= f"/{func} —— {dict_of_funcs[func][1]}\n"

#Tabs – 4 хватит

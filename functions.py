import nasapy, requests, json
from time import strftime, gmtime, time
from random import random, randint

api_key = 'key'
api = nasapy.Nasa(key = api_key)

def start():
    return "Привет, спасибо, что написал мне)))", False

def random_number():
    def handler(text):
        a, b = text.split()
        return randint(int(a), int(b))
    return "Отправьте мне два числа через пробел, и я верну случайное в интервале", handler

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
"photo":(get_media, "Получить свежую фотку с Марса, но не в hd :/"), "earth":(earth_photo, "Фотка Земли со спуника НАСА"), "rover":(rover_photo, "Фотки с ровера какого-то"),
"help":(help, "Функция HELP поможет вам всегда"), "random":(random_number, "Рандом")}

help_message = ""
for func in dict_of_funcs:
    help_message+= f"{func} —— {dict_of_funcs[func][1]}\n"

#Tabs – 4 хватит

import nasapy, requests, json
from time import strftime, gmtime, time
from random import random, randint

api_key = 'u76ZsSAKzdqxj9zODDD4BxDOflOpMgmC4bUblFvo'
api = nasapy.Nasa(key = api_key)

def get_media():
    media = api.picture_of_the_day()
    return media['url']

def get_weather():
    data = api.mars_weather()
    return data[list(data.keys())[0]]["AT"]['av']

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
        return f"Не было сегодняшнего фото, отправил за {date}\n\n{url_to_image}"

def rover_photo(date = strftime("%Y-%m-%d", gmtime()), counter = 1):
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={date}&api_key={api_key}"
    result = json.loads(requests.get(url).text)
    photos = result['photos']
    if not(photos):
        return rover_photo(strftime("%Y-%m-%d", gmtime(time() - 86400 * counter)), counter + 1)
    else:
        random_num = randint(0, len(photos) - 3)
        list_of_url = [photos[i]['img_src'] for i in range(random_num, random_num + 3)]
        return f"Это фотографии от {date} \n\n {"\n\n".join(list_of_url)}"

#Tabs – 4 хватит

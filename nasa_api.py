import nasapy, urllib
from time import strftime, gmtime

api = nasapy.Nasa(key = 'key')
flag = False

def get_photo():
    global flag
    picture = api.picture_of_the_day()
    date_of_photo = picture['date']
    text = picture['explanation']
    today_day = strftime("%Y-%m-%d", gmtime())
    if(date_of_photo != today_day or flag == False):
        flag = True
        with open('picture.jpg', 'wb') as photo:
            url_to_photo = picture['url']
            photo.write(urllib.request.urlopen(url_to_photo).read())
            photo.close()
    return text

def get_weather():
    data = api.mars_weather()
        for i in data:
            return data[i]["AT"]['av']

#Tabs – 4 хватит

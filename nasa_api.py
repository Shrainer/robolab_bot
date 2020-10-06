import nasapy
from time import strftime, gmtime
api = nasapy.Nasa(key = 'key')

def get_media():
    media = api.picture_of_the_day()
    return url_to_media = media['url']

def get_weather():
    data = api.mars_weather()
        for i in data:
            return data[i]["AT"]['av']

def earth_photo():
    today_date = strftime("%Y-%m-%d", gmtime())
    year = today_date[:4]
    month = today_date[5:7]
    day = today_date[8:10]
    epic_photos = api.epic(date = today_date)
    photo_name = epic_photos[0]['image']
    url_to_image = f"https://epic.gsfc.nasa.gov/archive/natural/{year}/{month}/{day}/jpg/{photo_name}.jpg"
    return url_to_image
#Tabs – 4 хватит

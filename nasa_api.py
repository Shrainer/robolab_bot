import nasapy

api = nasapy.Nasa(key = 'key')

def get_media():
    media = api.picture_of_the_day()
    return url_to_media = media['url']

def get_weather():
    data = api.mars_weather()
        for i in data:
            return data[i]["AT"]['av']

#Tabs – 4 хватит

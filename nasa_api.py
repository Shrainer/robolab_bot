import nasapy, requests, json
from time import strftime, gmtime, time

api_key = 'key'
api = nasapy.Nasa(key = api_key)

def get_media():
    media = api.picture_of_the_day()
    return media['url']

def get_weather():
    data = api.mars_weather()
    for i in data:
        return data[i]["AT"]['av']

def earth_photo(date = strftime("%Y-%m-%d", gmtime()), flag = False, counter = 1):
    year = date[:4]
    month = date[5:7]
    day = date[8:10]
    epic_photos = api.epic(date = date)
    if not(epic_photos):
        return earth_photo(strftime("%Y-%m-%d", gmtime(time() - 86400 * counter)), True, counter + 1)
    else:
        photo_name = epic_photos[0]['image']
        url_to_image = f"https://epic.gsfc.nasa.gov/archive/natural/{year}/{month}/{day}/jpg/{photo_name}.jpg"
        return url_to_image, flag, date

def rover_photo(date = strftime("%Y-%m-%d", gmtime()), flag = False, counter = 1):
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={date}&api_key={api_key}"
    result = json.loads(requests.get(url).text)
    if not(result['photos']):
        return rover_photo(strftime("%Y-%m-%d", gmtime(time() - 86400 * counter)), True, counter + 1)
    else:
        list_of_url = []
        for dictionary in result['photos']:
            list_of_url.append(dictionary['img_src'])
        return list_of_url, flag, date

#Tabs – 4 хватит

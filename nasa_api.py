import nasapy, urllib
from time import strftime, gmtime 

api = nasapy.Nasa(key = 'key')

def get_photo():
	picture = api.picture_of_the_day()
	date_of_photo = picture['date']
	text = picture['explanation']
	today_day = strftime("%Y-%m-%d", gmtime())
	if(date_of_photo != today_day):
		with open('picture.jpg', 'wb') as photo:
			url_to_photo = picture['url']
			photo.write(urllib.request.urlopen(url).read())
			photo.close()
	with open('picture.jpg', rb) as photo:
		return text, photo

def get_weather():
	data = api.mars_weather()
	def	get_data(data):
		for i in data:
			return data[i]["AT"], data[i]["HWS"]
	result = get_data(data)
	return result[0]['av']
#Tabs – 4

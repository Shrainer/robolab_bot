import nasapy, urllib
from time import strftime, gmtime 

api = nasapy.Nasa(key = 'key')

def get_photo():
	picture = api.picture_of_the_day()
	date_of_photo = picture['date']
	today_day = strftime("%Y-%m-%d", gmtime())
	if(date_of_photo != today_day):
		with open('picture.jpg', 'wb') as photo:
			text = picture['explanation']
			url_to_photo = picture['url']
			photo.write(urllib.request.urlopen(url).read())
			photo.close()
	with open('picture.jpg', rb) as photo:
		return text, photo

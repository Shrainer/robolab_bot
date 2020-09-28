import nasapy, urllib

api = nasapy.Nasa(key = 'key')

picture = api.picture_of_the_day()
text = picture['explanation']
url_to_photo = picture['url']
with photo as open('picture.jpg', 'wb'):
	photo.write(urllib.request.urlopen(url).read())
	photo.close()

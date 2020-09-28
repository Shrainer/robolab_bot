import nasapy, urllib

api = nasapy.Nasa(key = 'key')

def get_weather():
    data = api.mars_weather()
    for i in tt:
        return data[i]["AT"], data[i]["HWS"]

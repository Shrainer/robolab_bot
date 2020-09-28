import json 
import nasapy, urllib

api = nasapy.Nasa(key = 'key')

def get_weather():
    data = api.mars_weather()
    tt = json.loads(data.text)
    for i in tt:
        return tt[i]["AT"], tt[i]["HWS"]
    print(data)

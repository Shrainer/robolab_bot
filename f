import requests 
import json 
import webbrowser

def weather():
    f = r"https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0"
    data = requests.get(f)
    tt = json.loads(data.text)
    for i in tt:
        return tt[i]["AT"], tt[i]["HWS"]

print(marsweather())

from datetime import date
from functools import update_wrapper
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import json  # import json to load json data to python dictionary
import urllib.request  # urllib.request to make a request to api

def index(request):
    if request.method == 'POST':
        city = request.POST['city']

        # source contain JSON data from API
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=ac3d4963f935c2146c221ebc2f8ec8c4&units=metric').read()

        # converting JSON data to a dictionary
        list_of_data = json.loads(source)

        mmRtSt = int(list_of_data['main']['pressure']) * 3 / 4

        # data for variable list_of_data
        data = {
            'city': city.capitalize(),
            "country_code": str(list_of_data['sys']['country']),
            "temp": str(list_of_data['main']['temp']) + ' ℃',
            "pressure": str(mmRtSt) + ' mmhg',
            "visibility": str(list_of_data['visibility']) + ' meters',
            "wind_speed":str (list_of_data['wind']['speed']) + ' m/s',
            "clouds": str(list_of_data['clouds']['all']) + '%',
        }
        print(data)
    else:
        data ={}
    return render(request, "index.html", data)
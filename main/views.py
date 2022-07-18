from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import json  # import json to load json data to python dictionary
import urllib.request  # urllib.request to make a request to api

# 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={&appid=ac3d4963f935c2146c221ebc2f8ec8c4}'

def index(request):
    if request.method == 'POST':
        city = request.POST['city']

        ''' api key might be expired use your own api_key
            place api_key in place of appid ="your_api_key_here "  '''
        # source contain JSON data from API
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=ac3d4963f935c2146c221ebc2f8ec8c4&units=metric').read()

        # converting JSON data to a dictionary
        list_of_data = json.loads(source)

        # data for variable list_of_data
        data = {
            'city': city,
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + ' c',

            "humidity": str(list_of_data['main']['humidity']) + '%',
        }
        print(data)
    else:
        data ={}
    return render(request, "index.html", data)
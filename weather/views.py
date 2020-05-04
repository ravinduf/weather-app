import requests 
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=4ada227d2084bef19fb1c459fadd44a6'
    city = 'Kandana'

    r = requests.get(url.format(city)).json()
    

    city_weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon']
    }

    print(city_weather)
    context = {'city_weather': city_weather}
    return render(request, 'weather/index.html', context)

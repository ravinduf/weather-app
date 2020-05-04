import requests 
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=4ada227d2084bef19fb1c459fadd44a6'
    
    cities = City.objects.all()
    
    form = cityForm()

    if request.method == 'POST':
        form = cityForm(request.POST)
        if form.is_valid():
            form.save()


    weather_data = []
    


    for city in cities:
        r = requests.get(url.format(city)).json()
        try:
            city_weather = {
                'city': city.name,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon']
            }
            weather_data.append(city_weather)
        except:
            pass
    
    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather/index.html', context)

from django.shortcuts import render, redirect
import requests

from .forms import CityForm
from .models import City


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=00c684d3fef3d6d4412193d222573b1c'

    city = 'Dhaka'

    city_weather = requests.get(url.format(city)).json()  # request the API data and convert the JSON to Python data
    # types
    # print(city_weather)

    weather = {
        'city': city,
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']
    }

    # context = {'weather': weather}


    cities = City.objects.all()

    if request.method == 'POST':  # only true if form is submitted
        form = CityForm(request.POST)  # add actual request data to form for processing
        if form.is_valid():
            postCity = form.cleaned_data['name']
            city = requests.get(url.format(postCity)).json()
            if city['cod'] != '404':
                form.save()  # will validate and save if validate


    form = CityForm()
    weather_data = []

    for city in cities:
        city_weather = requests.get(
            url.format(city)).json()  # request the API data and convert the JSON to Python data types

        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }

        weather_data.append(weather)  # add the data for the current city into our list

    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'weather/index.html', context)  # returns the index.html template


def removeCity(request, city_name):
    city = City.objects.filter(name=city_name)
    city.delete()

    return redirect('index')

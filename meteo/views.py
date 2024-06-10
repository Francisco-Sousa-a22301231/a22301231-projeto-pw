import requests
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from datetime import datetime, timezone
from astral import LocationInfo
from astral.sun import sun
import pytz

def get_weather_data(global_id_local):
    url = f"https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{global_id_local}.json"
    response = requests.get(url)
    return response.json()

def get_city_list():
    url = "https://api.ipma.pt/open-data/distrits-islands.json"
    response = requests.get(url)
    return response.json()

def get_wind_details():
    url = "https://api.ipma.pt/open-data/wind-speed-daily-classe.json"
    response = requests.get(url)
    return response.json()

def get_weather_type_classes():
    url = "https://api.ipma.pt/open-data/weather-type-classe.json"
    response = requests.get(url)
    return response.json()

def index(request):
    cities_data = get_city_list()
    cities = cities_data['data']
    context = {'cities': cities}
    return render(request, 'meteo/index.html', context)

def weather_detail(request, city_id):
    days = []
    types = {}
    wind_details = {}
    wind_data_raw = get_wind_details()
    wind_data = wind_data_raw['data']
    weather_data_raw = get_weather_data(city_id)
    weather_data = weather_data_raw['data']
    weather_types_raw = get_weather_type_classes()
    weather_types = weather_types_raw['data']

    for wind_type in wind_data:
        wind_details[wind_type['classWindSpeed']] = wind_type['descClassWindSpeedDailyEN']
    for weather_type in weather_types:
        types[weather_type['idWeatherType']] = weather_type['descWeatherTypeEN']
    for day in weather_data:
        day['weatherType'] = types[day['idWeatherType']]
        day['windSpeed'] = wind_details[str(day['classWindSpeed'])]
        daytime = is_daytime(day['latitude'], day['longitude'])

        if day['idWeatherType'] < 10:
            day['idWeatherType'] = f"0{day['idWeatherType']}"

        if daytime:
            day['image'] = f"/media/meteo/w_ic_d_{day['idWeatherType']}anim.svg"
        else:
            day['image'] = f"/media/meteo/w_ic_n_{day['idWeatherType']}anim.svg"

        day['forecastDate'] = datetime.strptime(day['forecastDate'], '%Y-%m-%d')
        days.append(day)

    context = {
        'city' : search_for_city_name(city_id),
        'days': days,
    }
    return render(request, 'meteo/weather_detail.html', context)

def search_for_city_name(city_id):
    cities_data = get_city_list()
    cities = cities_data['data']

    for city in cities:
        if city['globalIdLocal'] == city_id:
            return city['local']
    return None

def is_daytime(lat, lon):
    location = LocationInfo(latitude=lat, longitude=lon)
    now = datetime.now(pytz.utc)
    s = sun(location.observer, date=now, tzinfo=pytz.utc)

    if s['sunrise'] <= now <= s['sunset']:
        return True
    else:
        return False

def api(request):
    return render(request, 'meteo/api.html', {})
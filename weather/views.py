import requests
import datetime
from django.shortcuts import render, redirect

from dotenv import load_dotenv
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Support env variables from .env file if defined
env_path = load_dotenv(os.path.join(BASE_DIR, '.env'))
load_dotenv(env_path)


def get_current_weather(weather_dict):
    details = {
        'city': weather_dict['resolvedAddress'],
        'icon': weather_dict['currentConditions']['icon'],
        'temp': weather_dict['currentConditions']['temp'],
        'condition': weather_dict['currentConditions']['conditions']
    }

    return details


def get_5_day_forecast(weather_dict):
    details = {}
    for i in range(5):
        date_str = weather_dict['days'][i]['datetime']
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        day = date_obj.strftime("%A")

        min_temp = weather_dict['days'][i]['tempmin']

        max_temp = weather_dict['days'][i]['tempmax']

        condition = weather_dict['days'][i]['conditions']

        icon = weather_dict['days'][i]['icon']

        details[f'day{i+1}'] = {
            'day': day,
            'mintemp': min_temp,
            'maxtemp': max_temp,
            'condition': condition,
            'icon': icon
        }

    return details


def index(request):
    WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
    if request.method == 'POST':        
        url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{{}}/next4days?unitGroup=metric&elements=datetime%2Cname%2Ctempmax%2Ctempmin%2Ctemp%2Cconditions%2Cicon&include=days%2Ccurrent&key={WEATHER_API_KEY}&contentType=json'
        city = request.POST.get('city', '')
        if city:
            unit = request.POST.get('unit', '')
            weather_dict = requests.get(url.format(city)).json()
            current_weather_dict = get_current_weather(weather_dict)
            forecast_weather_dict = get_5_day_forecast(weather_dict)

            days_forecast = []
            for key, values in forecast_weather_dict.items():
                if unit == 'F':
                    mintemp = round(values['mintemp'] * (9/5) + 32, 2)
                    maxtemp = round(values['maxtemp'] * (9/5) + 32, 2)
                else:
                    mintemp = values['mintemp']
                    maxtemp = values['maxtemp']
                day_forecast = {
                    'day': values['day'],
                    'mintemp': mintemp,
                    'maxtemp': maxtemp,
                    'condition': values['condition'],
                    'icon': values['icon']
                }
                days_forecast.append(day_forecast)
            if unit == 'F':
                current_temp = round(
                    current_weather_dict['temp'] * (9/5) + 32, 2)
                temp_unit = '°F'
            else:
                current_temp = current_weather_dict['temp']
                temp_unit = '°C'
            context = {
                'current_city': current_weather_dict['city'],
                'current_icon': current_weather_dict['icon'],
                'current_temp': current_temp,
                'temp_unit': temp_unit,
                'current_condition': current_weather_dict['condition'],
                'days': days_forecast
            }
            return render(request, 'weather/weather.html', context)
        else:
            return redirect(request.path)

    else:
        return render(request, 'weather/index.html')

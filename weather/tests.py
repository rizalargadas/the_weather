from django.test import TestCase
import datetime

# Create your tests here.
weather_dict = {
    'queryCost': 1,
    'latitude': 51.5064,
    'longitude': -0.12721,
    'resolvedAddress': 'London, England, United Kingdom',
    'address': 'London',
    'timezone': 'Europe/London',
    'tzoffset': 1.0,
    'days': [
        {'datetime': '2024-05-05', 'tempmax': 17.3, 'tempmin': 6.6,
            'temp': 12.3, 'conditions': 'Rain, Partially cloudy', 'icon': 'rain'},
        {'datetime': '2024-05-06', 'tempmax': 16.0, 'tempmin': 8.1,
            'temp': 12.3, 'conditions': 'Rain, Overcast', 'icon': 'rain'},
        {'datetime': '2024-05-07', 'tempmax': 20.3, 'tempmin': 11.8, 'temp': 15.4,
            'conditions': 'Partially cloudy', 'icon': 'partly-cloudy-day'},
        {'datetime': '2024-05-08', 'tempmax': 21.3, 'tempmin': 11.7, 'temp': 16.1,
            'conditions': 'Partially cloudy', 'icon': 'partly-cloudy-day'},
        {'datetime': '2024-05-09', 'tempmax': 19.2, 'tempmin': 11.6, 'temp': 14.8,
            'conditions': 'Partially cloudy', 'icon': 'partly-cloudy-day'}
    ],
    'currentConditions': {
        'datetime': '00:56:00',
        'temp': 9.8,
        'conditions': 'Clear',
        'icon': 'clear-night'
    }
}


city = weather_dict['resolvedAddress']
icon = weather_dict['currentConditions']['icon']
temp = weather_dict['currentConditions']['temp']
condition = weather_dict['currentConditions']['conditions']

# print(city)
# print(f'{icon} | {temp} | {condition}')


# def get_current_weather(weather_dict):
#     details = {
#         'city': weather_dict['resolvedAddress'],
#         'icon': weather_dict['currentConditions']['icon'],
#         'temp': weather_dict['currentConditions']['temp'],
#         'condition': weather_dict['currentConditions']['conditions']
#     }

#     return details


# current_weather_dict = get_current_weather(weather_dict)
# print(current_weather_dict['city'])
# min_temp = weather_dict['days'][0]['tempmin']
# max_temp = weather_dict['days'][0]['tempmax']
# condition = weather_dict['days'][0]['conditions']
# icon = weather_dict['days'][0]['icon']


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


forecast_weather_dict = get_5_day_forecast(weather_dict)
days_forecast = []
for key, values in forecast_weather_dict.items():
    day_forecast = {
        'day_name': values['day'],
        'min_temp': values['mintemp'],
        'max_temp': values['maxtemp'],
        'condition': values['condition'],
        'icon': values['icon']
    }
    days_forecast.append(day_forecast)

# Context for the template
context = {
    'days': days_forecast
}

days = [{'day_name': 'Sunday', 'min_temp': 6.6, 'max_temp': 17.3, 'condition': 'Rain, Partially cloudy', 'icon': 'rain'}, {'day_name': 'Monday', 'min_temp': 8.1, 'max_temp': 16.0, 'condition': 'Rain, Overcast', 'icon': 'rain'}, {'day_name': 'Tuesday', 'min_temp': 11.8, 'max_temp': 20.3,
                                                                                                                                                                                                                                     'condition': 'Partially cloudy', 'icon': 'partly-cloudy-day'}, {'day_name': 'Wednesday', 'min_temp': 11.7, 'max_temp': 21.3, 'condition': 'Partially cloudy', 'icon': 'partly-cloudy-day'}, {'day_name': 'Thursday', 'min_temp': 11.6, 'max_temp': 19.2, 'condition': 'Partially cloudy', 'icon': 'partly-cloudy-day'}]

for day in days:
    print(day.icon)

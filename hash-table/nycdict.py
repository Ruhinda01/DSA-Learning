#!/usr/bin/python3

weather_obj = {}

with open('nyc_weather.csv', 'r') as f:
    for line in f:
        token = line.split(',')
        date = token[0]
        try:
            temperature = int(token[1])
            weather_obj[date] = temperature
        except:
            print('Conversion error')

print(weather_obj)
print(weather_obj['Jan 9'])
print(weather_obj['Jan 4'])

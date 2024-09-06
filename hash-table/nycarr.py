#!/usr/bin/python3

arr = []
with open('nyc_weather.csv', 'r') as f:
    for line in f:
        token = line.split(',')
        try:
            temperature = int(token[1])
            arr.append(temperature)
        except:
            print('Conversion error')

print(arr)
print(sum(arr[0:7])/len(arr[0:7]))
print(max(arr))
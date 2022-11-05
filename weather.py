# pylint: disable=missing-module-docstring

import sys
import requests

BASE_URI = "https://weather.lewagon.com"


def search_city(query):
    '''Look for a given city. If multiple options are returned, have the user choose between them.
       Return one city (or None)
    '''
    query = query.strip()
    response = requests.get(BASE_URI+"/geo/1.0/direct?q="+query+"&limit=10").json()

    if response != []:
        if len(response) > 1 :
            for index, item in enumerate(response):
                print(f"{index+1}. {item.get('name')},{item.get('country')}")

            print("Multiple matches found, which city did you mean?")
            index_input = input("")
            index_input =int(index_input)-1

            return response[index_input]

        else:
            return response[0]

    return None

def weather_forecast(lat, lon):
    '''Return a 5-day weather forecast for the city, given its latitude and longitude.'''
    lat_str = str(lat)
    lon_str = str(lon)
    response = requests.get(BASE_URI+"/data/2.5/forecast?lat="+lat_str+"&lon="+lon_str+"&units=metric").json()
    if response != []:
        return response.get('list')

    return None

def main():
    '''Ask user for a city and display weather forecast'''
    while True:
        query = input("City?\n> ")
        city = search_city(query)
        if city is not None :
            break

    five_day_weather = weather_forecast(city.get('lat'),city.get('lon'))

    print(f"Here's the weather in {city.get('name')}")
    for weather in five_day_weather:
        print( f"{weather.get('dt_txt').split(' ')[0]} {weather.get('weather')[0]['description']} {get('main').get('temp_max')}°C")

if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)

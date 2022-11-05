import requests

url = "https://weather.lewagon.com/geo/1.0/direct?q=Barcelona"
response = requests.get(url).json()
print(response)
city = response[0]
print(city)
print(f"{city['name']}: ({city['lat']}, {city['lon']})")
print(type(city['lat']))

import requests

API_KEY='10cd51b2840ed07b12df4bcd2771c464'
city_name= input('enter the name of the city: ')

url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

response=requests.get(url)
print(response)

if response.status_code == 200:
    weather_data = response.json()
    weather_disc = weather_data['weather'][0]['description']
    temp= weather_data['main']['temp'] - 273.15
    print(f'Weather in {city_name} : {temp} *C with {weather_disc} ')

else:
    print(f'City name{city_name} is not found or incorrect')
# Weather App (Requires API key from OpenWeather)
import requests
city = input("Enter city: ")
res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY&units=metric").json()
print(f"Weather in {city}: {res['weather'][0]['description']}, {res['main']['temp']}°C")

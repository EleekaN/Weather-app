import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
    print("----Get Current Weather----")
    city = input("\n Enter City Name: ")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    # print(request_url)
    weather_data = requests.get(request_url).json()

    # pprint(weather_data)
    print(f'Current weather for {weather_data['name']}')
    print(f'Temperature is: {weather_data['main']['temp']}')

if __name__ == '__main__':
    get_current_weather()
import requests
import json


def get_weather(location):
    try:
        url = f"http://api.weatherstack.com/current?access_key=887f99e739d3cf04471da33a2f752636&query=Taipei&units=m"
        response = requests.request("GET", url)
        data = json.loads(response.text)
        return data
    except Exception as e:
        print(f"Error: {e}")

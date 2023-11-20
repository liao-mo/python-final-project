import requests
from datetime import datetime
import json

python_group_api_key = "aXeGGuxXR4KFNZlMXg0yfvIwD2ledWRD3mQI0L2Sume"


def send_image(image_path):
    try:
        # Open the image file in binary mode
        with open(image_path, "rb") as image_file:
            # Create a dictionary with the form data
            api_endpoint = "https://notify-api.line.me/api/notify?message= "
            files = {"imageFile": (image_path, image_file, "image/png")}
            headers = {"Authorization": f"Bearer {python_group_api_key}"}
            # Make a POST request with the image file as form data
            response = requests.post(api_endpoint, headers=headers, files=files)

        # Check the response
        if response.status_code == 200:
            print("Image uploaded successfully!")
        else:
            print(f"Error uploading image. Status code: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"Error: {e}")


def send_message(message):
    try:
        api_endpoint = f"https://notify-api.line.me/api/notify?message={message}"
        headers = {"Authorization": f"Bearer {python_group_api_key}"}
        # Make a POST request
        response = requests.post(api_endpoint, headers=headers)

        # Check the response
        if response.status_code == 200:
            print("Message uploaded successfully!")
        else:
            print(f"Error sending image. Status code: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"Error: {e}")


def get_weather(location):
    try:
        url = f"http://api.weatherstack.com/current?access_key=887f99e739d3cf04471da33a2f752636&query=Taipei&units=m"
        response = requests.request("GET", url)
        data = json.loads(response.text)
        return data
    except Exception as e:
        print(f"Error: {e}")

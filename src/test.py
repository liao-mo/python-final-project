from utility import *
from lineNotify import *

image_path = r"C:\Users\Hank\Desktop\常用素材\ETH.png"


# Call the function from the module
# send_image(image_path)
# send_message("你好哇")
weather_response_json = get_weather("Taipei")

location = "Taipei"
temperature = weather_response_json["current"]["temperature"]
feelslike = weather_response_json["current"]["feelslike"]
wind_speed = weather_response_json["current"]["wind_speed"]
humidity = weather_response_json["current"]["humidity"]
uv_index = weather_response_json["current"]["uv_index"]
weather_info = f"目前{location}的溫度是攝氏{temperature}度，感覺像是{feelslike}度，風速{wind_speed}km/h，濕度{humidity}%，紫外線指數{uv_index}"

user = LineNotify("aXeGGuxXR4KFNZlMXg0yfvIwD2ledWRD3mQI0L2Sume")
# user.send_message("test")

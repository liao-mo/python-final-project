from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from lineNotify import *

# PyOWN config settings
config_dict = get_default_config()
config_dict["language"] = "eg"

# PyOWN library initialization
owm = OWM("99e4d2e13a3796fc853c6f84f51cc68c", config_dict)
mgr = owm.weather_manager()
mgr_uv = owm.uvindex_manager()

# This only runs on python 3.7 - 3.9
# reg = owm.city_id_registry()
# list_of_locations = reg.locations_for("Taipei", country="TW", matching="exact")
# taipei = list_of_locations[0]
# lat = taipei.lat
# lon = taipei.lon

lat = 24.94702
lon = 121.581749

my_city_id = 1665148  # Taipei
w = mgr.weather_at_id(my_city_id).weather
uvi = mgr_uv.uvindex_around_coords(lat, lon)

# Present weather observation data
print("天氣: {}".format(w.status))
print("天氣狀況詳細說明: {}".format(w.detailed_status))
print("氣溫(℃): {}".format(w.temperature("celsius").get("temp", 0)))
print("最高氣溫(℃): {}".format(w.temperature("celsius").get("temp_max", 0)))
print("最低氣溫(℃): {}".format(w.temperature("celsius").get("temp_min", 0)))
print("體感溫度(℃): {}".format(w.temperature("celsius").get("feels_like", 0)))
print("濕度(%): {}".format(w.humidity))
print("風速(m/s): {}".format(w.wind().get("speed", 0)))
print("UV值: {}".format(uvi.value))
print("UV危險度: {}".format(uvi.get_exposure_risk()))


def get_weather():
    return w.status


def get_weather_detail():
    return w.detailed_status


def get_temperature():
    return w.temperature("celsius").get("temp", 0)


def get_temperature_max():
    return w.temperature("celsius").get("temp_max", 0)


def get_temperature_min():
    return w.temperature("celsius").get("temp_min", 0)


def get_feels_like():
    return w.temperature("celsius").get("feels_like", 0)


def get_humidity():
    return w.humidity


def get_wind_speed():
    return w.wind().get("speed", 0)


def get_uv_value():
    return uvi.value


def get_uv_exposure_risk():
    return uvi.get_exposure_risk()

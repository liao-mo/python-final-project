from pyowm.owm import OWM
from pyowm.utils import formatting
from pyowm.utils.config import get_default_config

#  PyOWMのコンフィグ設定
config_dict = get_default_config()
config_dict["language"] = "eg"  # 取得データの言語設定

# PyOWMライブラリの初期化
owm = OWM("99e4d2e13a3796fc853c6f84f51cc68c", config_dict)
mgr = owm.weather_manager()
mgr_uv = owm.uvindex_manager()

# This doesn't work on windows, don't know why...
# reg = owm.city_id_registry()
# list_of_locations = reg.locations_for('Taipei', country='TW', matching='exact')
# taipei = list_of_locations[0]
# lat = taipei.lat   # lat=24.94702
# lon = taipei.lon   # lon=121.581749

lat = 24.94702
lon = 121.581749

my_city_id = 1665148  # Taipei
w = mgr.weather_at_id(my_city_id).weather
uvi = mgr_uv.uvindex_around_coords(lat, lon)

# 現在の気象データを取得
# observation = mgr.weather_at_place("Taipei,TW")


# w = observation.weather
# w = taipei.weather
# print("気象データの計測日次時間(unixTime): {}".format(w.ref_time))
# print("気象データの計測日次時間(date): {}".format(formatting.to_date(w.ref_time)))
# print("天気コード: {}".format(w.weather_code))
print("天気: {}".format(w.status))
print("天気詳細: {}".format(w.detailed_status))
# print("気温(K): {}".format(w.temperature()))
print("気温(℃): {}".format(w.temperature("celsius").get("temp", 0)))
print("最高気温(℃): {}".format(w.temperature("celsius").get("temp_max", 0)))
print("最低気温(℃): {}".format(w.temperature("celsius").get("temp_min", 0)))
print("体感気温(℃): {}".format(w.temperature("celsius").get("feels_like", 0)))
print("湿度(%): {}".format(w.humidity))
# print("気圧(hPa): {}".format(w.barometric_pressure()))
print("風速(m/s): {}".format(w.wind().get("speed", 0)))

# print("雲量: {}".format(w.clouds))
# print("雨量: {}".format(w.rain))
# print("積雪量: {}".format(w.snow))

print("UV値: {}".format(uvi.value))
print("UV危険度: {}".format(uvi.get_exposure_risk()))

"""
uvi.get_value()
uvi.get_reference_time()
uvi.get_reception_time()
uvi.get_exposure_risk()
"""


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

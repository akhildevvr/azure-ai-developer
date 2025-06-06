import requests
from semantic_kernel.functions import kernel_function
from typing import Annotated

class WeatherPlugin:

    @kernel_function(description="Get weather conditions for past 16 days", name="get_weather_past")
    def get_weather_past(self, latitude: Annotated[int, "The latitude of the location"], 
                               longitude: Annotated[int, "The Longitude of the location"],
                               days: Annotated[int, "The number of days to get weather data for"]):
        url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={latitude}&longitude={longitude}"
            f"&daily=weather_code,temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,"
            f"sunrise,sunset,daylight_duration,uv_index_max,precipitation_sum,rain_sum,showers_sum,snowfall_sum,"
            f"precipitation_hours,wind_speed_10m_max,wind_gusts_10m_max"
            f"&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch"
            f"&past_days={days}"
        )
        response = requests.get(url)
        return response.json()

    @kernel_function(description="Get weather conditions for future 16 days", name="get_weather_future")
    def get_weather_future(self, latitude: Annotated[int, "The latitude of the location"], 
                                 longitude: Annotated[int, "The Longitude of the location"],
                                 days: Annotated[int, "The number of days to get weather data for"]):
        url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={latitude}&longitude={longitude}"
            f"&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,rain,showers,snowfall,weather_code,"
            f"wind_speed_10m,wind_direction_10m,wind_gusts_10m"
            f"&hourly=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation_probability,precipitation,rain,showers,"
            f"snowfall,weather_code,cloud_cover,wind_speed_10m,uv_index"
            f"&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch"
            f"&forecast_days={days}"
        )
        response = requests.get(url)
        return response.json()
import pprint
import requests
from dateutil.parser import parse
from datetime import datetime

#TODO: add wrapper class CachedForecast
class YahooWeatherForecast:
    weather_url_template = "https://query.yahooapis.com/" \
                           "v1/public/yql" \
                           "?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(" \
                           "select%20woeid%20from%20geo.places(1)%20where%20text%3D%22{city_name}%22" \
                           ")" \
                           "%20and%20u%3D'c'&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"

    def __init__(self):
        self._city_cache = {}

    def get(self, city_name):
        if city_name in self._city_cache:
            return self._city_cache[city_name]

        forecast_data = self._get_forecast_json(city_name)
        forecast = []
        for day_data in forecast_data:
            forecast.append(self._convert_day_forecast_to_dict(day_data))

        self._city_cache[city_name] = forecast

        return forecast

    def _get_forecast_json(self, city_name):
        print('Yahoo request')
        weather_url = YahooWeatherForecast.weather_url_template.format(city_name=city_name)
        data = requests.get(weather_url).json()
        return data['query']['results']['channel']['item']['forecast']


    def _convert_day_forecast_to_dict(self, day_data):
        return {
            "date": parse(day_data['date']),
            #"low_temperature": day_data['low'],
            "high_temperature": day_data['high']
        }


class CityInfo:
    def __init__(self, forecast_service: YahooWeatherForecast):
        self._forecast_service = forecast_service

    def weather_forecast(self, city_name):
        return self._forecast_service.get(city_name)


def _main():
    forecast_service = YahooWeatherForecast()
    city_info = CityInfo(forecast_service)

    for i in range(5):
        forecast = city_info.weather_forecast("Kyiv")
        pprint.pprint(forecast)


if __name__ == '__main__':
    _main()


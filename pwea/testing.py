import requests
import argparse

from rich import print
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel

from key import KEY
from WeatherCard import WeatherCard
from WeatherCard import DailyForecastCard


def get_weather(report_type='current', location='Warwick'):
    base_url = f'https://api.weatherapi.com/v1'
    weather_report = requests.get(f"{base_url}/{report_type}.json?key={KEY}"
                                  f"&q={location}&aqi=yes")
    return weather_report


def main():
    parser = argparse.ArgumentParser(
        usage='pwea [location]',
        description="description: pwea is a simple tool used to retrieve"
        "current weather weather_reportrmation")

    parser.add_argument('location', nargs='+',
                        help="Input a city name, US/UK/Canadian postal code,"
                        "IP address, or Latitude / Longitude (in decimal"
                        "degree)")
    parser.add_argument("-t" "--type", dest="report_type", default="current")
    parser.add_argument("-u", "--unit", dest = "unit", default="metric")
    parser.add_argument ("-v", "--verbosity", dest = "verbosity",
                         action="count", default = 2)

    args = parser.parse_args()

    unit = args.unit
    location = ' '.join(args.location)
    weather_report = get_weather(args.report_type, location).json()
    #print(weather_report)
    #print(WeatherCard(weather_report, unit, args.verbosity))
    forecast = ForecastCard(weather_report, unit, args.verbosity)

if __name__ == '__main__':
    main()

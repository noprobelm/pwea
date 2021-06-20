import json
from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from rich import print
from pwea.ascii_images import ascii_dict


class WeatherCard:

    def __init__(self, weather_report):
        self.weather_report = weather_report
        self.ascii_image = ascii_dict[weather_report['current']['condition']['text'].replace(' ', '_').lower()]
        self.weather_renderables = [Panel(f"[#5fd7d7]{weather_report['location']['name']}, {weather_report['location']['region']}, {weather_report['location']['country']}\n" \
                                          f"The current time is {weather_report['location']['localtime']}\n\n" \
                                          f"[underline bold]Weather report (last updated at {weather_report['current']['last_updated']}):\n\n[/#5fd7d7][/underline bold]" \
                                          f"{self.ascii_image}\n" \
                                          f"[indian_red]{weather_report['current']['temp_f']}°F ({weather_report['current']['feelslike_f']}°F), {weather_report['current']['condition']['text']}\n" \
                                          f"Humidity: {weather_report['current']['humidity']}%\tPressure: {weather_report['current']['pressure_in']} mmHg\n" \
                                          f"UV Index: {weather_report['current']['uv']}\n" \
                                          f"Current wind speed is {weather_report['current']['wind_mph']} mph to the {weather_report['current']['wind_dir']} ({weather_report['current']['wind_degree']} degrees)")]
        self.columns = Columns(self.weather_renderables)
        return None

    def display_weather(self):

        console = Console()
        console.print(Columns(self.weather_renderables))

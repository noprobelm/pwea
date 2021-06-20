import json
from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from rich import print
from pwea.ascii_art import ascii_dict


class WeatherCard:

    def __init__(self, weather_report):
        self.weather_report = weather_report
        self.ascii_image = ascii_dict[weather_report['current']['condition']
                                      ['text'].replace(' ', '_').lower()]
        self.display_text = (
            f"[#5fd7d7]{weather_report['location']['name']}, "
            f"{weather_report['location']['region']}, "
            f"{weather_report['location']['country']}\nThe current time is"
            f"{weather_report['location']['localtime']}\n\n[underline bold]"
            f"Weather report (last updated at)"
            f"{weather_report['current']['last_updated']})\n\n[/#5fd7d7]"
            f"[/underline bold] {self.ascii_image}\n[indian_red]"
            f"{weather_report['current']['temp_f']}°F "
            f"{weather_report['current']['feelslike_f']}°F), "
            f"{weather_report['current']['condition']['text']}\nHumidity: "
            f"{weather_report['current']['humidity']}%\tPressure: "
            f"{weather_report['current']['pressure_in']} mmHg\nUV Index: "
            f"{weather_report['current']['uv']}\nCurrent wind speed is "
            f"{weather_report['current']['wind_mph']} mph to the "
            f"{weather_report['current']['wind_dir']} "
            f"({weather_report['current']['wind_degree']} degrees)"
        )
        self.weather_renderables = [Panel(self.display_text)]

        self.columns = Columns(self.weather_renderables)
        return None

    def display_weather(self):

        print(self.display_text)
        console = Console()
        console.print(Columns(self.weather_renderables))
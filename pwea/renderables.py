from datetime import *
from pwea.ascii_art import ascii_art


def set_renderables(reports):
    """Main function for handling the setting of renderables. This
    will probably later be turned into a series of config files which
    will contain the theme and display format for the weather data,
    selectable by the user using argparser.

    Returns a nested dict object containing the requested location,
    current weather report, and forecasted weather report.

    """

    def set_current_renderables(location, report):
        """Sets renderables for the *current* weather report. Uses the
        ascii art this module imported to this module by default."""
        if report["is_day"]:
            ascii_renderables = ascii_art["day"]
        else:
            ascii_renderables = ascii_art["night"]

        report['localtime'] = (
            report['localtime'].strftime('%A, %B, %e, %Y, %H:%M')
            )
        report['last_updated'] = (
            report['last_updated'].strftime('%H:%M')
            )

        renderables = (
            f"[indian_red]"
            f"[underline][bold]{report['localtime']}[/underline][/bold]\n\n"
            f"In "
            f"{location['city']}, "
            f"{location['region']} "
            f"it is {report['condition'].lower()}.\n\n"
            f"[/indian_red]"
            f"{ascii_renderables[report['condition'].replace(' ', '_').lower()]}\n\n"
            f"[indian_red]"
            f"{report['temp_f']}°F "
            f"({report['temp_c']}°C)\n"
            f"Humidity: {report['humidity']}\n"
            f"Pressure: {report['pressure_in']}\n"
            f"UV Index: {report['uv']}\n"
            f"Current wind speed is {report['wind_mph']} mph "
            f"({report['wind_kph']} kph) to the {report['wind_dir']} "
        )
        return renderables

    def set_forecast_renderables(location, report):
        """Sets renderables for the *forecasted* weather report. Uses the
        ascii art this module imported to this module by default."""
        ascii_renderables = ascii_art["day"]
        renderables = {}
        for day in report:
            renderables[day] = (
                f"[indian_red]"
                f"{location['city']}, "
                f"{location['region']}, "
                f"{location['country']}\n"
                f"\n\n"
                f"[/indian_red]"
                f"{ascii_renderables[report[day]['condition']['text'].replace(' ', '_').lower()]}\n\n"
                f"[indian_red]"
                f"High: "
                f"{report[day]['maxtemp_f']}°F ({report[day]['maxtemp_c']}°C)\n"
                f"Low: "
                f"{report[day]['mintemp_f']}°F ({report[day]['mintemp_c']}°C).\n"
                f"Average: {report[day]['avgtemp_f']}°F ({report[day]['avgtemp_c']}°C).\n"
                f"Humidity: {report[day]['avghumidity']}\n"
                f"Wind speed: {report[day]['maxwind_mph']} mph ({report[day]['maxwind_kph']}) kph\n"
                f"Visibility: {report[day]['avgvis_miles']} mi ({report[day]['avgvis_km']} km)"
            )
        return renderables

    renderables = {"current": set_current_renderables(reports["location"],
                                                      reports["current"]),
                   "forecast": set_forecast_renderables(reports["location"],
                                                        reports["forecast"])}
    return renderables

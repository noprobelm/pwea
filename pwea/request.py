import requests
from datetime import *
from pwea.config import get_config


def get_data(args):
    """Main function for getting and parsing the weather report. This
    will probably eventually migrate to a separate config file if
    better support for custom APIs is implemented.
    """

    def request_json():
        """ Instantiates a requests object of the current and
        forecasted weather report. """
        KEY = get_config()

        base_url = "https://api.weatherapi.com/v1"
        weather_request = requests.get(f"{base_url}/forecast.json?key={KEY}"
                                    f"&q={args.location}&days=3&aqi=yes").json()
        return weather_request

    def parse_json(weather_request):
        """Parses the json from the request object into something the
        WeatherCurrent and WeatherForecast class recognizes
        """
        # dict indicating the location data of the report
        location = {
            "city": weather_request["location"]["name"],
            "region": weather_request["location"]["region"],
            "country": weather_request["location"]["country"]
        }
        weather_request_current = weather_request["current"]
        weather_report = {
            "localtime": datetime.strptime(
                weather_request["location"]["localtime"],
                '%Y-%m-%d %H:%M'
            ),
            # boolean
            "is_day": weather_request_current["is_day"],
            # timestamp
            "last_updated": datetime.strptime(
                weather_request_current["last_updated"],
                '%Y-%m-%d %H:%M'
            ),
            # All nums are floats unless specified otherwise
            "temp_c": weather_request_current["temp_c"],
            "temp_f": weather_request_current["temp_f"],
            "condition": weather_request_current["condition"]["text"],
            "wind_mph": weather_request_current["wind_mph"],
            "wind_kph": weather_request_current["wind_kph"],
            "wind_degree": weather_request_current["wind_degree"],
            # int
            "wind_dir": weather_request_current["wind_dir"],
            "pressure_mb": weather_request_current["pressure_mb"],
            "pressure_in": weather_request_current["pressure_in"],
            "precip_mm": weather_request_current["precip_mm"],
            "precip_in": weather_request_current["precip_in"],
            "humidity": weather_request_current["humidity"],
            # int
            "cloud": weather_request_current["cloud"],
            "feelslike_c": weather_request_current["feelslike_c"],
            "feelslike_f": weather_request_current["feelslike_f"],
            "vis_km": weather_request_current["vis_km"],
            "vis_miles": weather_request_current["vis_miles"],
            "uv": weather_request_current["uv"],
            "gust_mph": weather_request_current["gust_mph"],
            "gust_kph": weather_request_current["gust_kph"]
        }
        weather_request_forecast = weather_request["forecast"]["forecastday"]
        forecast_report = {}
        for day in range(len(weather_request_forecast)):
            forecast_report[day] = {
                "date": weather_request_forecast[day]["date"],
                "maxtemp_c": weather_request_forecast[day]["day"]["maxtemp_c"],
                "maxtemp_f": weather_request_forecast[day]["day"]["maxtemp_f"],
                "mintemp_c": weather_request_forecast[day]["day"]["mintemp_c"],
                "mintemp_f": weather_request_forecast[day]["day"]["mintemp_f"],
                "avgtemp_c": weather_request_forecast[day]["day"]["avgtemp_c"],
                "avgtemp_f": weather_request_forecast[day]["day"]["avgtemp_f"],
                "maxwind_mph": weather_request_forecast[day]["day"]["maxwind_mph"],
                "maxwind_kph": weather_request_forecast[day]["day"]["maxwind_kph"],
                "totalprecip_mm": weather_request_forecast[day]["day"]["totalprecip_mm"],
                "totalprecip_in": weather_request_forecast[day]["day"]["totalprecip_in"],
                "avgvis_km": weather_request_forecast[day]["day"]["avgvis_km"],
                "avgvis_miles": weather_request_forecast[day]["day"]["avgvis_miles"],
                "avghumidity": weather_request_forecast[day]["day"]["avghumidity"],
                "condition": weather_request_forecast[day]["day"]["condition"]
            }
        reports = {"location": location, "current": weather_report,
                   "forecast": forecast_report}
        return reports

    weather_request = request_json()
    reports = parse_json(weather_request)
    return reports

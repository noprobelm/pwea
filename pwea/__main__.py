from pwea.argparser import parse_args
from pwea.request import get_data
from pwea.renderables import set_renderables
from pwea.config import set_config, get_config
from pwea.Weather import CurrentWeather, ForecastWeather

from rich import print
from rich.panel import Panel


def main():
    """Main function to handle pwea. Creates args, generates weather
    report and console renderables, then renders the weather report."""
    args = parse_args()
    if not args.config:
        reports = get_data(args)
        renderables = set_renderables(reports)
        if args.report_type == "current":
            print(CurrentWeather(renderables["current"]))
        else:
            print(ForecastWeather(renderables["forecast"], "indian_red"))
    else:
        set_config(args.config)


if __name__ == '__main__':
    main()

import argparse
import os
import sys
from pwea.config import check_config


def parse_args():
    """Main function for parsing args. Utilizes the 'check_config'
    function from the config module to ensure an API key has been
    passed. If not, user is prompted to conduct initial configuration
    for pwea.

    If a valid configuration is found (there is currently no validity
    check for the API key, argparser will look for location and
    optional arguments. Location is required. Default weather report
    is current, forecast can be specified using -t)

    """
    if check_config():
        parser = argparse.ArgumentParser(
            usage='pwea [location] <optional args>',
            description="description: pwea is a simple tool used to retrieve"
            "current and forecasted weather information")
        parser.add_argument('location', nargs='+',
                            help="Input a city name or US/UK/Canadian postal code")
        parser.add_argument("-t" "--type", dest="report_type", default="current",
                            help="Acceptable report types are 'current' or 'forecast'. Default is 'current'")
        parser.add_argument('--config', dest='config', default=None,
                            help="Pass your API key for https://weatherapi.com")
        args = parser.parse_args()
        args.location = ' '.join(args.location)
        args.report_type = args.report_type.lower()
    else:
        parser = argparse.ArgumentParser(
            usage='No API key found in ~/.config/pwearc. Please set your API key using pwea --config <API_KEY>',
            description="description: pwea is a simple tool used to retrieve"
            "current and forecasted weather information")
        parser.add_argument('--config', dest='config', required=True,
                            help="Pass your API key for https://weatherapi.com")
        args = parser.parse_args()

    return args

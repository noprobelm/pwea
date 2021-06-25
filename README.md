# Pwea 

Pwea is a simple weather tool written in Python, utilizing the [Weather API](https://www.weatherapi.com/) to source current weather information.

Pwea uses the [requests](https://docs.python-requests.org/en/master/) and [rich](https://github.com/willmcgugan/rich) libraries to retrieve and display weather data.

# How it works

Simply pass a desired location for weather data. Acceptable arguments are US/Canadian/UK zip code, IP address, latitude/longitude (in decimal degree), or city name. Multiple arguments are acceptable to assist in specifying location.

Use it like this:

`pwea springfield MA`

![springfield](pwea.gif)

# Installation

You can install pwea from PyPi, or build it from source.

## Pypi

`pip install pwea`

## Building from source

Clone the repository:

`git clone https://gitlab.com/jeffreybarfield/pwea.git`

Install using `setuptools`:

`python3 setup.py install`

# Credit

I created this tool for the purpose of self-education. I was originally inspired by the [pwy](https://github.com/clieg/pwy) project.

# License

Copyright © 2021 Jeff Barfield.


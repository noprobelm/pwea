# Pwea 

Pwea is a simple weather tool written in Python, utilizing the [Weather API](https://www.weatherapi.com/) to source current weather information.

Pwea uses the [requests](https://docs.python-requests.org/en/master/) and [rich](https://github.com/willmcgugan/rich) libraries to retrieve and display weather data.

# How it works

Pass a desired location to `pwea` to retrieve the current weather information. For forecast information, add `-t forecast` or `--type forecast`.

Use it like this:

`pwea new york`

![current](current.gif)

![forecast](forecast.gif)

# Installation

- Clone the repository:

`git clone https://gitlab.com/jeffreybarfield/pwea.git`

- Install using `setuptools`:

`python3 setup.py install`

# Configuration

- Get a free API key from [weatherapi.com](https://www.weatherapi.com/)
- Configure pwea to run: `pwea --config <YOUR_API_KEY>`, or manually put your key in `~/.config/pwearc`

# Credit

I created this tool to educate myself on the Rich library. I was originally inspired by the [pwy](https://github.com/clieg/pwy) project.

# License

Copyright © 2021 Jeff Barfield.


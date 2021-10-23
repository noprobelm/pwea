import os
import sys


def set_config(KEY):
    home = os.path.expanduser("~")
    config = open(f"{home}/.config/pwearc", "w")
    config.write(KEY)
    config.close()


def get_config():
    home = os.path.expanduser("~")
    config = open(f"{home}/.config/pwearc", "r")
    KEY = config.read()
    return KEY


def check_config():
    home = os.path.expanduser("~")
    try:
        config = open(f"{home}/.config/pwearc", "r")
        config.close()
        return True
    except FileNotFoundError:
        return False

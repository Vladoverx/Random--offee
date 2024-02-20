"""
This file handles telegram token reading from JSON file.
"""
import json

with open(r'.vscode\config.json') as config_data:
    CONFIG = json.load(config_data)


def get_token():
    return CONFIG['bot']['token']
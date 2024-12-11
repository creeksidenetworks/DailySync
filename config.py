#!/usr/bin/env python
# Daily file sync utility
# Copyright (c) 2024 Jackson Tong, Creekside Networks LLC.

import json
import configparser

def remove_quotes(value):
    """
    Removes quotes from the beginning and end of a string if they exist.

    :param value: The string value to process
    :return: The string value without surrounding quotes
    """
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1]
    return value

def read_config(config_path):
    """
    Reads the configuration file from the given path and removes quotes from values.

    :param config_path: Path to the config.ini file
    :return: ConfigParser object with the configuration
    """
    config = configparser.ConfigParser()
    config.read(config_path)

    return config

    # Remove quotes from all values
    for section in config.sections():
        for key in config[section]:
            config[section][key] = remove_quotes(config[section][key])

# Debug
if __name__ == "__main__":
    config_path = './cfg/config.ini'
    config = read_config(config_path)
    print(json.dumps(config._sections, indent=4))
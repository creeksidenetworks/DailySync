#!/usr/bin/env python
# Daily file sync utility
# Copyright (c) 2024 Jackson Tong, Creekside Networks LLC.

import os
import json
import argparse

from config import read_config
from logger import get_logger, logger

def main():

    # main scripts started here
    title = """
***************************************************************************
*                   Linux Daily Sync Utility v1.0                         *
*          (c) 2024-2024 Jackson Tong, Creekside Networks LLC             *
***************************************************************************

"""
    print(title)

    parser = argparse.ArgumentParser(description='Linux daily file sync utility')
    parser.add_argument('--config', type=str, default='./cfg/config.ini', help='Path to the configuration file')
    args = parser.parse_args()

    config_file_path = os.path.abspath(args.config)
    root_dir = os.path.dirname(os.path.dirname(config_file_path))

    log_dir = os.path.join(root_dir, 'logs')
    logger = get_logger(log_dir)
    config = read_config(config_file_path)
    print(json.dumps(config._sections, indent=4))

if __name__ == "__main__":
    main()
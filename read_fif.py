#!/usr/local/bin/python3

import mne
import numpy as np
import json
import os
import shutil

# Load inputs from config.json
with open('config.json') as config_json:
    config = json.load(config_json)

tmp = dict((k, None) for k, v in config.items() if v == "")
config.update(tmp)

print(config['list_of_integers'][0])
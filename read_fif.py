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

picks = config['list_of_integers']
if isinstance(picks, str) and picks.find("[") != -1 and picks is not None:
    picks = picks.replace('[', '')
    picks = picks.replace(']', '')
    picks = picks.replace("'", '')
    config['list_of_integers'] = list(map(str, picks.split(', ')))
#!/usr/local/bin/python3

import mne
import numpy as np
import json
import os
import shutil
import pandas as pd


# Load inputs from config.json
with open('config.json') as config_json:
    config = json.load(config_json)

print('yeeeah')

# data_file = config.pop('ds')
# raw_ctf = mne.io.read_raw(data_file)
# raw_ctf.save('test_raw.fif')

# list_keys = list(config['reject'].keys())
# list_keys = [k[:-1] for k in list_keys] 
# print(list_keys)

# test = dict((k.replace("'", ""), v) for k, v in config['reject'].items())
# print(test)

# tmp = dict((k, None) for k, v in config.items() if v == "")
# config.update(tmp)

# picks = config['list_of_integers']
# print(picks)
# if isinstance(picks, str) and picks.find("[") != -1 and picks is not None:
#     picks = picks.replace('[', '')
#     picks = picks.replace(']', '')
#     picks = picks.replace("'", '')
#     config['list_of_integers'] = list(map(str, picks.split(', ')))
# print(config['list_of_integers'])
# print(config['list_of_integers'][0])
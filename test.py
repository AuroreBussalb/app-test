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


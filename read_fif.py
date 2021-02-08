#!/usr/local/bin/python3

import mne
import json

# Load inputs from config.json
with open('config.json') as config_json:
    config = json.load(config_json)

# Read the files
data_file = str(config.pop('input_raw'))
raw = mne.io.read_raw_fif(data_file, allow_maxshield=True)

# Save file
raw.save(raw.filenames[0].replace('.fif', 'test-raw.fif'))

#!/usr/local/bin/python3

import mne
import json


# Load inputs from config.json
with open('config.json') as config_json:
    config = json.load(config_json)

# Read files frim bids directory

data_file = config.pop('ds')
raw_ctf = mne.io.read_raw_ctf('bids/sub-0001/meg/sub-0001_task-AEF_run-02_meg.ds/sub-0001_task-AEF_run-02_meg.res4')
raw_ctf.save('test_raw.fif')


#!/usr/local/bin/python3

import mne
import json
from mne_bids import read_raw_bids


# Load inputs from config.json
with open('config.json') as config_json:
    config = json.load(config_json)

# Read files frim bids directory

data_file = config.pop('ds')
bids_path = BIDSPath(subject='0001',
                     session=None,
                     task='AEF',
                     run='02',
                     acquisition=None,
                     processing=None,
                     recording=None,
                     space=None,
                     suffix=None,
                     datatype='meg',
                     root=None)
# raw_ctf = mne.io.read_raw_ctf('bids/sub-0001/meg/sub-0001_task-AEF_run-02_meg.ds/sub-0001_task-AEF_run-02_meg.res4')
raw_ctf = read_raw_bids(bids_path)
raw_ctf.save('test_raw.fif')


#!/usr/local/bin/python3

import mne
import json
from mne_bids import BIDSPath, read_raw_bids


# Load inputs from config.json
with open('config.json') as config_json:
    config = json.load(config_json)

# Read files from bids directory
bids_path = BIDSPath(subject=config['subject'],
                     session=config['session'],
                     task=config['task'],
                     run=config['run'],
                     acquisition=config['acquisition'],
                     processing=config['processing'],
                     recording=config['recording'],
                     space=config['space'],
                     suffix=config['suffix'],
                     datatype=config['datatype'],
                     root=config['root'])

raw_ctf = read_raw_bids(bids_path)

# Save ctf file into fif
raw_ctf.save('out_dir/meg.fif', overwrite=True)


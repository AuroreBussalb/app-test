#!/usr/local/bin/python3

import mne
import json
from mne_bids import BIDSPath, read_raw_bids


# Load inputs from config.json
with open('config.json') as config_json:
    config = json.load(config_json)

# Convert all "" into None when the App runs on BL 
tmp = dict((k, None) for k, v in config.items() if v == "")
config.update(tmp)

# Read files from bids directory
# bids_path = BIDSPath(subject=config['subject'],
#                      session=config['session'],
#                      task=config['task'],
#                      run=config['run'],
#                      acquisition=config['acquisition'],
#                      processing=config['processing'],
#                      recording=config['recording'],
#                      space=config['space'],
#                      suffix=config['suffix'],
#                      datatype='meg',
#                      root='bids')

bids_path = BIDSPath(subject="0001",
                     session=None,
                     task="AEF",
                     run="02",
                     acquisition=None,
                     processing=None,
                     recording=None,
                     space=None,
                     suffix=None,
                     datatype='meg',
                     root='bids')

# raw_ctf = read_raw_bids(bids_path)

# # Save ctf file into fif
# raw_ctf.save('out_dir/meg.fif', overwrite=True)


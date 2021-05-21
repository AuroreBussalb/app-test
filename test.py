#!/usr/local/bin/python3

import mne
import json
from mne_bids import BIDSPath, read_raw_bids


# Load inputs from config.json
with open('config.json') as config_json:
    config = json.load(config_json)

# Read ctf
data_file = config.pop('fif')
raw = mne.io.read_raw_fif(data_file)

# Save ctf file
raw.save('out_dir/test.fif', overwrite=True)


# Read the raw file
# data_file = config.pop('fif')
# raw = mne.io.read_raw_fif(data_file, allow_maxshield=True)   

# print(raw.pick_types(eeg=True)) 
# print(raw.info['ch_names']) 


# print(raw.info['chs'])

# # Convert all "" into None when the App runs on BL 
# tmp = dict((k, None) for k, v in config.items() if v == "")
# config.update(tmp)

# # Create BIDS directory
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

# # Read file from BIDS directory
# raw_ctf = read_raw_bids(bids_path)

# # Save ctf file into fif
# raw_ctf.save('out_dir/meg.fif', overwrite=True)


#!/usr/local/bin/python3

import mne
import json

# Load inputs from config.json
with open('config.json') as config_json:
    config = json.load(config_json)

# Read the files
data_file = str(config.pop('fif'))
raw = mne.io.read_raw_fif(data_file, allow_maxshield=True)

# Save file
# raw.save(raw.filenames[0].replace('.fif', 'test-raw.fif'), overwrite=True)

# Generate a report
report = mne.Report(title='Rapport test', verbose=True)

# Save report
report.save('out_dir/report_maxfilter.html', overwrite=True)

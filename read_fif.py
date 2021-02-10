#!/usr/local/bin/python3

import mne
import json

# Print mne version
print(mne.__version__)

# Generate a json.product to display messages on Brainlife UI
dict_json_product = {'brainlife': []}

# Load inputs from config.json
with open('config.json') as config_json:
    config = json.load(config_json)

# Read the files
data_file = str(config.pop('fif'))
raw = mne.io.read_raw_fif(data_file, allow_maxshield=True)

# Test param
# test_param = config.pop('param_test')
# if test_param is not None:
#     test_param = str(test_param)
#     print('a')
# elif test_param == "":
#     dict_json_product['brainlife'].append({'type': 'warning', 'msg': "no param"})
#
# if test_param == "ok":
#     dict_json_product['brainlife'].append({'type': 'warning', 'msg': "ok"})
# elif test_param == "okay":
#     dict_json_product['brainlife'].append({'type': 'warning', 'msg': "okay"})
# else:
#     ValueError_message = f'Wrong parameter!'
#     # Raise exception
#     raise ValueError(ValueError_message)

# Save file
# raw.save(raw.filenames[0].replace('.fif', 'test-raw.fif'), overwrite=True)
# print(raw.filenames[0].replace('.fif', 'test-raw.fif'))
raw.save("out_dir/test-raw.fif", overwrite=True)

# Generate a report
report = mne.Report(title='Rapport test', verbose=True)

# Save report
report.save('out_dir/report_maxfilter.html', overwrite=True)

# Success message in product.json
dict_json_product['brainlife'].append({'type': 'success', 'msg': 'It runs!'})

# Save the dict_json_product in a json file
with open('product.json', 'w') as outfile:
    json.dump(dict_json_product, outfile)

#!/usr/local/bin/python3

import mne
import json
import warnings


# Generate a json.product to display messages on Brainlife UI
dict_json_product = {'brainlife': []}

# Load inputs from config.json
with open('config.json') as config_json:
    config = json.load(config_json)

# Read the files
data_file = str(config.pop('fif'))
raw = mne.io.read_raw_fif(data_file, allow_maxshield=True)

# Warning if bad channels are empty
if raw.info['bads'] is None:
    UserWarning_message = f'No channels are marked as bad. ' \
                      f'Make sure to check (automatically or visually) for bad channels before ' \
                      f'running MaxFilter.'
    warnings.warn(UserWarning_message)
    dict_json_product['brainlife'].append({'type': 'warning', 'msg': UserWarning_message})

# Check if MaxFilter was already applied on the data
sss_info = raw.info['proc_history'][0]['max_info']['sss_info']
tsss_info = raw.info['proc_history'][0]['max_info']['max_st']
if bool(sss_info) or bool(tsss_info) is True:
    ValueError_message = f'You cannot apply MaxFilter if data have already ' \
                     f'processed with Maxwell-filter.'
    # Raise exception
    raise ValueError(ValueError_message)

# Apply MaxFilter
raw_maxfilter = mne.preprocessing.maxwell_filter(raw,
                                                 st_duration=config['param_st_duration'],
                                                 st_correlation=config['param_st_correlation'])

# Save file
if config['param_st_duration'] is not None:
    raw_maxfilter.save("out_dir/test-raw_tsss.fif)", overwrite=True)
else:
    raw_maxfilter.save("out_dir/test-raw_sss.fif)", overwrite=True)

# Save file
# raw.save(raw.filenames[0].replace('.fif', 'test-raw.fif'), overwrite=True)
# print(raw.filenames[0].replace('.fif', 'test-raw.fif'))
# test = raw.filenames[0].replace('.fif', '_%s.fif' % config['param_output_tag'])
# # path = "/network/lustre/iss01/home/aurore.bussalb/Repositories/app-maxfilter/data/"
# path = "/out_dir/"
# path_fif = os.path.join(path, test)
# raw.save(path_fif, overwrite=True)
#
# # Generate a report
# report = mne.Report(title='Rapport test', verbose=True)
#
# # Save report
# report.save('out_dir/report_maxfilter.html', overwrite=True)

# Success message in product.json
dict_json_product['brainlife'].append({'type': 'success', 'msg': 'It runs!'})

# Save the dict_json_product in a json file
with open('product.json', 'w') as outfile:
    json.dump(dict_json_product, outfile)

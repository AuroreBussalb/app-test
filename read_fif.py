import mne
import json

# Generate a json.product to display messages on Brainlife UI
dict_json_product = {'brainlife': []}

# Load inputs from config.json
with open('config.json') as config_json:
    config = json.load(config_json)

data_file = str(config.pop('fif'))
raw = mne.io.read_raw_fif(data_file, allow_maxshield=True)

print(raw.info)

# Save file
raw.save("test-raw.fif", overwrite=True)

# Success message in product.json
dict_json_product['brainlife'].append({'type': 'success',
                                       'msg': 'Yeah'})

# Save the dict_json_product in a json file
with open('product.json', 'w') as outfile:
    json.dump(dict_json_product, outfile)

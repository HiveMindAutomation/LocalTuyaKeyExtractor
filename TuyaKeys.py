# Python Script to extract Local API Keys from Tuya Cloud API
# Streamlines Local Tuya Setup

import pandas as pd
from tuya_connector import TuyaOpenAPI

# Add your ACCESS_ID and ACCESS_KEY to auth_template.py and save it as auth.py
from auth import ACCESS_ID, ACCESS_KEY

## You MIGHT need to change this endpoint if your API Endpoint is on a Different Server, i.e. China

API_ENDPOINT = "https://openapi.tuyaeu.com"

# Instantiate the Tuya API Session
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

#Load input.CSV into a Dataframe
input_df = pd.read_csv('input.csv')
# Convert the "device_id" Column of the Dataframe into a list for our lookups later
devices = input_df.device_id.to_list()

# print(devices)

def get_local_keys(device_id):
    params = {'device_ids': device_id}
    data = openapi.get(f"/v1.1/iot-03/devices/{device_id}")
    if data['success'] == False:
        print(f'Something went wrong with {device_id}')
        return None
    mac_data = openapi.get(f"/v1.0/iot-03/devices/factory-infos", params=params)
    try:
        # Get RAW mac Address Data from Tuya API
        try:
            mac_address = mac_data['result'][0]['mac']
        except IndexError:
            mac_address = 'NOT FOUND'
        # Format MAC Address with ':' between octets.
        mac_address_formatted = ':'.join(mac_address[i:i + 2] for i in range(0, len(mac_address), 2))
    except KeyError:
        # In testing, not all accessories returned the Mac Address on the JSON Response. This handles the error thrown.
        mac_address_formatted = "Unknown"


    output_data = {
        'device_id': device_id,
        'device_name': data['result']['name'],
        'local_key': data['result']['local_key'],
        'mac_address': mac_address_formatted,
        'product_name': data['result']['product_name'],
        'product_category': data['result']['category_name']
    }

    return output_data


device_list = []

for device in devices:
    device_list.append(get_local_keys(device))

df = pd.DataFrame(device_list)
df.to_csv('./local_tuya.csv', index=False)
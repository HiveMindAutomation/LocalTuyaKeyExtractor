# [Hive Mind Automation](https://hivemindautomation.com.au)
# Local Tuya Key Extractor

## Tool for pulling Local Keys from Tuya IoT Cloud for use with Local Tuya
As Seen in the [Hive Mind Automation YouTube Video](https://)

## Pre-Requisites

- You need to have a Tuya IoT Cloud Developer account
  - have created a Cloud Project.
  - The Cloud project needs to also be linked to your Tuya Smart/Smart Life App so the devices are visible.
  - You will need the API Keys for that project in order for this tool to work

## Known Limitations
You need to manually add your devices to the input.csv file.
Attempts to automatically extract the device list have failed so far.

## Getting Started

### TIP: Easier with [PyCharm - Community Edition](https://www.jetbrains.com/pycharm/)

Clone this project: `git clone https://github.com/HiveMindAutomation/LocalTuyaKeyExtractor.git`  
Change to the project directory: `cd TuyaKeyExtractor`

### Optional - Create a Python Virtual Environment (recommended)
- Create the Virtual Environment
`python3 -m venv venv`  
- Activate the Virtual Environment:
`source ./venv/bin/activate`

### Install Dependencies
`pip3 install -r requirements.txt`  

Optional - deactivate the venv: `deactivate`

### Setup your Authentication details
open `auth_template.py` in the editor of your choice 
- Change "ACCESS_ID" to the Access ID/Client ID copied from your Tuya IoT Cloud project
- Change "ACCESS_KEY" to the Access Secret/Client Secret copied from your Tuya IoT Cloud project

### Add your Devices to input.csv
open `input.csv` in Excel/Numbers/Editor of your choice.
- Copy the Device ID's of the Devices you want to lookup into the CSV
  - You can either get this from the "Devices" page in your Tuya IoT Cloud project OR
  - open the device in the Tuya Smart app, click the "edit" option, and go to "Device Information"
    - Copy the "Virtual ID" from the Tuya Smart App. on macOS/iOS, Handoff will mean you can copy from your phone and paste into the CSV File.
- Repeat for ALL Device ID's you want to lookup, this doesn't have to be all of your Tuya Devices, but I don't see much point in doing it by halves.
- Save the CSV, do not change the name, it MUST be input.csv

### run the script

Activate the virtual environment (if you're using a venv):
`source ./venv/bin/activate`

Run TuyaKeys.py: `python3 ./TuyaKeys.py`

Optional - deactivate the Venv: `deactivate`

## Output

Following a successful run of the script, you should have a file added to the folder called `local_tuya.csv`
containing the following details for each device in your input.csv file:

| Parameter        |                                          Description                                          |
|------------------|:---------------------------------------------------------------------------------------------:|
| device_id        |        This is the Device ID we input to the CSV file. You need this to add LocalTuya         |
| device_name      |    The "Friendly Name" of the Device in your Tuya IoT Cloud setup and your Tuya Smart App     |
| local_key        | This is what we came here for. The Local API Key for the device. Required to setup Local Tuya |
| mac_address      |      MAC Address of the device. Helpful when you're trying to find the Local IP Address       |
| product_name     |                                       Tuya Product Name                                       |
| product_category |                                     Tuya Product Category                                     |

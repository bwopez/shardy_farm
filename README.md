# Shardy farm

Shardy farm is a python script that automates the process of the legendary shard farm that was found during Season of the Haunted 2022.

## Installation

You will need python3+ to run this script. Follow instructions [here](https://phoenixap.com/kb/how-to-install-python-3-windows) for a Windows install. Download the ZIP file for this repository and unZIP it in a folder of your choosing. Open a command line in the folder that holds the repository. A [virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) is recommended but not required.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all requirements.

```bash
pip install -r requirements.txt
```

## Setup

There are two calibration scripts that are needed to be run before you can use the farming scripts; calibration_materials.py and calibration_shards.py. Running calibration_materials.py is needed to gather materials from Master Rahool in the tower and you need to be in his shop to calibrate. Once Master Rahool's shop, run
```bash
python calibration_materials.py
```
and follow instructions in the command line until completion. 

Running calibration_shards.py is needed to gather legendary shards from your inventory. Once your character menu, or inventory, is opened, run
```bash
python calibration_shards.py
```
and follow instructions in the command line until completion.

## Usage

If you are short on planetary materials or just want to add some more to your inventory, you can run
```bash
python materials_collector.py
```
while in Master Rahool's shop and follow instructions in command line.

If you would like to farm for legendary shards you can run
```bash
python legendary_shards.py
```
with your inventory open and follow instructions in command line. There is also a flag to exclude certain armor pieces in your farming as well with the -x option. 
The keywords that you can use for exclusions would be: helm, arms, chest, legs, class.

-x option example:
```bash
python legendary_shards.py -x class arms 
```

The script takes control of your mouse and keyboard, to take back control you would need to activate the kill switch by either forcing the mouse into the top left corner of your screen or by holding the right control key until the kill switch is activated.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
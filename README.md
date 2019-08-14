ezProtocol is a simple protocol writer for [Opentrons](https://opentrons.com/) OT-2 robot.

Using this tool, you can easily generate compatible scripts to be run on OT-2. 

ezProtocol can read protocol file in a format designed to be easy but versatile. 

See [here](https://github.com/SichongP/ezProtocol/blob/master/How_to_write_a_protocol.md) on how to make a protocol file.

## Requirements 
ezProtocol relies on below packages:
- PyYAML
- Pandas
- python-frontmatter
- regex
- opentrons

## Installation (pip deploy pending)
Clone this repo:
```
git clone https://github.com/SichongP/ezProtocol
```

Change directory:
```
cd ezProtocol
```
Install package:
```
pip install .
```
**Or**, use install.sh script:
```
bash install.sh
```
Test installation:
```
ezprotocol -h
```

## Getting started 
Once you have protocol and deck layout file ready (see [here](https://github.com/SichongP/ezProtocol/blob/master/How_to_write_a_protocol.md) for more detail on protocol and layout format), on commandline, type:
```
ezprotocol -p protocol.txt -d deck_layout.csv -o ot2_script.py
```


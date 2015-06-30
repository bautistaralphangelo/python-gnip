# Python Gnip
A python wrapper for the Gnip API.

## Installation

#### via Pip
```
pip install pygnip
```

#### From Source
```
wget https://github.com/benjiao/python-gnip/archive/pygnip-v1.0.1.a1.tar.gz
tzr -xvzf pygnip-v1.0.1.a1.tar.gz
cd pygnip-v1.0.1.a1
python setup.py build
python setup.py install
```

## Usage

#### PowerTrack API

Initialization
```
from pygnip import GnipPowerTrack

gnip = GnipPowerTrack(account_name="account-name",
                      username="yourusername",
                      passwd="yourpassword")
```

----
Add Rule
```
gnip.addRule(tag="yourcustomtag",
             value="Filter OR Filters")
```

----
Remove Rule
```
gnip.removeRule(rule="Filter OR Filters")
```

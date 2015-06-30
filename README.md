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


----
To Run Tests (`python setup.py test`)

1. Create a file called `.gnipvars` with the following lines:
```
export GNIP_ACCOUNT_NAME=<your-gnip-account-name>
export GNIP_USERNAME=<your-gnip-username>
export GNIP_PASSWD=<your-gnip-password>
```

2. Type in `source .gnipvars` to activate environment variables

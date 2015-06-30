# Python Gnip
A python wrapper for the Gnip API.

## Installation

#### via Pip
```
pip install pygnip
```

#### Manually
```
git clone git@github.com:benjiao/python-gnip.git
cd python-gnip
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

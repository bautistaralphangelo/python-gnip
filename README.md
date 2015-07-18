# Python Gnip
A python wrapper for the Gnip API.

## API Documentation

http://pythonhosted.org/pygnip/

## Installation

### via Pip
```
pip install pygnip
```

#### From Source
```
git clone https://github.com/benjiao/python-gnip.git
cd python-gnip
python setup.py install
```

## Usage

### PowerTrack API

* Initialization
```
from pygnip import GnipPowerTrack

gnip = GnipPowerTrack(account_name="account-name",
                      username="yourusername",
                      passwd="yourpassword")
```

* Add Rule
```
gnip.addRule(tag="yourcustomtag",
             value="Filter OR Filters")

# Samples with quotation marks
gnip.addRule(tag="tag2", value='("TESTFILTER1" OR "TESTFILTER")')
gnip.addRule(tag="tag3", value="(\"TESTFILTER2\" OR \"TESTFILTER3\")")
```

* Remove Rule
```
gnip.removeRule(rule="Filter OR Filters")
```

* List Rules
```
rules = gnip.getRules()
```


## Contribute
### Run Tests

1. Create a file called `.gnipvars` with the following lines:
```
export GNIP_ACCOUNT_NAME=<your-gnip-account-name>
export GNIP_USERNAME=<your-gnip-username>
export GNIP_PASSWD=<your-gnip-password>
```
2. Type in `source .gnipvars` to activate environment variables
3. Run tests 
```
python setup.py test
```
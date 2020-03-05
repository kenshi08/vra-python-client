# vra-python-client
vRealize Automation SDK Python Client
- only supporting vRA IaaS Api 

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage

```sh
pip3 install git+https://github.com/kenshi08/vra-python-client.git
(you may need to run `pip3` with root permission: `sudo pip3 install git+https://github.com/kenshi08/vra-python-client.git`)
```

## Setup requirements

```sh
pip3 install -r requirements.txt
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python3 setup.py install --user
```
(or `sudo python3 setup.py install` to install the package for all users)

Then import the package:
```python
import vra_iaas_client
```

## Getting Started

To test if Client is working, please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import vra_iaas_client
from vra_iaas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vra_iaas_client.AboutApi(vra_iaas_client.ApiClient(configuration))

try:
    # Get about page
    api_response = api_instance.get_about_page()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AboutApi->get_about_page: %s\n" % e)

```
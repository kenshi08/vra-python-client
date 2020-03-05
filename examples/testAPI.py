from __future__ import print_function
import time
import vra_iaas_client
from vra_iaas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vra_iaas_client.AboutApi(vra_iaas_client.ApiClient())

try:
    # Get about page
    api_response = api_instance.get_about_page()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AboutApi->get_about_page: %s\n" % e)
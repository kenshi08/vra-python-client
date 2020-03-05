from __future__ import print_function
import time
import vrac_iaas_client
from vrac_iaas_client.rest import ApiException
from pprint import pprint
import json

#reading data from output.json
with open('examples/output.json') as json_file:
    data = json.load(json_file)
    for p in data['cloudaccount']:
        print('CloudAccountID: ' + p['cloudaccountID'])
    for p in data['projects']:
        print('ProjectID: ' + p['projectID'])
    for p in data['regions']:
        print('RegionID: '+ p['regionID'])
    for p in data['zones']:
        print('ZoneID: '+ p['cloudzoneID'])
    for p in data['netprofiles']:
        print('NetworkProfileID: '+ p['networkprofileID'])

#read refresh token from file
with open('examples/input.json') as json_file:
    token = json.load(json_file)

#Declare variables from input.json
refresh_token = token['refresh_token']

#Get OAuth token
loginAPI = vrac_iaas_client.LoginApi(vrac_iaas_client.ApiClient())
loginspec = vrac_iaas_client.CspLoginSpecification(refresh_token=refresh_token)
response = loginAPI.retrieve_auth_token(loginspec)
print("Token Retrieved: " + response.token)
token = "Bearer " + response.token

#delete network profile
networkProfileAPI = vrac_iaas_client.NetworkProfileApi(vrac_iaas_client.ApiClient(header_name="Authorization", header_value=token))
for p in data['netprofiles']:
    try:
        print('Deleting network profile: '+ p['networkprofileID'])
        response = networkProfileAPI.delete_network_profile(p['networkprofileID'])
    except ApiException as e:
                    print("Exception when calling NetworkProfileApi->delete_network_profile: %s\n" % e)

#remove cloud zones from project
projectAPI = vrac_iaas_client.ProjectApi(vrac_iaas_client.ApiClient(header_name="Authorization", header_value=token))
for p in data['projects']:
    try:
        print('Removing clonezones from project: ' + p['projectID'])
        body = {"zoneAssignmentConfigurations": []}
        projectAPI.update_project(p['projectID'], body)
    except ApiException as e:
        print("Exception when calling ProjectApi->update_project: %s\n" % e)

#delete project
for p in data['projects']:
    try:
        print('Deleting project: ' + p['projectID'])
        projectAPI.delete_project(p['projectID'])
    except ApiException as e:
        print("Exception when calling ProjectApi->delete_project: %s\n" % e)

#delete cloud zones
cloudzoneAPI = vrac_iaas_client.LocationApi(vrac_iaas_client.ApiClient(header_name="Authorization", header_value=token))
for p in data['zones']:
    try:
        print('Deleting cloud zone: ' + p['cloudzoneID'])
        cloudzoneAPI.delete_zone(p['cloudzoneID'])
    except ApiException as e:
        print("Exception when calling LocationApi->delete_zone: %s\n" % e)

#delete cloud account
cloudaccountAPI = vrac_iaas_client.CloudAccountApi(vrac_iaas_client.ApiClient(header_name="Authorization", header_value=token))
for p in data['cloudaccount']:
    try:
        print('Deleting cloud account: ' + p['cloudaccountID'])
        cloudaccountAPI.delete_cloud_account(p['cloudaccountID'])
    except ApiException as e:
        print("Exception when calling CloudAccountApi->delete_cloud_account: %s\n" % e)

print('Completed')
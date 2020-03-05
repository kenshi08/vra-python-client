from __future__ import print_function
import time
import json
import vrac_iaas_client
from vrac_iaas_client.rest import ApiException
from pprint import pprint

#to be used for output.json later
dataCloudAccount = {}
dataCloudAccount['cloudaccount'] = []
dataProject = {}
dataProject['projects'] = []
dataRegion = {}
dataRegion['regions'] = []
dataCloudZone = {}
dataCloudZone['zones'] = []
dataNetworkProfile = {}
dataNetworkProfile['netprofiles'] = []

#Test SDK client is working - create an instance of the API class
api_instance = vrac_iaas_client.AboutApi(vrac_iaas_client.ApiClient())
try:
    # Get about page
    api_response = api_instance.get_about_page()
    print(api_response)
    print("SDK working with API")
except ApiException as e:
    print("Exception when calling AboutApi->get_about_page: %s\n" % e)

#read data from file
with open('examples/input.json') as json_file:
    data = json.load(json_file)

#Declare variables from input.json
refresh_token = data['refresh_token']
aws_access_key = data['aws_access_key']
aws_secret = data['aws_secret']
cloudaccountname = data['cloud_account_name']
projectname = data['project_name']
members = [data['members']]
administrators = [data['administrators']]
fabricName = data['subnet_name']    

#Get OAuth token
loginAPI = vrac_iaas_client.LoginApi(vrac_iaas_client.ApiClient())
loginspec = vrac_iaas_client.CspLoginSpecification(refresh_token=refresh_token)
response = loginAPI.retrieve_auth_token(loginspec)
#print("Token Retrieved: " + response.token)
token = "Bearer " + response.token

#create aws cloud account
default_zones = 'false'
desc = 'Created from python sdk'
regionID = ["us-west-1", "us-east-1"]
tags = [{ "key": "platform", "value": "aws" }]
aws_spec = vrac_iaas_client.CloudAccountAwsSpecification(aws_access_key, aws_secret, default_zones, cloudaccountname, desc, regionID, tags) 
cloudaccountAPI = vrac_iaas_client.CloudAccountApi(vrac_iaas_client.ApiClient(header_name="Authorization", header_value=token))
cloudaccountID = ''
try:
    response = cloudaccountAPI.create_aws_cloud_account(aws_spec)
    #print(response)
    print('Cloud account created: ' + response.id)
    cloudaccountID = response.id
    dataCloudAccount['cloudaccount'].append({'cloudaccountID': response.id})
    time.sleep(30)
except ApiException as e:
    print("Exception when calling CloudAccountAPI->create_aws_cloud_account: %s\n" % e)

#create aws cloud zones
cloudzoneAPI = vrac_iaas_client.LocationApi(vrac_iaas_client.ApiClient(header_name="Authorization", header_value=token))
regions = cloudzoneAPI.get_regions()
regionArray = []
cloudzoneList = [] 
for i in regions.content:
        #print(i.id)
        if i.cloud_account_id == cloudaccountID:
            #print("RegionID: " + i.id)
            regionArray.append(i.id)    
            dataRegion['regions'].append({'regionID': i.id})        

print('List of region IDs: ' + str(regionArray))
for i in regionArray:
    try:
        region = cloudzoneAPI.get_region(i)
        name = cloudaccountname + '_' + region.external_region_id
        description = 'Cloud zone created from SDK'
        regionID = region.id
        tags = [{ "key": "platform", "value": "aws" }, {"key": "env", "value": "lab"}]
        placement = 'DEFAULT'
        cloudzonespec = vrac_iaas_client.ZoneSpecification(region_id=regionID, name=name, description=description, placement_policy=placement, tags=tags)
        cloudzone = cloudzoneAPI.create_zone(cloudzonespec)
        cloudzoneList.append(cloudzone.id)
        print('Cloud zone created: ' + cloudzone.id)
        dataCloudZone['zones'].append({'cloudzoneID': cloudzone.id})
    except ApiException as e:
        print("Exception when calling LocationAPI->create_zone: %s\n" % e)

#create project
description = 'SDK Project created by Python SDK Client'
# members = [{ "email": "kenshi08@gmail.com" }]
# administrators = [{ "email": "clementwong@vmware.com" }]
zoneAssignments = []
for i in cloudzoneList:
    try:
        zoneassignment = vrac_iaas_client.ZoneAssignmentConfig(memory_limit_mb=0, zone_id=i, max_number_instances=0, priority=0)
        zoneAssignments.append(zoneassignment)
    except ApiException as e:
        print("Exception in cloudzoneList: %s\n" % e)
projectAPI = vrac_iaas_client.ProjectApi(vrac_iaas_client.ApiClient(header_name="Authorization", header_value=token))
projectspec = vrac_iaas_client.ProjectSpecification(members=members, zone_assignment_configurations=zoneAssignments, name=projectname, description=description, administrators=administrators)
try:
    project = projectAPI.create_project(projectspec)
    print('Project ID: ' + project.id)
    dataProject['projects'].append({'projectID': project.id})
except ApiException as e:
        print("Exception when calling ProjectAPI->create_project: %s\n" % e)

#create network profiles
fabricnetworkAPI = vrac_iaas_client.FabricNetworkApi(vrac_iaas_client.ApiClient(header_name="Authorization", header_value=token))
fabricnetworkList = fabricnetworkAPI.get_fabric_networks()
networkprofileAPI = vrac_iaas_client.NetworkProfileApi(vrac_iaas_client.ApiClient(header_name="Authorization", header_value=token))
#get fabric network ids
fabricnetworkList2 = []
for i in regionArray:
    region = cloudzoneAPI.get_region(i)
    for a in fabricnetworkList.content:
        for b in a.cloud_account_ids:
            if b == cloudaccountID and a.name == fabricName and a.external_region_id == region.external_region_id:
                #print("Found fabric network: " + a.name)        
                try:
                    name = 'sdk_netprofile_' + region.external_region_id
                    description = 'Network Profile created from SDK'
                    regionID = region.id
                    tags = [{ "key": "platform", "value": "aws" }, {"key": "env", "value": "lab"}]
                    fabric_network_ids = [a.id]
                    networkprofilespec = vrac_iaas_client.NetworkProfileSpecification(description=description, tags=tags, fabric_network_ids=fabric_network_ids, region_id=regionID, security_group_ids=None, name=name, isolation_type=None)        
                    networkprofile = networkprofileAPI.create_network_profile(networkprofilespec)
                    print("NetworkProfile ID: " +networkprofile.id)
                    dataNetworkProfile['netprofiles'].append({'networkprofileID': networkprofile.id})
                except ApiException as e:
                    print("Exception when calling LocationAPI->create_zone: %s\n" % e)

#combining and formating data to dump into json output
data = {}
data.update(dataCloudAccount)
data.update(dataProject)
data.update(dataRegion)
data.update(dataCloudZone)
data.update(dataNetworkProfile)

with open('examples/output.json', 'w') as outfile:
    json.dump(data, outfile, sort_keys=True, indent=4)
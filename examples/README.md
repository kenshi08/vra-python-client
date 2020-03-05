# vra-python-client
vRealize Automation SDK Python Client

## Examples

You can find some examples of how to use the SDK

## testAPI.py

This example is just for you to test if the SDK is working with the API by sending a GET post to retrieve information of the API. You just need to execute:
```sh
sudo python3 testAPI.py
```

## OnBoarding (onboard.py)

This example allows you to create
1) AWS Cloud Account
2) 2 Cloud Zones
3) Project with members and cloud zones attach
4) 2 network profiles for each region

Please use the input.json.sample, rename it as input.json and populate it with the respective information needed like vRA API Token (refresh token), AWS access key and secret.

Once the process has been completed, json outputs will be dumped into an output.json file to be used in the next example for removing what we created above.
```sh
sudo python3 onboard.py
```

### Remove (remove.py)

This example shows how we can remove objects created with the SDK client using the output.json create from OnBoardin (Part 1) example

This will remove:
1) Delete Network Profiles
2) Detach 2 cloudzones from project
3) Delete Project
4) Delete 2 cloud zones
5) Delete cloud account

```sh
sudo python3 remove.py
```
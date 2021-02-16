import json
import requests
import sys

if (len(sys.argv) != 2):
    print("")
    print("this script need to be given the name of the json file as an argument")
    print("")
    exit()

headers = {"Content-Type": "application/json", "Accept": "application/json"}
try:
    with open("config.json", "r") as config:
        credentials = json.load(config)
        user = credentials['USERNAME']
        pwd = credentials['PASSWORD']
        api_url = credentials['APIURL']
except:
    print("unable to load config file")
    exit()
try:
    with open(sys.argv[1], "r") as snow:
        snow_data = json.load(snow)
except:
    print("unable to import upload_racks.json")
    exit()
try:
    for rack in snow_data:
        response = requests.post(api_url, auth=(user, pwd), headers=headers, json=rack)
        print("{} {}".format(rack["u_rack_name"], response.status_code))
except:
    print("unable to load snow.json")
    exit()

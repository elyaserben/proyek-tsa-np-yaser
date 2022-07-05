import json
import requests
api_url = "http://localhost:58001/api/v1/network-device"

headers={"X-Auth-Token": "NC-12-25ade76081434e229d24-nbi"}

resp = requests.get(api_url, headers=headers, verify=False)

print("Request status: ", resp.status_code)

response_json = resp.json()
networkDevices = response_json["response"]

for networkDevice in networkDevices:
    print(networkDevice["hostname"], "\t", networkDevice["platformId"], "\t", networkDevice["managementIpAddress"])


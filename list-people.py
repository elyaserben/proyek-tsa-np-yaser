# Fill in this file with the people listing code from the Webex Teams exercise
import requests
import json
access_token = 'ZThlZTg0ZTYtMTg2Yy00YjhkLTkyZTQtY2ViNjFjZTI5MmY5NWMxMmExNmQtYTcz_P0A1_4a252141-f787-4173-a4c9-bde69c553a24'
url = 'https://webexapis.com/v1/people/me'
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))

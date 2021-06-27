
from pprint import pprint

import json
import urllib3
import requests




urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

host = 'https://webexapis.com/'
teams_path = "https://webexapis.com/v1/teams"
rooms_path = "https://webexapis.com/v1/rooms"
msg_path = "https://webexapis.com/v1/messages"
token = "Bearer Y2IxMWQ0ZmEtM2UzMy00YzhiLTlkYzMtODI2ZWM1ZDRjYjY0MmYyZWE4NWMtZDQ1_P0A1_f98b67b3-1ec1-437e-acce-3fd02f2f5d04"



teams_body = {"name": "NotificationMessageApp"}

headers = {
    "Authorization": token,
    "Content-Type": "application/json"
}

#import requests


#r = requests.post('https://webexapis.com/v1/teams', data=json.dumps(teams_body),
                  #headers={'Authorization': token,
                  #'Content-Type': 'application/json'})

#print (r.text)

teams_post = requests.post(teams_path, headers=headers, data=json.dumps(teams_body), verify=False).json()
teams_get = requests.get(teams_path, headers=headers, verify=False).json()
pprint(json.dumps(teams_get, indent=2, sort_keys=True))
teams = teams_get['items']
for team in teams:
    if team['name'] == 'test':
        teamId = team['id']
        print(teamId)

rooms_body = {
    "title": "Our Main Room",
    "teamId": 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1RFQU0vNDcyZmVmZDAtZDcwZS0xMWViLTg5MTEtNGY3MGI2MjZiY2Ni'
}
rooms_post = requests.post(rooms_path, headers=headers, data=json.dumps(rooms_body), verify=False).json()
rooms_get = requests.get(rooms_path, headers=headers, verify=False).json()
pprint(json.dumps(rooms_get, indent=2, sort_keys=True))
rooms = rooms_get['items']
for room in rooms:
    if room['title'] == 'Our Main Room':
        roomId = room['id']
        print(roomId,"room id")


msg_body = {
    "roomId": roomId,
    "text": "Python tutorials"
}
msg_post = requests.post(msg_path, headers=headers, data=json.dumps(msg_body), verify=False).json()
msg_get = requests.get(msg_path, headers=headers, verify=False).json()
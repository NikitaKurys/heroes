from pprint import pprint

import requests

hulk_id = '/332'
Captain_id = '/149'
Thanos_id = '/655'
API_BASE_URL = 'https://superheroapi.com/api/2619421814940190'

response_hulk = requests.get(API_BASE_URL + hulk_id + '/powerstats')
response_captain = requests.get(API_BASE_URL + Captain_id + '/powerstats')
response_thanos = requests.get(API_BASE_URL + Thanos_id + '/powerstats')

list_hero = [response_thanos.json(), response_hulk.json(), response_captain.json()]
max_intelligence = 0
most_intelligent = 0

for hero in list_hero:
    if int(hero['intelligence']) > int(max_intelligence):
        max_intelligence = hero['intelligence']
        most_intelligent = hero['name']

pprint(f'Самый умный супергерой {most_intelligent}, его интеллект равен:{max_intelligence}!!!')




from pprint import pprint

import requests

user_input1 = 'Hulk'
user_input2 = 'Captain America'
user_input3 = 'Thanos'

hero_id1 = 0
hero_id2 = 0
hero_id3 = 0

API_BASE_URL = 'https://superheroapi.com/api/2619421814940190/'

response_hero1 = requests.get(API_BASE_URL + 'search/' + user_input1)
response_hero2 = requests.get(API_BASE_URL + 'search/' + user_input2)
response_hero3 = requests.get(API_BASE_URL + 'search/' + user_input3)

for i in response_hero1.json()['results']:
    if i['name'] == user_input1:
         hero_id1 = i['id']

for i in response_hero2.json()['results']:
    if i['name'] == user_input2:
        hero_id2 = i['id']


for i in response_hero3.json()['results']:
    if i['name'] == user_input3:
        hero_id3 = i['id']


response_hero1 = requests.get(API_BASE_URL + hero_id1 + "/powerstats")
response_hero2 = requests.get(API_BASE_URL + hero_id2 + "/powerstats")
response_hero3 = requests.get(API_BASE_URL + hero_id3 + "/powerstats")

list_hero = [response_hero1.json(), response_hero2.json(), response_hero3.json()]
max_intelligence = 0
most_intelligent = 0

for hero in list_hero:
    if int(hero['intelligence']) > int(max_intelligence):
        max_intelligence = hero['intelligence']
        most_intelligent = hero['name']

pprint(f'Самый умный супергерой {most_intelligent}, его интеллект равен:{max_intelligence}!!!')




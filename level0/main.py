import json

file1 = open('C:\HackathoN\KLAHackathon\level0\level0.json')

data = json.load(file1)

for i in data['neighbourhoods']:
    print(i)

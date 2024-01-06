import json

file1 = open('C:\HackathoN\KLAHackathon\level0\level0.json')

data = json.load(file1)

list1 = []
for item in data['neighbourhoods']:
    list1.append(data['neighbourhoods'][item]['distances'])

list1.append(data['restaurants']['r0']['neighbourhood_distance'])
print(list1)
    

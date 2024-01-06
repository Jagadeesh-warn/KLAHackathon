import json

file1 = open('C:\HackathoN\KLAHackathon\level0\level0.json')

data = json.load(file1)

list1 = []
for item in data['neighbourhoods']:
    list1.append(data['neighbourhoods'][item]['distances'])

list1.append(data['restaurants']['r0']['neighbourhood_distance'])
list1[0].insert(0,0)
for i in range(1,21):
    list1[i].insert(0,list1[0][i])
print(list1)
    

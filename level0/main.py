import json
from collections import deque


file1 = open('C:\HackathoN\KLAHackathon\level0\level0.json')

data = json.load(file1)

list1 = []
length = data["n_neighbourhoods"]+len(data["restaurants"])

list1.append([0]+data["restaurants"][data["vehicles"]["v0"]["start_point"]]["neighbourhood_distance"])
for i in data["neighbourhoods"]:
    list1.append([0]+data["neighbourhoods"][i]["distances"])
#print(list1)

def travellingsalesman(c,cost,list2):
    v=0
    min=99999
    visited[c]=1
    list2.append("n%d"%(c-1))
    for k in range(length):
        if (list1[c][k] != 0) and (visited[k] == 0):
            if list1[c][k] < min:
                min=list1[c][k]
                v=k
    if min!=99999:
        cost+=min
    if v==0:
        list2.append("r0")
        cost+=list1[c][0]
        return
    travellingsalesman(v,cost,list2)

visited=[0]*(length+1)
cost=0
list2=[]
travellingsalesman(0,cost,list2)
    
list2[0]="r0"
output={"v0":{"path":list2}}

with open('level1.json', 'w') as file2:
    json.dump(output, file2)

with open('level1.json', 'r') as file:
    output_data = json.load(file)

for key, value in output_data.items():
    path = value["path"]
    print(f"Path for city {key}: {path}")

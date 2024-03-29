import json
import itertools


file1 = open('C:\HackathoN\KLAHackathon\level1\level1a.json')
data = json.load(file1)


neighbourhood = data['neighbourhoods']
ord_quantity = []
distance = []

for i in neighbourhood.keys():
    temp = list(neighbourhood[i].values())
    ord_quantity.append(temp[0])
    distance.append(temp[1])

res_dist = data['restaurants']['r0']['neighbourhood_distance']

max_cap = data['vehicles']['v0']['capacity']

def find_optimized_slots(distances, res_dist, ord_quantities, max_cap):
    node_order = sorted(range(len(res_dist)), key=lambda x: res_dist[x])
    slots = []
    current_slot = []
    current_capacity = 0
    current_distance = 0

    for node in node_order:
        if current_capacity + ord_quantities[node] <= max_cap:
            current_slot.append(node)
            current_capacity += ord_quantities[node]

            if len(current_slot) > 1:
                current_distance += distances[current_slot[-2]][current_slot[-1]]
        else:
            slots.append((current_slot, current_distance))
            current_slot = [node]
            current_capacity = ord_quantities[node]
            current_distance = 0

    if current_slot:
        slots.append((current_slot, current_distance))

    optimized_slots = []

    for slot, _ in slots:
        possible_orders = itertools.permutations(slot)
        min_distance = float('inf')
        best_order = []

        for order in possible_orders:
            dist = sum(distances[order[i]][order[i + 1]] for i in range(len(order) - 1))
            if dist < min_distance:
                min_distance = dist
                best_order = order

        optimized_slots.append((best_order, min_distance))

    return optimized_slots


optimized_slots = find_optimized_slots(distance, res_dist, ord_quantity, max_cap)
final_lst = []

for i in optimized_slots:
    temp = ['r0']
    temp.extend(['n' + str(j) for j in i[0]])
    temp.append('r0')
    final_lst.append(temp)

final_slots = {"v0": {f"path{i + 1}": final_lst[i] for i in range(len(final_lst))}}
print(final_slots)

with open('level1_output.json', 'w') as file2:
    json.dump(final_slots, file2)


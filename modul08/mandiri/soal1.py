import random
import math

cities = [(0,0), (2,5), (5,2), (8,8), (1,7), (6,1), (3,9), (7,3)]

def euclidean(c1, c2):
    return math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)

def total_distance(route, cities):
    return sum(euclidean(cities[route[i]], cities[route[(i+1) % len(route)]]) for i in range(len(route)))

initial_route = list(range(len(cities)))
random.shuffle(initial_route)

current_route = initial_route[:]
current_dist = total_distance(current_route, cities)

while True:
    neighbors = []
    for i in range(len(current_route)):
        for j in range(i+1, len(current_route)):
            n = current_route[:]
            n[i], n[j] = n[j], n[i]
            neighbors.append(n)
            
    best_neighbor = min(neighbors, key=lambda r: total_distance(r, cities))
    best_dist = total_distance(best_neighbor, cities)
    
    if best_dist >= current_dist:
        print("\nSolusi optimal lokal telah ditemukan")
        break
        
    current_route, current_dist = best_neighbor, best_dist

print(f"Rute awal      : {initial_route}")
print(f"Jarak awal     : {total_distance(initial_route, cities):.4f}")
print(f"Rute terbaik   : {current_route}")
print(f"Jarak terbaik  : {current_dist:.4f}")
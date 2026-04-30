import random

cities = ["A", "B", "C", "D", "E"]

distances = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 15],
    [15, 35, 0, 30, 20],
    [20, 25, 30, 0, 10],
    [25, 15, 20, 10, 0]
]

def total_distance(tour):
    return sum(
        distances[tour[i]][tour[(i + 1) % len(tour)]]
        for i in range(len(tour))
    )

def get_neighbors(tour):
    neighbors = []
    for i in range(len(tour)):
        for j in range(i + 1, len(tour)):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            neighbors.append(new_tour)
    return neighbors


current = list(range(len(cities)))
random.shuffle(current)

print("Solusi awal:", [cities[i] for i in current],
      "=", total_distance(current))

while True:
    neighbors = get_neighbors(current)
    best = min(neighbors, key=total_distance)

    print("→", [cities[i] for i in best], "=", total_distance(best))

    if total_distance(best) >= total_distance(current):
        break

    current = best

print("\nSolusi terbaik:", [cities[i] for i in current])
print("Total jarak:", total_distance(current))
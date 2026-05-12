import random

tasks = ['A', 'B', 'C', 'D', 'E']
durations = {'A': 4, 'B': 7, 'C': 3, 'D': 5, 'E': 6}

def calculate_cost(schedule):
    total, current_time = 0, 0
    for t in schedule:
        current_time += durations[t]
        total += current_time
    return total

initial_schedule = tasks[:]
random.shuffle(initial_schedule)

current_schedule = initial_schedule[:]
current_cost = calculate_cost(current_schedule)
iteration = 1

print(f"Solusi awal: {initial_schedule} | Cost: {current_cost}")
print("-" * 45)

while True:
    neighbors = []
    for i in range(len(current_schedule)):
        for j in range(i+1, len(current_schedule)):
            n = current_schedule[:]
            n[i], n[j] = n[j], n[i]
            neighbors.append(n)
            
    best_neighbor = min(neighbors, key=calculate_cost)
    best_cost = calculate_cost(best_neighbor)
    
    if best_cost < current_cost:
        current_schedule, current_cost = best_neighbor, best_cost
        print(f"Iterasi {iteration}: {current_schedule} | Cost: {current_cost}")
        iteration += 1
    else:
        print(f"\nIterasi {iteration}: Tidak ada cost lebih kecil. Proses berhenti.")
        break

print(f"Solusi terbaik : {current_schedule}")
print(f"Total cost     : {current_cost}")

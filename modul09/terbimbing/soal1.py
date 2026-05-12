import random
import math
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_distance(tour, cities):
    dist = 0
    for i in range(len(tour)):
        dist += distance(cities[tour[i]], cities[tour[(i + 1) % len(tour)]])
    return dist

def total_distance_two_salesmen(solution, cities):
    route1, route2 = solution
    return total_distance(route1, cities) + total_distance(route2, cities)

def initial_solution(n_cities):
    cities = list(range(n_cities))
    random.shuffle(cities)
    
    mid = n_cities // 2
    return [cities[:mid], cities[mid:]]

def random_swap(solution):
    route1, route2 = solution[0][:], solution[1][:]
    
    if random.random() < 0.5:
        if len(route1) > 1:
            i, j = random.sample(range(len(route1)), 2)
            route1[i], route1[j] = route1[j], route1[i]
    else:
        if len(route1) > 0 and len(route2) > 0:
            i = random.randint(0, len(route1)-1)
            j = random.randint(0, len(route2)-1)
            route1[i], route2[j] = route2[j], route1[i]
    
    return [route1, route2]

def simulated_annealing(cities, initial_temp, cooling_rate, stopping_temp):
    
    current_solution = initial_solution(len(cities))
    current_distance = total_distance_two_salesmen(current_solution, cities)
    
    best_solution = [current_solution[0][:], current_solution[1][:]]
    best_distance = current_distance
    
    temp = initial_temp
    
    while temp > stopping_temp:
        
        new_solution = random_swap(current_solution)
        new_distance = total_distance_two_salesmen(new_solution, cities)
        
        if new_distance < current_distance:
            current_solution = [new_solution[0][:], new_solution[1][:]]
            current_distance = new_distance
        else:
            prob = math.exp((current_distance - new_distance) / temp)
            if random.random() < prob:
                current_solution = [new_solution[0][:], new_solution[1][:]]
                current_distance = new_distance
        
        if current_distance < best_distance:
            best_solution = [current_solution[0][:], current_solution[1][:]]
            best_distance = current_distance
        
        temp *= cooling_rate
    
    return best_solution, best_distance

cities = [
    (10, 20),  
    (35, 15),  
    (5, 40),   
    (25, 30),  
    (15, 25), 
    (40, 35), 
    (20, 40),  
    (50, 10)   
]

initial_temp = 10000
cooling_rate = 0.995
stopping_temp = 1

best_solution, best_distance = simulated_annealing(
    cities, initial_temp, cooling_rate, stopping_temp
)

print("Rute Salesman 1:", best_solution[0])
print("Rute Salesman 2:", best_solution[1])
print("Total jarak minimum:", best_distance)
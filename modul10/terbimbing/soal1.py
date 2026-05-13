import networkx as nx
import matplotlib.pyplot as plt
import math

G_europe = nx.Graph()

edges_europe = [
    ('Arad', 'Zerind', 75),
    ('Arad', 'Sibiu', 140),
    ('Arad', 'Timisoara', 118),
    ('Zerind', 'Oradea', 71),
    ('Oradea', 'Sibiu', 151),
    ('Timisoara', 'Lugoj', 111),
    ('Lugoj', 'Mehadia', 70),
    ('Mehadia', 'Dobreta', 75),
    ('Dobreta', 'Craiova', 120),
    ('Craiova', 'Rimnicu Vilcea', 146),
    ('Craiova', 'Pitesti', 138),
    ('Rimnicu Vilcea', 'Sibiu', 80),
    ('Rimnicu Vilcea', 'Pitesti', 97),
    ('Sibiu', 'Fagaras', 99),
    ('Fagaras', 'Bucharest', 211),
    ('Pitesti', 'Bucharest', 101),
]

G_europe.add_weighted_edges_from(edges_europe)
pos_europe = {
    'Arad': (0,4),
    'Zerind': (1,5),
    'Oradea': (2,6),
    'Sibiu': (3,4),
    'Timisoara': (0,2),
    'Lugoj': (1,1),
    'Mehadia': (1,0),
    'Dobreta': (1,-1),
    'Craiova': (3,-1),
    'Rimnicu Vilcea': (3,2),
    'Pitesti': (4,0),
    'Fagaras': (5,4),
    'Bucharest': (6,0)
}
goal = "Bucharest"

def heuristic(node):
    x1, y1 = pos_europe[node]
    x2, y2 = pos_europe[goal]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

path_europe = nx.astar_path(
    G_europe,
    source="Arad",
    target="Bucharest",
    heuristic=heuristic,
    weight=lambda u, v, d: 0  
)

print("=== GREEDY BFS (EUROPE) ===")
print("Jalur:", " -> ".join(path_europe))

plt.figure(figsize=(12,7))

nx.draw(
    G_europe,
    pos_europe,
    with_labels=True,
    node_color="lightblue",
    node_size=1500,
    font_weight="bold",
    edgecolors="black"
)

plt.title("Graph Eropa (Romania Map)")
plt.axis("off")
plt.show()
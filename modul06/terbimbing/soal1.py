import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

edges = [
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
    ('Giurgiu', 'Bucharest', 90),
    ('Urziceni', 'Bucharest', 85),
    ('Urziceni', 'Hirsova', 98),
    ('Urziceni', 'Vaslui', 142),
    ('Hirsova', 'Eforie', 86),
    ('Vaslui', 'Iasi', 92),
    ('Iasi', 'Neamt', 87)
]

G.add_weighted_edges_from(edges)

pos = {
    "Arad": (0,4),
    "Zerind": (1,5),
    "Oradea": (2,6),
    "Sibiu": (3,4),
    "Timisoara": (0,2),
    "Lugoj": (1,1),
    "Mehadia": (1,0),
    "Dobreta": (1,-1),
    "Craiova": (3,-1),
    "Rimnicu Vilcea": (3,2),
    "Pitesti": (4,0),
    "Fagaras": (5,4),
    "Bucharest": (6,0),
    "Giurgiu": (6,-1),
    "Urziceni": (7,1),
    "Hirsova": (9,1),
    "Eforie": (10,0),
    "Vaslui": (8,3),
    "Iasi": (7,4),
    "Neamt": (6,5)
}

plt.figure(figsize=(14,8))

nx.draw(
    G, pos,
    with_labels=True,
    node_color="red",
    node_size=1500,
    font_color="white",
    font_weight="bold",
    width=2
)

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='blue')

plt.title("Graf Peta Romania (Weighted Graph)")
plt.show()

print("\nDFS dari Arad ke Neamt:")

visited_order = ["Arad"]
goal = "Neamt"

for u, v in nx.dfs_edges(G, source='Arad'):
    visited_order.append(v)
    if v == goal:
        break

print(" -> ".join(visited_order))
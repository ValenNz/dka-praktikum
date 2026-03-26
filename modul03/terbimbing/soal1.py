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

print("=== GRAF ROMANIA ===")
print(f"Jumlah node (kota): {G.number_of_nodes()}")
print(f"Jumlah edge (jalur): {G.number_of_edges()}")
print(f"Kota-kota: {list(G.nodes())}")
print()

print("=" * 80)
print("=== SEMUA PASANGAN SHORTEST PATH (ALL PAIRS SHORTEST PATH) ===")
print("=" * 80)

all_shortest_paths = dict(nx.all_pairs_dijkstra_path(G, weight='weight'))
all_shortest_path_lengths = dict(nx.all_pairs_dijkstra_path_length(G, weight='weight'))


print("\n=== CONTOH SHORTEST PATH PENTING ===")
print("=" * 80)

important_routes = [
    ('Arad', 'Bucharest'),
    ('Arad', 'Iasi'),
    ('Zerind', 'Bucharest'),
    ('Timisoara', 'Neamt')
]

for source, target in important_routes:
    path = nx.dijkstra_path(G, source=source, target=target, weight='weight')
    distance = nx.dijkstra_path_length(G, source=source, target=target, weight='weight')
    path_str = " -> ".join(path)
    print(f"\n{source} ke {target}:")
    print(f"  Rute: {path_str}")
    print(f"  Total jarak: {distance} km")

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

plt.figure(figsize=(14, 8))

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=1500,
    node_color="lightblue",
    edgecolors="black",
    font_size=8,
    font_weight="bold",
    width=2
)

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7)

plt.title("Romania Map Graph - Weighted Graph", fontsize=14, fontweight='bold', pad=20)
plt.axis("off")
plt.tight_layout()
plt.show()
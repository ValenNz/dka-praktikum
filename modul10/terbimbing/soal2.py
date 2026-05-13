import networkx as nx
import matplotlib.pyplot as plt
import math

G_jawa = nx.Graph()

edges_jawa = [
    ('Jakarta', 'Bandung', 270),
    ('Jakarta', 'Cirebon', 327),
    ('Bandung', 'Cirebon', 120),
    ('Bandung', 'Yogyakarta', 373),
    ('Cirebon', 'Yogyakarta', 210),
    ('Cirebon', 'Semarang', 305),
    ('Yogyakarta', 'Semarang', 109),
    ('Yogyakarta', 'Surakarta', 60),
    ('Semarang', 'Surakarta', 97),
    ('Semarang', 'Surabaya', 369),
    ('Surakarta', 'Malang', 370),
    ('Surabaya', 'Malang', 94)
]

G_jawa.add_weighted_edges_from(edges_jawa)

pos = {
    'Jakarta': (0, 4),
    'Bandung': (2, 2),
    'Cirebon': (3, 4),
    'Yogyakarta': (6, 0),
    'Surakarta': (8, 1),
    'Semarang': (7, 4),
    'Surabaya': (11, 4),
    'Malang': (10, 0)
}

goal = "Malang"

def heuristic(n):
    x1, y1 = pos[n]
    x2, y2 = pos[goal]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

path = nx.astar_path(
    G_jawa,
    source="Jakarta",
    target="Malang",
    heuristic=heuristic,
    weight=lambda u, v, d: 0   
)

print("=== GREEDY BEST-FIRST SEARCH (JAWA) ===")
print("Jalur:", " -> ".join(path))

plt.figure(figsize=(12, 6))

nx.draw(
    G_jawa,
    pos,
    with_labels=True,
    node_color='lightgreen',
    node_size=2000,
    font_size=10,
    font_weight='bold',
    edge_color='gray',
    width=2
)

edge_labels = nx.get_edge_attributes(G_jawa, 'weight')
nx.draw_networkx_edge_labels(G_jawa, pos, edge_labels=edge_labels, font_size=8)

plt.title("Greedy Best-First Search - Pulau Jawa")
plt.axis('off')
plt.tight_layout()
plt.show()
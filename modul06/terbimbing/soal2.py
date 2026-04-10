import networkx as nx
import matplotlib.pyplot as plt


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

plt.figure(figsize=(12, 6))

nx.draw(
    G_jawa, pos,
    with_labels=True,
    node_color='red',
    node_size=2000,
    font_color='white',
    font_weight='bold',
    width=2
)

edge_labels = nx.get_edge_attributes(G_jawa, 'weight')
nx.draw_networkx_edge_labels(G_jawa, pos, edge_labels=edge_labels, font_color='blue')

plt.title("Graf Kota-Kota Besar di Pulau Jawa")
plt.show()

print("\nDFS dari Bandung ke Malang:")

goal = "Malang"
path = ["Bandung"]

for u, v in nx.dfs_edges(G_jawa, source='Bandung'):
    path.append(v)
    
    if v == goal:
        break

print(" -> ".join(path))
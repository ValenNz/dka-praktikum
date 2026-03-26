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
    ('Surakarta', 'Surabaya', 370),
    ('Surabaya', 'Malang', 94)
]

G_jawa.add_weighted_edges_from(edges_jawa)

print("=== GRAF KOTA-KOTA JAWA ===")
print(f"Jumlah node: {G_jawa.number_of_nodes()}")
print(f"Jumlah edge: {G_jawa.number_of_edges()}")
print()

print("=== SHORTEST PATH ===")
print(f"Jakarta ke Surabaya: {nx.shortest_path(G_jawa, 'Jakarta', 'Surabaya', weight='weight')}")
print(f"Jarak: {nx.shortest_path_length(G_jawa, 'Jakarta', 'Surabaya', weight='weight')} km")
print()

print(f"Bandung ke Malang: {nx.shortest_path(G_jawa, 'Bandung', 'Malang', weight='weight')}")
print(f"Jarak: {nx.shortest_path_length(G_jawa, 'Bandung', 'Malang', weight='weight')} km")
print()

print(f"Jakarta ke Yogyakarta: {nx.shortest_path(G_jawa, 'Jakarta', 'Yogyakarta', weight='weight')}")
print(f"Jarak: {nx.shortest_path_length(G_jawa, 'Jakarta', 'Yogyakarta', weight='weight')} km")

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
nx.draw(G_jawa, pos, with_labels=True, node_color='lightgreen', 
        node_size=2000, font_size=9, font_weight='bold',
        edge_color='gray', width=2)
edge_labels = nx.get_edge_attributes(G_jawa, 'weight')
nx.draw_networkx_edge_labels(G_jawa, pos, edge_labels=edge_labels, font_size=8)
plt.title('Graf Kota-Kota Besar di Pulau Jawa')
plt.axis('off')
plt.tight_layout()
plt.show()
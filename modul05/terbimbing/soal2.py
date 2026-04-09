import networkx as nx
import matplotlib.pyplot as plt


def show_graph(G, pos=None, title=''):
    if pos is None:
        pos = nx.spring_layout(G)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color='lightgreen',
        node_size=2000,
        font_size=9,
        font_weight='bold',
        edge_color='gray',
        width=2
    )

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(
        G, pos,
        edge_labels=edge_labels,
        font_size=8
    )

    plt.title(title)
    plt.axis('off')
    plt.show()


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

show_graph(G_jawa, pos=pos, title="Graf Kota Jawa - BFS")

path = nx.shortest_path(G_jawa, source='Bandung', target='Malang')

print("\nPath Bandung ke Malang (BFS / jumlah langkah):")
print(" -> ".join(path))

path_weighted = nx.shortest_path(G_jawa, 'Bandung', 'Malang', weight='weight')
distance = nx.shortest_path_length(G_jawa, 'Bandung', 'Malang', weight='weight')

print("\nKESIMPULAN:")
print("BFS menggunakan nx.bfs_edges() untuk traversal graf.")
print("BFS mengeksplorasi node berdasarkan level.")
print("BFS tidak mempertimbangkan weight.")
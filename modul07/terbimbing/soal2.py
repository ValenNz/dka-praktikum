import networkx as nx
import matplotlib.pyplot as plt

def show_graph(G, pos=None, title=''):
    if pos is None:
        pos = nx.spring_layout(G)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color='red',
        node_size=2000,
        font_color="white",
        font_weight="bold",
        width=2
    )

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='blue')

    plt.title(title)
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

print("Elemen pada Graf Jawa:")
print("Node:", list(G_jawa.nodes()))
print("Edge:", list(G_jawa.edges()))
print("Jumlah Node:", G_jawa.number_of_nodes())
print("Jumlah Edge:", G_jawa.number_of_edges())


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

show_graph(G_jawa, pos, title="Graf Pulau Jawa (UCS)")


def heuristic(a, b):
    return 0

path = nx.astar_path(G_jawa, 'jakarta ', 'surakarta',
                     heuristic=heuristic,
                     weight='weight')

cost = nx.astar_path_length(G_jawa, 'jakarta ', 'surakarta',
                            heuristic=heuristic,
                            weight='weight')

print("\n=== HASIL UCS ===")
print("Path:", path)
print("Total Cost:", cost)
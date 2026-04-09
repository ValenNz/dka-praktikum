import networkx as nx
import matplotlib.pyplot as plt

def show_graph(G, pos=None, title=''):
    if pos is None:
        pos = nx.spring_layout(G)

    nx.draw(
        G, pos,
        with_labels=True,
        node_color='red',
        node_size=2000,
        font_color='white',
        font_weight='bold',
        width=2
    )

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title(title)
    plt.show()

G = nx.Graph()

edges = [
    ('Bandung','Jakarta',150),
    ('Bandung','Yogyakarta',380),
    ('Jakarta','Semarang',450),
    ('Yogyakarta','Surabaya',330),
    ('Semarang','Surabaya',350)
]

G.add_weighted_edges_from(edges)

show_graph(G, title="Graf Kota Berbobot")

bfs_edges = list(nx.bfs_edges(G, source='Bandung'))

print("Urutan BFS (edge):")
for u, v in bfs_edges:
    print(f"{u} - {v}")
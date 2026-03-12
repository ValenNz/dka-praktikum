import matplotlib.pyplot as plt
import networkx as nx

pos = {
    'A': [0.93888004, -0.0449161],
    'B': [-0.73226196, -0.53345128],
    'C': [0.29334637, 1.0],
    'D': [-0.79991428, 0.56134392],
    'E': [0.29994983, -0.98297654]
}

def show_graph(G, pos=None, title=''):
    if pos is None:
        pos = nx.spring_layout(G)
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color='red',
        node_size=2000,
        font_color='white',
        font_weight='bold',
        width=5
    )
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edge_labels,
        font_color='blue',
        font_weight='bold',
        font_size=12,
    )
    plt.margins(0.2)
    plt.title(title)
    plt.show()

# criar grafo fora da função
G_undirected = nx.Graph()
G_undirected.add_nodes_from(pos.keys())
# opcional: adicionar arestas:
# G_undirected.add_weighted_edges_from([('A','B',1), ('B','C',2), ...])

show_graph(G_undirected, pos=pos, title="Undirected Graph Kosong")
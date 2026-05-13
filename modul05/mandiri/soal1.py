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

    plt.title(title)
    plt.show()

G = nx.Graph()

edges = [
    ('A','B'), ('A','C'),
    ('B','D'), ('B','E'),
    ('C','F'), ('C','G')
]

G.add_edges_from(edges)

pos = {
    'A': (0,3),
    'B': (-1,2), 'C': (1,2),
    'D': (-1.5,1), 'E': (-0.5,1),
    'F': (0.5,1), 'G': (1.5,1)
}

bfs_edges = list(nx.bfs_edges(G, source='A'))

print("Urutan BFS (edge):")
for u, v in bfs_edges:
    print(f"{u} - {v}")

print("\nUrutan BFS (node):")
bfs_nodes = ['A'] + [v for u, v in bfs_edges]
print(" -> ".join(bfs_nodes))

show_graph(G, pos, "Graf Tree BFS")
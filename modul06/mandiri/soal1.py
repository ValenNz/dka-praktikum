import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edges_from([
    ('A', 'B'), ('A', 'C'),
    ('B', 'D'), ('B', 'E'),
    ('C', 'F'), ('C', 'G')
])

pos = {
    'A': (0, 3),
    'B': (-2, 2), 'C': (2, 2),
    'D': (-3, 1), 'E': (-1, 1),
    'F': (1, 1), 'G': (3, 1)
}

nx.draw(
    G, pos,
    with_labels=True,
    node_color='red',
    node_size=2000,
    font_color='white'
)

plt.title("Tree DFS")
plt.show()

print("=== DFS Tanpa Depth Limit ===")

for i, edge in enumerate(nx.dfs_edges(G, source='A'), start=1):
    print(f"{i}. {edge[0]} -> {edge[1]}")

print("\n=== DFS Dengan Depth Limit = 2 ===")
for i, edge in enumerate(nx.dfs_edges(G, source='A', depth_limit=2), start=1):
    print(f"{i}. {edge[0]} -> {edge[1]}")
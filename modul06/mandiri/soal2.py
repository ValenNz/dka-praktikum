import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_edges_from([
    ('A', 'B'), ('A', 'C'),
    ('B', 'D'), ('B', 'E'),
    ('C', 'E'), ('C', 'F'),
    ('E', 'F')
])

pos = {
    'A': (0, 2),
    'B': (1, 3), 'C': (1, 1),
    'D': (2, 4), 'E': (2, 2),
    'F': (3, 2)
}

nx.draw(
    G, pos,
    with_labels=True,
    node_color='red',
    node_size=2000,
    font_color='white',
    arrows=True
)

plt.title("Directed Graph DFS")
plt.show()

print("=== Urutan DFS ===")

goal = 'F'
found = False

for i, edge in enumerate(nx.dfs_edges(G, source='A'), start=1):
    print(f"{i}. {edge[0]} -> {edge[1]}")

    if edge[1] == goal:
        found = True
        break

if found:
    print(f"\nNode {goal} ditemukan")
else:
    print(f"\nNode {goal} tidak ditemukan")
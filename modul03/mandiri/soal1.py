import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edges_from([
    ('A','B'),
    ('A','C'),
    ('B','D'),
    ('C','D'),
    ('D','E')
])

plt.figure()
pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue')
plt.title("Graf Soal 1")

plt.show()

# =========================
# 2. Degree tiap node
# =========================
print("Degree tiap node:")
for node in G.nodes():
    print(f"{node} : {G.degree(node)}")

# =========================
# Neighbor node D
# =========================
print("\nNeighbor dari node D:")
neighbors_D = list(G.neighbors('D'))
print(neighbors_D)

# =========================
# 3. Cek Cycle
# =========================
cycle = list(nx.cycle_basis(G))

print("\nCek Cycle:")
if cycle:
    print("Graf memiliki cycle:", cycle)
    print("Contoh cycle: A -> B -> D -> C -> A")
else:
    print("Graf tidak memiliki cycle")

# =========================
# 4. Analisis Node Penting
# =========================
max_degree_node = max(G.degree, key=lambda x: x[1])

print("\nNode paling penting:")
print(f"Node {max_degree_node[0]} dengan degree {max_degree_node[1]}")
print("Alasan: karena memiliki koneksi terbanyak dan menjadi penghubung utama")

# =========================
# VISUALISASI GRAF
# =========================

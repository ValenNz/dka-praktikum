import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_weighted_edges_from([
    ('A','B',4),
    ('A','C',2),
    ('B','C',1),
    ('B','D',5),
    ('C','D',8),
    ('C','E',10),
    ('D','E',2)
])

plt.figure()
pos = nx.spring_layout(G)


nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightgreen')


labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("Weighted Graph Soal 2")
plt.show()

# =========================
# 2. Shortest Path A ke E
# =========================
path = nx.shortest_path(G, source='A', target='E', weight='weight')
distance = nx.shortest_path_length(G, source='A', target='E', weight='weight')

print("\nJalur terpendek dari A ke E:", path)
print("Total weight:", distance)

# =========================
# Analisis Jalur Awal
# =========================
print("\nAnalisis:")
print("- Jalur dipilih karena memiliki total weight paling kecil")
print("- Weight berperan sebagai biaya/jarak dalam menentukan jalur optimal")

# =========================
# 3. Ubah Weight (C,E) jadi 1
# =========================
G['C']['E']['weight'] = 1

print("\n=== SETELAH PERUBAHAN WEIGHT (C,E)=1 ===")

path_baru = nx.shortest_path(G, source='A', target='E', weight='weight')
distance_baru = nx.shortest_path_length(G, source='A', target='E', weight='weight')

print("Jalur terpendek baru:", path_baru)
print("Total weight baru:", distance_baru)

# =========================
# Analisis Perubahan
# =========================
print("\nAnalisis Perubahan:")
print("- Jalur berubah karena ada edge dengan weight lebih kecil")
print("- Algoritma selalu memilih total weight paling minimum")

# =========================
# 4. Visualisasi Graph
# =========================

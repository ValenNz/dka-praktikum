# ============================================================
# IMPORT LIBRARY YANG DIPERLUKAN
# ============================================================
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

# ============================================================
# POIN 1: FUNGSI & PROSEDUR
# ============================================================
# Fungsi menggunakan 'return' untuk mengembalikan nilai
def hitung_diskon(harga, persen):
    return harga - (harga * persen / 100)

# Prosedur (hanya menjalankan aksi, tidak mengembalikan nilai)
def tampilkan_info(nama, hasil):
    print(f"[Poin 1] {nama} mendapatkan harga: Rp{hasil:.0f}")

harga_asli = 100000
hasil_diskon = hitung_diskon(harga_asli, 20)
tampilkan_info("Poin 1", hasil_diskon)

# ============================================================
# POIN 2: INPUT, OUTPUT & KONVERSI TIPE DATA
# ============================================================
# (Simulasi input agar kode bisa dijalankan otomatis)
nama_user = "Mahasiswa"
umur = int("20")
tinggi = float("170.5")
print(f"\n[Poin 2] Halo {nama_user}, umur {umur} tahun, tinggi {tinggi} cm")

# ============================================================
# POIN 3: OPERASI DASAR
# ============================================================
a, b = 15, 4
print(f"\n[Poin 3] Penjumlahan: {a+b}, Pengurangan: {a-b}")
print(f"Perkalian: {a*b}, Pembagian: {a/b}, Modulus: {a%b}")
print(f"Rata-rata: {np.mean([80, 90, 70, 85])}")

# ============================================================
# POIN 4: PENGKONDISIAN (if, elif, else & operator logika)
# ============================================================
nilai = 78
kehadiran = 85
if nilai >= 75 and kehadiran >= 80:
    status = "LULUS"
elif nilai >= 60:
    status = "REMEDI"
else:
    status = "TIDAK LULUS"
print(f"\n[Poin 4] Status: {status}")

# ============================================================
# POIN 5: PERULANGAN (for, while, range(), break)
# ============================================================
print("\n[Poin 5] For dengan range:")
for i in range(1, 4):
    print(i, end=" ")

print("\nWhile dengan break:")
count = 0
while True:  # perulangan berulang terus-menerus
    count += 1
    if count == 3:
        break
    print(count, end=" ")

# ============================================================
# POIN 6: FIZZBUZZ (urutan pengecekan modulus penting!)
# ============================================================
print("\n\n[Poin 6] FizzBuzz:")
for i in range(1, 16):
    if i % 3 == 0 and i % 5 == 0:  # Cek kelipatan 15 dulu
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")

# ============================================================
# POIN 7: LIST & DICTIONARY
# ============================================================
print("\n\n[Poin 7] List & Dictionary:")
buah = ["Apel", "Mangga"]
buah.append("Jeruk")          # Menambah isi
print("List:", buah[0])       # Akses data

data_mhs = {"Nama": "Budi", "NIM": "123"}
data_mhs["Prodi"] = "Informatika"  # Menambah isi
print("Dict:", data_mhs["Nama"])   # Akses data

# Iterasi dictionary
for key, val in data_mhs.items():
    print(f"  {key}: {val}")

# ============================================================
# POIN 8 & 9: DASAR NUMPY & ATRIBUT ARRAY
# ============================================================
arr_1d = np.array([10, 20, 30])
arr_2d = np.array([[1, 2], [3, 4]])
arr_acak = np.random.randint(1, 50, size=(2, 3))

print(f"\n[Poin 8] Array 1D: {arr_1d}")
print(f"Array 2D:\n{arr_2d}")
print(f"Array Acak:\n{arr_acak}")

print(f"\n[Poin 9] ndim: {arr_2d.ndim}, shape: {arr_2d.shape}")
print(f"size: {arr_2d.size}, dtype: {arr_2d.dtype}")

# ============================================================
# POIN 10: OPERASI ARRAY NUMPY
# ============================================================
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(f"\n[Poin 10] Penjumlahan array: {x + y}")
print(f"Pembagian array: {y / 2}")
print(f"Gabung vertikal (vstack):\n{np.vstack((x, y))}")
print(f"Statistik -> Mean: {np.mean(x)}, Max: {np.max(y)}, Min: {np.min(x)}")

# ============================================================
# POIN 11 & 12: MATPLOTLIB DASAR & GRAFIK
# ============================================================
# Catatan: plt.show() akan menampilkan jendela grafik. 
# Di lingkungan otomatis/jupyter, gunakan %matplotlib inline atau plt.savefig()
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.bar(['A', 'B', 'C'], [10, 25, 15], color='skyblue')
plt.title("Bar Chart")
plt.xlabel("Kategori")
plt.ylabel("Nilai")

plt.subplot(1, 2, 2)
plt.pie([10, 25, 15], labels=['A', 'B', 'C'], autopct='%1.1f%%')
plt.title("Pie Chart")

# plt.tight_layout()
# plt.show()  # Uncomment saat dijalankan di IDE/Jupyter
print("\n[Poin 11 & 12] Kode Matplotlib siap dijalankan.")

# ============================================================
# POIN 13 - 17: NETWORKX (Graph, Undirected, Directed, Weighted, Neighbor)
# ============================================================
print("\n[Poin 13-17] NetworkX Graph:")
# 13 & 14: Undirected Graph
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (2, 3), (3, 4), (1, 4)])  # Tidak berarah: 1-2 == 2-1

# 15: Directed Graph
DG = nx.DiGraph()
DG.add_edges_from([(1, 2), (2, 3), (3, 4)])  # Berarah: 1->2 berbeda dengan 2->1

# 16: Weighted Graph
WG = nx.Graph()
WG.add_weighted_edges_from([(1, 2, 4), (2, 3, 2), (3, 4, 5), (1, 4, 8)])
weights = nx.get_edge_attributes(WG, 'weight')

# 17: Traversal & Neighbor
print(f"Nodes di G: {list(G.nodes())}")
print(f"Tetangga node 1 di G: {list(G.neighbors(1))}")
print(f"Bobot edge WG: {weights}")

# ============================================================
# POIN 18, 19, 20: BREADTH FIRST SEARCH (BFS)
# ============================================================
def bfs(graph, start):
    """
    Poin 18: Menjelajah per level, prioritaskan tetangga terdekat
    Poin 19: Menggunakan Queue (FIFO) & Visited set
    Poin 20: Masukkan start -> ambil -> cek neighbor -> ulang sampai queue kosong
    """
    queue = deque([start])      # FIFO
    visited = {start}
    result = []
    
    while queue:
        node = queue.popleft()  # Ambil dari depan queue
        result.append(node)
        
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result

print(f"\n[Poin 18-20] BFS dari node 1: {bfs(G, 1)}")

# ============================================================
# POIN 21, 22, 23: DEPTH FIRST SEARCH (DFS)
# ============================================================
def dfs(graph, start, visited=None):
    """
    Poin 21: Menelusuri sedalam mungkin, lalu backtracking
    Poin 22: Menggunakan Stack (rekursi implisit) & Visited set
    Poin 23: Kunjungi -> tandai visited -> neighbor pertama -> mentok -> kembali
    """
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]
    
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    return result

print(f"[Poin 21-23] DFS dari node 1: {dfs(G, 1)}")

# ============================================================
# POIN 24, 25, 26, 27: UNIFORM COST SEARCH (UCS)
# ============================================================
"""
Poin 24: UCS mencari shortest path berdasarkan total cost terkecil pada weighted graph.
Poin 25: Weight berfungsi sebagai biaya, jarak, atau latency antar node.
Poin 26: Di NetworkX, UCS dapat diimplementasikan via nx.astar_path() dengan heuristic=0.
Poin 27: Total cost dihitung menggunakan nx.path_weight()
"""
source_node = 1
target_node = 4

# Heuristic bernilai 0 membuat A* berjalan persis seperti UCS/Dijkstra
path_ucs = nx.astar_path(WG, source=source_node, target=target_node, 
                         heuristic=lambda u, v: 0, weight='weight')
total_cost = nx.path_weight(WG, path_ucs, weight='weight')

print(f"\n[Poin 24-27] UCS dari {source_node} ke {target_node}")
print(f"Jalur terpendek: {path_ucs}")
print(f"Total Cost: {total_cost}")

# ============================================================
# POIN 28: KONSEP DASAR AI (Queue, Stack, Visited, Traversal, Shortest Path, Heuristic)
# ============================================================
print("\n[Poin 28] Ringkasan Konsep Dasar AI:")
print("- Queue (FIFO): Digunakan di BFS, menjelajah level per level.")
print("- Stack (LIFO): Digunakan di DFS, menjelajah sedalam mungkin (backtracking).")
print("- Visited Set: Mencegah siklus/perulangan tak terbatas pada graph.")
print("- Traversal: Proses mengunjungi semua node/edge secara sistematis.")
print("- Shortest Path: Jalur dengan total bobot/cost terendah antar dua node.")
print("- Heuristic: Fungsi estimasi biaya ke tujuan. Jika 0, A* = UCS/Dijkstra.")
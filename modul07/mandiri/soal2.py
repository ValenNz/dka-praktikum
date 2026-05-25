import heapq
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
        font_color='white',
        font_weight='bold',
        width=3
    )

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edge_labels,
        font_color='blue',
        font_weight='bold'
    )

    plt.title(title)
    plt.show()

graph = {
    'Surabaya': [('Malang', 2), ('Madiun', 5)],
    'Malang': [('Surabaya', 2), ('Kediri', 4)],
    'Madiun': [('Surabaya', 5), ('Kediri', 1), ('Solo', 6)],
    'Kediri': [('Malang', 4), ('Madiun', 1), ('Yogyakarta', 7)],
    'Solo': [('Madiun', 6), ('Yogyakarta', 3)],
    'Yogyakarta': [('Kediri', 7), ('Solo', 3)]
}
G = nx.Graph()

for node in graph:
    for neighbor, weight in graph[node]:
        G.add_edge(node, neighbor, weight=weight)

pos = {
    'Surabaya': (0, 2),
    'Malang': (-2, 1),
    'Madiun': (2, 1),
    'Kediri': (0, 0),
    'Solo': (3, -1),
    'Yogyakarta': (1, -2)
}

show_graph(G, pos=pos, title='Graf Distribusi Barang')

def ucs(graph, start, goal):
    queue = [(0, start, [start])]
    visited = []
    expansion = []

    while queue:
        cost, node, path = heapq.heappop(queue)
        if node not in visited:
            visited.append(node)
            expansion.append(node)
            if node == goal:
                return path, cost, visited, expansion
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    total_cost = cost + weight
                    heapq.heappush(
                        queue,
                        (total_cost, neighbor, path + [neighbor])
                    )
    return None, None, visited, expansion

start = input("Masukkan kota asal : ")
goal = input("Masukkan kota tujuan : ")

path, cost, visited, expansion = ucs(graph, start, goal)

if path:
    print("\nJalur terbaik :")
    print(" -> ".join(path))
    print("\nTotal biaya :")
    print(cost)
    print("\nNode yang dikunjungi :")
    print(visited)
    print("\nUrutan ekspansi node :")
    print(expansion)
else:
    print("Jalur tidak ditemukan")git
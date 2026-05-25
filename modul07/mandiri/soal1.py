import heapq
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('D', 5), ('E', 10)],
    'C': [('A', 2), ('F', 3)],
    'D': [('B', 5)],
    'E': [('B', 10), ('F', 4), ('G', 6)],
    'F': [('C', 3), ('E', 4), ('G', 2)],
    'G': [('E', 6), ('F', 2)]
}
def ucs(graph, start, goal):
    queue = [(0, start, [start])]
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)
        if node == goal:
            return path, cost
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    total_cost = cost + weight
                    heapq.heappush(
                        queue,
                        (total_cost, neighbor, path + [neighbor])
                    )
    return None, None

start = input("Masukkan node awal : ").upper()
goal = input("Masukkan node tujuan : ").upper()
path, cost = ucs(graph, start, goal)

if path:
    print("Jalur tercepat dari", start, "ke", goal, ":")
    print(" -> ".join(path))
    print("Total cost :", cost)

else:
    print("Jalur tidak ditemukan")
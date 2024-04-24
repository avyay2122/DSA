import heapq

def sol(graph, start, dest):
    mst = []
    visited = set()
    heap = [(0, start, dest)]
    while heap:
        weight, source, dest = heapq.heappop(heap)
        if dest not in visited:
            visited.add(dest)
            mst.append((weight, source, dest))
            for neighbour, neighbour_weight in graph[dest]:
                if neighbour not in visited:
                    heapq.heappush(heap, (neighbour_weight, dest, neighbour))
    return mst

graph = {
    'A': [('B', 7), ('D', 5)],
    'B': [('A', 7), ('E', 7), ('D', 9), ('C', 8)],
    'C': [('B', 8), ('E', 5)],
    'D': [('A', 5), ('B', 9), ('E', 15), ('F', 6)],
    'E': [('B', 7), ('C', 5), ('D', 15), ('F', 8)],
    'F': [('D', 6), ('E', 8)]
}

start_vertex = 'A'  # Set start_vertex to 'A'
mst = sol(graph, start_vertex, start_vertex)
print("MST:", mst)

min_spanning_cost = 0
for e in mst:
    min_spanning_cost += e[0]
print("Minimum spanning tree cost:", min_spanning_cost)

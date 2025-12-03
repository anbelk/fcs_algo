#      "a" -1-  "e"
#     /3   \7      \4
#   "b" -5- "c" -2- "d"

# input:
#     graph:
#     {
#         "a": {"b": 3, "c": 7, "e": 1},
#         "b": {"a": 3, "c": 5},
#         "c": {"a": 7, "b": 5, "d": 2},
#         "d": {"c": 2, "e": 4},
#         "e": {"a": 1, "d": 4}
#     }
#     start: "c"

# output:
#     {"a": 6, "b": 5, "c": 0, "d": 2, "e": 6}
import heapq


def dijkstra(graph, start):
    dists = {node: float('inf') for node in graph}
    dists[start] = 0

    heap = [(start, 0)]

    visited = set()

    while heap:
        curr_node, curr_dist = heapq.heappop(heap)
        if curr_node in visited:
            continue

        visited.add(curr_dist)

        if curr_dist > dists[curr_node]:
            continue

        for neighbour, weight in graph[curr_node].items():
            distance = curr_dist + weight
            
            if distance < dists[neighbour]:
                dists[neighbour] = distance
                heapq.heappush(heap, (neighbour, distance))
                
    return dists
from collections import deque


def find_adj_comps(graph: dict) -> list:
    comps = []
    visited = set()

    for start in graph.keys():
        if start in visited:
            continue
        
        visited.add(start)
        nodes_deque = deque([start])
        comps.append([start])

        while nodes_deque:
            parent = nodes_deque.popleft()

            for child in graph[parent]:
                if child not in visited:
                    visited.add(child)
                    nodes_deque.append(child)
                    comps[-1].append(child)
    
    return comps
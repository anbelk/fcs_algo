from collections import deque

class DagExplorer:
    def __init__(self, adjacency_map):
        self.adj_map = adjacency_map
        self.vertex_status = {vertex: 0 for vertex in adjacency_map}
        self.final_order = deque()
        self.detected_loop = []
        self.loop_detected_flag = False
        self.path_stack = []

    def _explore_vertex(self, current_vertex):
        if self.loop_detected_flag:
            return True
        
        self.vertex_status[current_vertex] = 1
        self.path_stack.append(current_vertex)

        for neighbor in self.adj_map.get(current_vertex, []):
            if self.vertex_status[neighbor] == 1:
                self.loop_detected_flag = True
                cycle_start_index = self.path_stack.index(neighbor)
                self.detected_loop = self.path_stack[cycle_start_index:]
                return True
            elif self.vertex_status[neighbor] == 0:
                if self._explore_vertex(neighbor):
                    return True
        
        self.vertex_status[current_vertex] = 2
        self.path_stack.pop()
        self.final_order.appendleft(current_vertex)
        return False

    def process_graph(self):
        for vertex in list(self.adj_map.keys()):
            if self.vertex_status[vertex] == 0:
                if self._explore_vertex(vertex):
                    break

        if self.loop_detected_flag:
            return {"has_loop": True, "loop_path": self.detected_loop}
        else:
            return {"has_loop": False, "sorted_result": list(self.final_order)}
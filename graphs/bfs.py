from typing import List, Tuple, Optional, Dict


class Graph:
    def __init__(self, vertices: Optional[List]):
        self.vertices = vertices
        self.adj_dict = {vertex: [] for vertex in vertices}

    def add_edge(self, node1, node2):
        (self.adj_dict[node1]).append(node2)


class BFS:
    def __init__(self, graph: Graph):
        self.graph: Graph = graph
        self.visited = [False] * len(self.graph.vertices)

    def bfs(self, index=0) -> Optional[List]:
        queue = [graph.vertices[index]]
        self.visited[index] = True
        bfs = []
        while queue:
            val = queue.pop(0)
            bfs.append(val)
            edges = graph.adj_dict.get(val)

            for edge in edges:
                if not self.visited[edge]:
                    queue.append(edge)
                    self.visited[edge] = True

        return bfs


if __name__ == '__main__':
    graph = Graph([0, 1, 2, 3, 4, ])
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    bfs = BFS(graph)
    result = bfs.bfs(2)
    print(result)

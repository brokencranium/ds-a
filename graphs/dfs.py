from typing import Optional, List


class Graph:
    def __init__(self, vertices: Optional[List]):
        self.vertices = vertices
        self.adj_list = {vertex: [] for vertex in vertices}

    def add_edge(self, u, v):
        self.adj_list[u].append(v)


class DFS:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.visited = [False] * len(graph.vertices)

    def dfs(self, vertex=0) -> List[int]:
        stack = [self.graph.vertices[vertex]]
        self.visited[vertex] = True
        result = []

        while stack:
            vertex = stack.pop()
            edges = self.graph.adj_list.get(vertex)
            result.append(vertex)

            for edge in edges:
                if not self.visited[edge]:
                    self.visited[edge] = True
                    stack.append(edge)

        return result


if __name__ == '__main__':
    graph = Graph([0, 1, 2, 3, 4, ])
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    dfs: DFS = DFS(graph)
    result: List[int] = dfs.dfs(1)
    print(result)

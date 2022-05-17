from typing import List, Dict
from collections import namedtuple

Graph = namedtuple("Graph", ["nodes", "edges"])


class Adjacency:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.adj_dict: Dict[str, List[str]] = {}
        self.adj_matrix: List = []

    def build_list(self):
        self.adj_dict = {node: [] for node in self.graph.nodes}

        for edge in self.graph.edges:
            node1, node2 = edge
            self.adj_dict[node1].append(node2)
            self.adj_dict[node2].append(node1)

    def build_matrix(self):
        node_size = len(self.graph.nodes)
        self.adj_matrix = [[0 for j in range(node_size)] for i in range(node_size)]
        # self.adj_matrix = [None for i in range(node_size) [for j in node_size]]]
        for edge in edges:
            node1, node2 = edge
            self.adj_matrix[node1][node2] += 1
            self.adj_matrix[node2][node1] += 1


if __name__ == '__main__':
    nodes = ["A", "B", "C", "D"]
    edges = [("A", "B"), ("A", "B"),
             ("A", "C"), ("A", "C"),
             ("A", "D"),
             ("B", "D"),
             ("C", "D")
             ]
    graph = Graph(nodes, edges)
    adj = Adjacency(graph)
    print(adj.graph)
    adj.build_list()
    print(adj.adj_dict)

    nodes = list(range(4))
    edges = [(0, 1), (0, 1),
             (0, 2), (0, 2),
             (0, 3),
             (1, 3),
             (2, 3)
             ]
    graph = Graph(nodes, edges)
    adj = Adjacency(graph)
    adj.build_matrix()
    print(adj.adj_matrix)

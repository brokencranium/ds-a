from typing import List


# For undirected skip recursion if the adjacency list value points to the parent noe

class Graph:
    cycle_detected = True
    not_a_cycle = False

    def __init__(self, numCourses: int, prerequisites: List[List[int]]):
        self.vertices = list(range(numCourses))
        self.edges = prerequisites
        self.adj_dict = {course: [] for course in self.vertices}
        self.build_adj_dict(prerequisites)

    def build_adj_dict(self, pre_reqs):
        for req_a, req_b in pre_reqs:
            self.adj_dict[req_a].append(req_b)

    def course_pre_reqs(self):
        stack = []
        visited = []

        def dfs(pre_req) -> bool:
            if pre_req in stack:
                return self.cycle_detected

            stack.append(pre_req)

            for req in self.adj_dict.get(pre_req):
                if dfs(req):
                    return self.cycle_detected

            val = stack.pop()
            self.adj_dict[val] = []
            if val not in visited:
                visited.append(pre_req)

            return self.not_a_cycle

        for vertex in self.vertices:
            if dfs(vertex):
                return self.cycle_detected

        return self.not_a_cycle, visited


if __name__ == '__main__':
    # pre_reqs = [[0, 1], [1, 2], [0, 2], [2, 3], [3, 3]]
    # num_courses = 4
    # graph = Graph(num_courses, pre_reqs)
    # result = graph.course_pre_reqs()
    # if result:
    #     print('Cycle Detected')
    # else:
    #     print('Not a Cycle')
    #
    # pre_reqs = [[0, 1], [1, 2], [2, 3], [3, 4]]
    # num_courses = 5
    # graph = Graph(num_courses, pre_reqs)
    # result = graph.course_pre_reqs()
    # if result:
    #     print('Cycle Detected')
    # else:
    #     print('Not a Cycle')
    #
    # pre_reqs = [[0, 1], [1, 2], [2, 3], [3, 0]]
    # num_courses = 4
    # graph = Graph(num_courses, pre_reqs)
    # result = graph.course_pre_reqs()
    # if result:
    #     print('Cycle Detected')
    # else:
    #     print('Not a Cycle')
    #
    # pre_reqs = [[0, 1], [1, 2], [2, 3], [2, 4], [3, 5], [3, 6], [6, 7], [4, 8], [8, 9]]
    # num_courses = 10
    # graph = Graph(num_courses, pre_reqs)
    # result = graph.course_pre_reqs()
    # if result:
    #     print('Cycle Detected')
    # else:
    #     print('Not a Cycle')

    pre_reqs = [[5, 0], [4, 0], [0, 1], [0, 2], [1, 3], [3, 2]]
    num_courses = 6
    graph = Graph(num_courses, pre_reqs)
    result, sequence = graph.course_pre_reqs()
    if result:
        print('Cycle Detected')
    else:
        print('Not a Cycle')

    print(sequence[::-1])

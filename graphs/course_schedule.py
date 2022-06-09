from typing import List, Dict
from collections import defaultdict


class Solution:
    def get_graph_meta(self, prerequisites: List[List[int]]) -> Dict[int, List[int]]:
        adj_list = defaultdict(list)
        vertices = set()
        for prereq_a, prereq_b in prerequisites:
            vertices.add(prereq_a)
            vertices.add(prereq_b)
            adj_list[prereq_a].append(prereq_b)

        return adj_list, vertices

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = []
        stack = []

        def dfs(vertex):
            visited.append(vertex)
            stack.append(vertex)

            vertices = adj_list[vertex]
            for vertex in vertices:
                if vertex in stack:
                    return False

                if vertex in visited:
                    continue

                if not dfs(vertex):
                    return False
                else:
                    adj_list[stack.pop()] = []

            return True

        adj_list, vertices = self.get_graph_meta(prerequisites)
        for vertex in vertices:
            stack.clear()
            if not dfs(vertex):
                return False

        return True


if __name__ == '__main__':
    sol = Solution()
    # assert False == sol.canFinish(4, [[1, 0], [0, 1], [1, 3], [3, 4]])
    #
    # sol = Solution()
    # assert True == sol.canFinish(2, [[1, 0], [1, 3], [3, 4]])
    #
    # sol = Solution()
    # assert False == sol.canFinish(2, [[1, 0], [0, 1]])

    sol = Solution()
    assert True == sol.canFinish(3, [[0, 1], [0, 2], [1, 2]])

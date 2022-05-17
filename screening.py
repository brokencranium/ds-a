import collections
# Reconstruct itinerary from a list of tickets JFK has to fly to SFO, JFK to ATL, ATL to SFO
# and JFK to SFO to ATL

class Solution:
    def findItinerary(self, tickets):
        """

        :param tickets:
        :return:
        """
        # create a graph
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            graph[a].append(b)

        route = []
        def visit(airport):
            while graph[airport]:
                visit(graph[airport].pop())
            route.append(airport)

        visit('JFK')
        return route[::-1]

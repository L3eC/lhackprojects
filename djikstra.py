from heapq import heapify, heappush, heappop
# dictionary adjacency list
example_graph = {
    "A": {"B": 3, "C": 3},
    "B": {"A": 3, "D": 3.5, "E": 2.8},
    "C": {"A": 3, "E": 2.8, "F": 3.5},
    "D": {"B": 3.5, "E": 3.1, "G": 10},
    "E": {"B": 2.8, "C": 2.8, "D": 3.1, "G": 7},
    "F": {"G": 2.5, "C": 3.5},
    "G": {"F": 2.5, "E": 7, "D": 10},
}

class Graph:
    def __init__(self, graph: dict = {}):
        self.graph = graph

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = {}
        self.graph[node1][node2] = weight

    def shortest_distances(self, source: str):
        # create a dictionary with keys corresponding to nodes and values corresponding to distances
        # the distances of all nodes but source are infinite on code initialization
        distances = {node: float("inf") for node in self.graph}
        distances[source] = 0

        # *priority queue* being used exactly as such- queue up the nodes based on priority, or distance (i think)
        pq = [(0, source)]
        heapify(pq)

        visited = set() # empty set cuz we haven't visited any nodes yet

        while pq: # until the priority queue is empty; first round, pq will have infinite distances to everywhere
            current_distance, current_node = heappop(pq) # grab the node
            if current_node in visited:
                continue # skip if we've visited
                #  TODO: find out what the definition of visited is
                #  I think visited means we've checked out all its neighbors?
            else:
                visited.add(current_node)

            for neighbor, weight in self.graph[current_node].items():  # iterate over the neigbors of the node being visited
                tentative_distance = current_distance + weight
                if tentative_distance < distances[neighbor]:
                    # if we see our current node provides a nicer path to the node under examination than any we've found,
                    # note that down
                    distances[neighbor] = tentative_distance
                    heappush(pq, (tentative_distance, neighbor))


        predecessors = {node: None for node in self.graph}  # a none for each node

        for node, distance in distances.items():
            for neighbor, weight in self.graph[node].items():
                if distances[neighbor] == distance + weight:
                    predecessors[neighbor] = node

        return distances, predecessors

    def shortest_path(self, source: str, target: str):
        _, predecessors = self.shortest_distances(source) # just grab the predecessors,
        # specifically the dictionary telling which node has what as its predecessor

        path = []
        current_node = target

        # just backtrack
        while current_node:
            path.append(current_node)
            current_node = predecessors[current_node]

        path.reverse()

        return path


G = Graph(graph=example_graph)

print(G.shortest_path("A", "G"))

# distances = G.shortest_distances("B")
# print(distances, "\n")
#
# to_F = distances["F"]
# print(f"The shortest distance from B to F is {to_F}")
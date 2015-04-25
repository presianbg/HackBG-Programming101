from walkdfs import WalkDFS


class DirectedGraph:

    def __init__(self):
        self.graph = {}

    def _add_node(self, node):
        self.graph[node] = set()

    def _is_node_in_graph(self, node):
        if node in self.graph:
            return True
        return False

    def add_edge(self, node_a, node_b):
        if not self._is_node_in_graph(node_a):
            self._add_node(node_a)
        if not self._is_node_in_graph(node_b):
            self._add_node(node_b)
        if node_b not in self.graph[node_a]:
            self.graph[node_a].add(node_b)

    def get_neighbors_for(self, node):
        return self.graph[node]

    def path_between(self, node_a, node_b):
        return WalkDFS.are_connected(node_a, node_b, self.graph)

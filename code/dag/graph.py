from graph.vertex import Vertex

class Graph():
    def __init__(self):
        self.vertices = {}
        self.count_vertices = 0

    def __iter__(self):
        return iter(self.vertices.values())

    def add_vertex(self, node, value):
        self.count_vertices += 1
        new_vertex = Vertex(node, value)
        self.vertices[node] = new_vertex
        return new_vertex

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vertices:
            self.add_vertex(frm)
        if to not in self.vertices:
            self.add_vertex(to)

        self.vertices[frm].add_neighbour(self.vertices[to], cost)
        self.vertices[to].add_neighbour(self.vertices[frm], cost)

    def get_vertices(self):
        return self.vertices.keys()

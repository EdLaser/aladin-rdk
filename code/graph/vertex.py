class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' ajdacent: ' + str([x.id for x in self.adjacent])

    def add_neighbour(self, neighbour, weight=0):
        self.adjacent[neighbour] = weight

    def get_connected(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

class Vertex:
    def __init__(self, node, value):
        self.id = node
        self.value = value
        self.adjacent = {}
        self.next = {}
        self.previous = {}

    def __str__(self):
        return str(self.id) + ' next: ' + str([x.id for x in self.next]) \
            + " previous: "  + str([x.id for x in self.previous])

    def add_neighbour(self, neighbour, weight=0):
        self.adjacent[neighbour] = weight

    def add_next(self, next, weight=0):
        self.next[next] = weight

    def add_previous(self, previous, weight=0):
        self.previous[previous] = weight

    def get_connected(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_value(self):
        return self.value
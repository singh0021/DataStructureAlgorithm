class graph:

    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def print_graph(self):
        for vertex in self.adj_list.keys():
            print(vertex, ':', self.adj_list[vertex])

    def add_vertices(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
        return False

g = graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertices('A', 'B')
g.print_graph()


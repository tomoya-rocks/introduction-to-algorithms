import enum


class Color(enum.Enum):

    WHITE = 'white'
    GRAY = 'gray'
    BLACK = 'black_'


class Vertex:

    def __init__(self, name):
        self.name = name
        self.predecessor = None
        self.distance = 0
        self.color = Color.WHITE


class Edge:

    def __init__(self, start, end):
        self.start = start
        self.end = end


class Graph:

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.adjacency_list = {}
        self.__init_graph()

    def print_graph(self):
        for u, adjacencies in self.adjacency_list.items():
            print(u, end=' : ')
            for i, v in enumerate(adjacencies):
                print(v, end=' -> ' if i < len(adjacencies) - 1 else '')
            print('')

    def __init_graph(self):
        for edge in self.edges:
            if not self.adjacency_list.get(edge.start):
                self.adjacency_list[edge.start] = []
            self.adjacency_list[edge.start].append(edge.end)

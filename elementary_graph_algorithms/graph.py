import enum


class Color(enum.Enum):

    WHITE = 'white'
    GRAY = 'gray'
    BLACK = 'black'


class Vertex:

    def __init__(self, name, color=Color.WHITE):
        self.name = name
        self.distance = 0
        self.predecessor = None
        self.color = color


class Edge:

    def __init__(self, start, end):
        self.start = start
        self.end = end


class Graph:

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.adjacency_list = {}

        self.__initialize_graph()

    def print_graph(self):
        for vertex in self.vertices.values():
            print(f"{vertex.name}({vertex.distance}) : ", end='')

            for i, adjacency in enumerate(self.adjacency_list[vertex.name]):
                print(
                    f"{adjacency}", end=' -> ' if i < len(self.adjacency_list[vertex.name]) - 1 else '\n')

    def __initialize_graph(self):
        for vertex in self.vertices.values():
            self.adjacency_list[vertex.name] = []

        for edge in self.edges:
            self.adjacency_list[edge.start].append(edge.end)

import enum
import sys


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
        self.discovered_time = self.finished_time = 0

    def __lt__(self, other):
        return self.distance < other.distance


class Edge:

    def __init__(self, start, end, weight=1):
        self.start = start
        self.end = end
        self.weight = weight


class Graph:

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.adjacency_list = {}

        self.__initialize_graph()

    def print_graph(self):
        for vertex in self.vertices.values():
            print(f"{vertex.name} : ", end='')

            for i, adjacency in enumerate(self.adjacency_list[vertex.name]):
                print(
                    f"{adjacency.end}({adjacency.weight})", end=' -> ' if i < len(self.adjacency_list[vertex.name]) - 1 else '\n')

    def __initialize_graph(self):
        for vertex in self.vertices.values():
            self.adjacency_list[vertex.name] = []

        for edge in self.edges:
            self.adjacency_list[edge.start].append(edge)


def initialize_single_source(graph, s):
    vertices = graph.vertices
    for v in vertices.values():
        v.distance = sys.maxsize
        v.predecessor = None

    s.distance = 0


def relax(u, v, weight):
    if v.distance > u.distance + weight:
        print(f"Relax: u = {u.name}, v = {v.name}, before = {
              v.distance}, after = {u.distance + weight}")

        v.distance = u.distance + weight
        v.predecessor = u

import heapq
import sys

from graph import Edge
from graph import Graph
from graph import Vertex


def prim(graph, a):

    def exists(vertices_list, name):
        for v in vertices_list:
            if v.name == name:
                return True

        return False

    vertices = graph.vertices
    edges = graph.edges
    adjacency_list = graph.adjacency_list

    for u in vertices.values():
        u.distance = sys.maxsize
        u.predecessor = None

    a.distance = 0
    vertices_list = sorted(vertices.values(), key=lambda u: u.distance)
    heapq.heapify(vertices_list)

    results = []
    while len(vertices_list):
        u = heapq.heappop(vertices_list)
        print(f"target vertex: {u.name}")

        adjacency = adjacency_list[u.name]
        for edge in adjacency:
            v = vertices[edge.end]
            if exists(vertices_list, edge.end) and edge.weight < v.distance:
                print(f"{v.name} update weight. {v.distance} -> {edge.weight}")

                results.append(edge)

                v.predecessor = u
                v.distance = edge.weight

                heapq.heapify(vertices_list)

    return results


if __name__ == '__main__':
    vertices = {}
    vertices['a'] = Vertex('a')
    vertices['b'] = Vertex('b')
    vertices['c'] = Vertex('c')
    vertices['d'] = Vertex('d')
    vertices['e'] = Vertex('e')
    vertices['f'] = Vertex('f')
    vertices['g'] = Vertex('g')
    vertices['h'] = Vertex('h')
    vertices['i'] = Vertex('i')

    edges = []
    edges.append(Edge('a', 'b', 4))
    edges.append(Edge('a', 'h', 8))
    edges.append(Edge('b', 'a', 4))
    edges.append(Edge('b', 'c', 8))
    edges.append(Edge('b', 'h', 11))
    edges.append(Edge('c', 'b', 8))
    edges.append(Edge('c', 'd', 7))
    edges.append(Edge('c', 'f', 4))
    edges.append(Edge('c', 'i', 2))
    edges.append(Edge('d', 'c', 7))
    edges.append(Edge('d', 'e', 9))
    edges.append(Edge('d', 'f', 14))
    edges.append(Edge('e', 'd', 9))
    edges.append(Edge('e', 'f', 10))
    edges.append(Edge('f', 'c', 4))
    edges.append(Edge('f', 'd', 14))
    edges.append(Edge('f', 'e', 10))
    edges.append(Edge('f', 'g', 2))
    edges.append(Edge('g', 'f', 2))
    edges.append(Edge('g', 'h', 1))
    edges.append(Edge('g', 'i', 6))
    edges.append(Edge('h', 'a', 8))
    edges.append(Edge('h', 'b', 11))
    edges.append(Edge('h', 'g', 1))
    edges.append(Edge('h', 'i', 7))
    edges.append(Edge('i', 'c', 2))
    edges.append(Edge('i', 'g', 6))
    edges.append(Edge('i', 'h', 7))

    graph = Graph(vertices, edges)

    print("--- graph ---")
    graph.print_graph()

    print("--- Prim's algorith ---")
    results = prim(graph, vertices['a'])

    print("--- result ---")
    total = 0
    for v in vertices.values():
        print(f"name = {v.name}, predecessor = {
              v.predecessor.name if v.predecessor else 'None'}, weight = {v.distance}")
        total += v.distance
    print(f"total weight = {total}")

from graph import Color
from graph import Edge
from graph import Graph
from graph import Vertex

import sys


def breadth_first_search(graph, root):
    vertices = graph.vertices
    edges = graph.edges
    adjacency_list = graph.adjacency_list

    for vertex in vertices.values():
        vertex.color = Color.WHITE
        vertex.distance = sys.maxsize
        vertex.predecessor = None

    vertices[root].color = Color.GRAY
    vertices[root].distance = 0

    q = []
    q.append(vertices[root])
    print(f"{vertices[root].name} color update gray.")

    while q:
        u = q.pop(0)
        adjacencies = adjacency_list[u.name]
        for name in adjacencies:
            v = vertices[name]
            if v.color == Color.WHITE:
                v.color = Color.GRAY
                print(f"{v.name} color update gray.")
                v.distance = u.distance + 1
                print(f"{v.name}'s distance = {v.distance}")
                v.predecessor = u

                q.append(v)

        u.color = Color.BLACK
        print(f"{u.name} color update black.")


def print_breath_first_search(s, v, v_name):
    if v == s:
        print(s.name, end=' -> ' if v.name != v_name else '')
    elif not v.predecessor:
        return
    else:
        print_breath_first_search(s, v.predecessor, v_name)
        print(v.name, end=' -> ' if v.name != v_name else '')


if __name__ == '__main__':
    vertices = {}
    for u in ['s', 'r', 'v', 'w', 't', 'x', 'u', 'y']:
        vertices[u] = Vertex(u)
    edges = []
    edges.append(Edge('s', 'r'))
    edges.append(Edge('s', 'w'))
    edges.append(Edge('r', 's'))
    edges.append(Edge('r', 'v'))
    edges.append(Edge('v', 'r'))
    edges.append(Edge('w', 's'))
    edges.append(Edge('w', 't'))
    edges.append(Edge('w', 'x'))
    edges.append(Edge('t', 'w'))
    edges.append(Edge('t', 'x'))
    edges.append(Edge('t', 'u'))
    edges.append(Edge('x', 'w'))
    edges.append(Edge('x', 't'))
    edges.append(Edge('x', 'u'))
    edges.append(Edge('x', 'y'))
    edges.append(Edge('u', 't'))
    edges.append(Edge('u', 'x'))
    edges.append(Edge('u', 'y'))
    edges.append(Edge('y', 'x'))
    edges.append(Edge('y', 'u'))

    graph = Graph(vertices, edges)
    print("--- Graph ---")
    graph.print_graph()

    print("--- breath first search ---")
    breadth_first_search(graph, 's')

    print("--- result ---")
    for v in vertices.values():
        print(f"{v.name} ({v.distance}) : ", end='')
        print_breath_first_search(vertices['s'], v, v.name)
        print('')

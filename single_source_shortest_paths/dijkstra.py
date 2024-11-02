from graph import Edge
from graph import Graph
from graph import Vertex
from graph import initialize_single_source
from graph import relax

import heapq


def dijkstra(graph, s):
    initialize_single_source(graph, s)

    vertices = graph.vertices
    vertices_list = list(vertices.values())

    heapq.heapify(vertices_list)

    while len(vertices_list) != 0:
        u = heapq.heappop(vertices_list)
        print(f"target vertex = {u.name}")

        adjacency_list = graph.adjacency_list[u.name]
        for adjacency in adjacency_list:
            v = vertices[adjacency.end]
            weight = adjacency.weight

            relax(u, v, weight)

            heapq.heapify(vertices_list)


def print_path(graph, s, v, name):
    if v == s:
        print(s.name, end=' -> ')
    elif not v.predecessor:
        return
    else:
        print_path(graph, s, v.predecessor, name)
        print(v.name, end=' -> ' if v.name != name else '')


if __name__ == '__main__':
    vertices = {}
    vertices['s'] = Vertex('s')
    vertices['t'] = Vertex('t')
    vertices['y'] = Vertex('y')
    vertices['x'] = Vertex('x')
    vertices['z'] = Vertex('z')

    edges = []
    edges.append(Edge('s', 't', 10))
    edges.append(Edge('s', 'y', 5))
    edges.append(Edge('t', 'y', 2))
    edges.append(Edge('t', 'x', 1))
    edges.append(Edge('y', 't', 3))
    edges.append(Edge('y', 'x', 9))
    edges.append(Edge('y', 'z', 2))
    edges.append(Edge('x', 'z', 4))
    edges.append(Edge('z', 's', 7))
    edges.append(Edge('z', 'x', 6))

    graph = Graph(vertices, edges)

    print("--- graph ---")
    graph.print_graph()

    print("--- Dijstra's algorithn ---")
    dijkstra(graph, vertices['s'])

    print("--- result ---")
    for v in vertices.values():
        print(f"name = {v.name}, distance = {v.distance} : ", end='')
        if v.name != 's':
            print_path(graph, vertices['s'], v, v.name)
        print('')

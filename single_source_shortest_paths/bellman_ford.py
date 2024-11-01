from graph import Edge
from graph import Graph
from graph import Vertex
from graph import initialize_single_source
from graph import relax


def bellman_ford(graph, s):
    initialize_single_source(graph, s)

    vertices = graph.vertices
    edges = graph.edges

    print("--- before ---")
    for v in vertices.values():
        print(f"name = {v.name}, distance = {v.distance}")

    for i in range(len(vertices) - 1):
        for edge in edges:
            u = vertices[edge.start]
            v = vertices[edge.end]
            weight = edge.weight

            relax(u, v, weight)

    print("--- after ---")
    for v in vertices.values():
        print(f"name = {v.name}, distance = {v.distance}")

    for edge in edges:
        u = vertices[edge.start]
        v = vertices[edge.end]
        weight = edge.weight

        if v.distance > u.distance + weight:
            return False

    return True


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
    edges.append(Edge('s', 't', 6))
    edges.append(Edge('s', 'y', 7))
    edges.append(Edge('t', 'y', 8))
    edges.append(Edge('t', 'x', 5))
    edges.append(Edge('t', 'z', -4))
    edges.append(Edge('y', 'x', -3))
    edges.append(Edge('y', 'z', 9))
    edges.append(Edge('x', 't', -2))
    edges.append(Edge('z', 's', 2))
    edges.append(Edge('z', 'x', 7))

    graph = Graph(vertices, edges)

    print("--- graph ---")
    graph.print_graph()

    print("--- Bellman-Ford algorithm ---")
    has_cycle = bellman_ford(graph, vertices['s'])

    print("--- result ---")
    if not has_cycle:
        print("Graph has a cycle.")
    else:
        for v in vertices.values():
            print(f"name = {v.name}, distance = {v.distance} : ", end='')
            if v.name != 's':
                print_path(graph, vertices['s'], v, v.name)
            print('')

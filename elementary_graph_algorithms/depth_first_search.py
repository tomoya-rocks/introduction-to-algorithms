from graph import Color
from graph import Edge
from graph import Graph
from graph import Vertex



time = 0


def depth_first_search(graph):
    vertices = graph.vertices
    for u in vertices.values():
        u.color = Color.WHITE
        u.predecessor = None

    for u in vertices.values():
        if u.color == Color.WHITE:
            depth_first_search_internal(graph, u)


def depth_first_search_internal(graph, u):
    vertices = graph.vertices
    global time

    time += 1
    u.start = time
    u.color = Color.GRAY
    print(f"{u.name} color change to gray. start = {u.start}")

    adjacencies = graph.adjacency_list[u.name]
    for v_name in adjacencies:
        v = vertices[v_name]
        if v.color == Color.WHITE:
            v.predecessor = u
            depth_first_search_internal(graph, v)

    u.color = Color.BLACK
    time += 1
    u.finish = time
    print(f"{u.name} color change to black. finish = {u.finish}")


def calculate_path(u):
    result = []
    result.append(u.name)

    while u.predecessor:
        u = u.predecessor
        result.append(u.name)

    result.sort()

    return result


if __name__ == '__main__':
    vertices = {}
    for v in ['u', 'v', 'x', 'y', 'w', 'z']:
        vertices[v] = Vertex(v)

    edges = []
    edges.append(Edge('u', 'v'))
    edges.append(Edge('u', 'x'))
    edges.append(Edge('v', 'y'))
    edges.append(Edge('x', 'v'))
    edges.append(Edge('y', 'x'))
    edges.append(Edge('w', 'y'))
    edges.append(Edge('w', 'z'))
    edges.append(Edge('z', 'z'))

    graph = Graph(vertices, edges)
    print("--- graph ---")
    graph.print_graph()

    print("--- depth first search ---")
    depth_first_search(graph)

    print("--- result ---")
    for u in vertices.values():
        print(f"{u.name} ({u.start} / {u.finish}) ", end=': ')
        path = calculate_path(u)
        for i, u in enumerate(path):
            print(u, end=' -> ' if i < len(path) - 1 else '')

        print('')

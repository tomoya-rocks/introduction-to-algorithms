from graph import Color
from graph import Edge
from graph import Graph
from graph import Vertex


time = 0


def depth_first_search(graph):
    vertices = graph.vertices

    for u in vertices.values():
        if u.color == Color.WHITE:
            depth_first_search_internal(graph, u)


def depth_first_search_internal(graph, u):
    global time

    time += 1
    u.discovered_time = time
    u.color = Color.GRAY
    print(f"{u.name} is discovered. time = {time}")

    vertices = graph.vertices
    adjacencies = graph.adjacency_list[u.name]
    for adjacency in adjacencies:
        v = vertices[adjacency]

        if v.color == Color.WHITE:
            v.color = Color.GRAY
            v.predecessor = u

            depth_first_search_internal(graph, v)

    u.color = Color.BLACK
    time += 1
    u.finished_time = time
    print(f"{u.name} is finished. time = {time}")


def print_path(graph, v, name):
    if not v.predecessor:
        print(v.name, end=' -> ' if v.name != name else '')

        return
    else:
        print_path(graph, v.predecessor, name)
        print(v.name, end=' -> ' if v.name != name else '')


if __name__ == '__main__':
    vertices = {}
    vertices['u'] = Vertex('u')
    vertices['v'] = Vertex('v')
    vertices['x'] = Vertex('x')
    vertices['y'] = Vertex('y')
    vertices['w'] = Vertex('w')
    vertices['z'] = Vertex('z')

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
    for v in vertices.values():
        print(f"{v.name} ({v.discovered_time} / {v.finished_time}): ", end='')
        print_path(graph, v, v.name)
        print('')

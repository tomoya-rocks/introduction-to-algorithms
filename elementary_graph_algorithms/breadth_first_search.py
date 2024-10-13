from queue import Queue
from graph import Color
from graph import Edge
from graph import Graph
from graph import Vertex


def breadth_first_search(graph, s):
    vertices = graph.vertices
    edges = graph.edges
    adjacency_list = graph.adjacency_list

    print(f"{s.name} is dicovered.")
    s.color = Color.BLACK

    q = []
    q.append(s)
    while len(q) != 0:
        u = q.pop(0)
        for adjacency in adjacency_list[u.name]:
            v = vertices[adjacency]
            if v.color == Color.WHITE:
                print(f"{v.name} is discovered.")
                v.color = Color.GRAY
                v.distance = u.distance + 1
                v.predecessor = u

                q.append(v)

        print(f"{u.name} is finished.")
        u.color = Color.BLACK


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
    vertices['r'] = Vertex('r')
    vertices['v'] = Vertex('v')
    vertices['w'] = Vertex('w')
    vertices['t'] = Vertex('t')
    vertices['x'] = Vertex('x')
    vertices['u'] = Vertex('u')
    vertices['y'] = Vertex('y')

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

    print("--- graph ---")
    graph.print_graph()

    print("--- breadth first search ---")
    breadth_first_search(graph, vertices['s'])

    print("--- result ---")
    for v in vertices.values():
        print(f"{v.name} ({v.distance}): ", end='')
        print_path(graph, vertices['s'], v, v.name)
        print('')

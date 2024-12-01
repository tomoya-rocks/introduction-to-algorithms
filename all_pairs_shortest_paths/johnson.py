from graph import Edge
from graph import Graph
from graph import Vertex
from graph import bellman_ford
from graph import dijkstra


def johnson(graph):
    vertices = graph.vertices
    edges = graph.edges

    extended_vertices = vertices.copy()
    extended_vertices['0'] = Vertex('0')
    extended_edges = edges.copy()
    extended_edges.append(Edge('0', '0', 0))
    extended_edges.append(Edge('0', '1', 0))
    extended_edges.append(Edge('0', '2', 0))
    extended_edges.append(Edge('0', '3', 0))
    extended_edges.append(Edge('0', '4', 0))
    extended_edges.append(Edge('0', '5', 0))
    extended_graph = Graph(extended_vertices, extended_edges)

    print("--- Extended graph ---")
    extended_graph.print_graph()
    input()

    print("--- Bellman-Ford algorithm ---")
    if not bellman_ford(extended_graph, extended_vertices['0']):
        print("Graph has a cycle.")

        return
    else:
        input()
        h = {}
        for v in extended_vertices.values():
            h[v.name] = v.distance

        print("--- h ---")
        for name, distance in h.items():
            print(f"{name}: {distance}")
        input()

        print("--- Update weight ---")
        for extended_edge in extended_edges:
            u = extended_edge.start
            v = extended_edge.end
            edge = find_edge(edges, u, v)
            if edge:
                extended_edge.weight = edge.weight + h[u] - h[v]
                edge.weight = extended_edge.weight
            else:
                extended_edge.weight = h[u] - h[v]

        extended_graph.print_graph()
        input()

        print("--- Dijkstra's algorithm ---")
        delta_hat = [[-1 for _ in range(len(vertices) + 1)]
                     for _ in range(len(vertices) + 1)]
        for u in vertices.values():
            dijkstra(graph, u)
            for v in vertices.values():
                delta_hat[int(u.name)][int(v.name)] = v.distance
        for u in vertices.values():
            print(f"{u.name}: {u.distance}")
        input()

        D = [[0 for _ in range(len(vertices) + 1)]
             for _ in range(len(vertices) + 1)]
        for u in vertices.values():
            for v in vertices.values():
                D[int(u.name)][int(v.name)] = delta_hat[int(
                    u.name)][int(v.name)] + h[v.name] - h[u.name]

        return D


def find_edge(edges, start, end):
    for edge in edges:
        if edge.start == start and edge.end == end:
            return edge

    return None


if __name__ == '__main__':
    vertices = {}
    vertices['1'] = Vertex('1')
    vertices['2'] = Vertex('2')
    vertices['3'] = Vertex('3')
    vertices['4'] = Vertex('4')
    vertices['5'] = Vertex('5')

    edges = []
    edges.append(Edge('1', '2', weight=3))
    edges.append(Edge('1', '3', weight=8))
    edges.append(Edge('1', '5', weight=-4))
    edges.append(Edge('2', '4', weight=1))
    edges.append(Edge('2', '5', weight=7))
    edges.append(Edge('3', '2', weight=4))
    edges.append(Edge('4', '1', weight=2))
    edges.append(Edge('4', '3', weight=-5))
    edges.append(Edge('5', '4', weight=6))

    graph = Graph(vertices, edges)

    print("--- graph ---")
    graph.print_graph()

    print("--- Johnson's algorithm ---")
    D = johnson(graph)

    if D:
        print("--- result ---")
        for i in range(1, len(D)):
            for j in range(1, len(D)):
                print(f"{D[i][j]:>4}", end='')

            print('')

from disjoint_sets_with_linked_list import DisjointSet
from graph import Edge
from graph import Graph
from graph import Vertex


def kruskal(graph):
    vertices = graph.vertices
    edges = graph.edges
    adjacency_list = graph.adjacency_list

    vertex_names = [vertex.name for vertex in vertices.values()]
    disjoint_set = DisjointSet(vertex_names)

    sorted_edges = sorted(edges, key=lambda e: e.weight)

    results = []
    for edge in sorted_edges:
        u = edge.start
        v = edge.end
        weight = edge.weight

        print(f"u = {u}, v = {v}, weight = {weight}")

        if disjoint_set.find_set(u) != disjoint_set.find_set(v):
            print(f"Edge ({u}, {v}) append to spanning tree.")

            results.append((u, v, weight))
            disjoint_set.union(u, v)
        else:
            print(f"Edge ({u}, {v}) is ignored.")

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

    print("--- Kruslal's algorith ---")
    results = kruskal(graph)

    print("--- result ---")
    total_weight = 0
    for start, end, weight in results:
        print(f"Edge {start, end} weight = {weight}")

        total_weight += weight
    print(f"Total weight = {total_weight}")

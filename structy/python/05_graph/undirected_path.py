"""
Write a function, undirected_path, that takes in a list of edges for an
undirected graph and two nodes (node_A, node_B). The function should return a
boolean indicating whether or not there exists a path between node_A and
node_B.
"""


def undirected_path(edges, node_A, node_B):
    graph = build_graph(edges)
    return has_path(graph, node_A, node_B, set())


def build_graph(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph


def has_path(graph, source, destination, visited):
    if source == destination:
        return True

    if source in visited:
        return False

    visited.add(source)
    for neighbor in graph[source]:
        if has_path(graph, neighbor, destination, visited):
            return True
    return False


if __name__ == "__main__":
    edges = [("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")]
    print(undirected_path(edges, "j", "m"))  # -> True

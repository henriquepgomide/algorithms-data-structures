"""
Write a function, has_path, that takes in a dictionary representing the
adjacency list of a directed acyclic graph and two nodes (src, dst).
The function should return a boolean indicating whether or not there exists a
directed path between the source and destination nodes.
"""


def has_path(graph, source, destination):
    if source == destination:
        return True

    for neighbor in graph[source]:
        if has_path(graph, neighbor, destination):
            return True
    return False


if __name__ == "__main__":

    graph = {
      "f": ["g", "i"],
      "g": ["h"],
      "h": [],
      "i": ["g", "k"],
      "j": ["i"],
      "k": []
    }

    print(has_path(graph, "f", "k"))  # True

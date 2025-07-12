def hasPath(graph, source, destination):
    if source == destination:
        return True
    for neighbor in graph[source]:
        if hasPath(graph, neighbor, destination):
            return True
    return False

if __name__ == "__main__":
    graph = {
        "a": ["b", "c"],
        "b": ["d"],
        "c": ["e"],
        "d": [],
        "e": []
    }
    print(hasPath(graph, "a", "e"))
    print(hasPath(graph, "b", "e"))
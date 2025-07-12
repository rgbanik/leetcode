def hasPath(graph, source, destination):
    # Initialize stack with source because DFS uses stack
    stack = [source]

    while stack: # Keep going as long as the stack holds something
        current = stack.pop()
        print(current)
        if current == destination:
            return True
        for neighbor in graph[current]:
            stack.append(neighbor)
    return False

if __name__ == "__main__":
    graph = {
        "a": ["b", "c"],
        "b": ["d"],
        "c": ["e"],
        "d": [],
        "e": []
    }
    print(f"Source: a, Destination: e, Output: {hasPath(graph, "a", "d")}")
    print(f"Source: d, Destination: e, Output: {hasPath(graph, "d", "e")}")
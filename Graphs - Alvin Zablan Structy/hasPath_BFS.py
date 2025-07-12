def hasPath(graph, source, destination):
    # Initialize a queue with source, becasue BFS uses queue
    queue = [source]
    
    while queue:
        current = queue.pop(0) # Or maybe use insert(0, element)?
        print(current)
        if current == destination:
            return True
        for neighbor in graph[current]:
            queue.append(neighbor)
    return False

if __name__ == "__main__":
    graph = {
        "a": ["b", "c"],
        "b": ["d"],
        "c": ["e"],
        "d": [],
        "e": []
    }
    print(f"Source: a, Destination: e, Output: {hasPath(graph, "a", "e")}")
    print(f"Source: d, Destination: e, Output: {hasPath(graph, "d", "e")}")
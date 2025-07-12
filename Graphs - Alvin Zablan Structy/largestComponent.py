def largestComponent(graph):
    largest = 0
    visited = set()

    for key in graph.keys():
        if key in visited:
            continue
        queue = [key]
        size = 0
        while queue:
            print(queue)
            current = queue.pop(0)
            visited.add(current)
            size += 1
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor) # Standard practice to mark a neighbor as visited when adding to queue.
                    queue.append(neighbor)
        largest = max(largest, size)
    return largest


if __name__ == "__main__":
    graph = {
        0: [1, 5, 8],
        1: [0],
        2: [3, 4],
        3: [2, 4],
        4: [2, 3],
        5: [0, 8],
        8: [0, 5]
    }
    print(largestComponent(graph))
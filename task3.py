from min_heap import MinHeap


def dijkstra(graph, start):
    """Shortest paths from `start` to all vertices using a binary min-heap.

    `graph` is an adjacency dict {vertex: {neighbor: weight}}.
    Returns (distances, previous) where `previous` allows path restoration.
    """
    for edges in graph.values():
        for weight in edges.values():
            if weight < 0:
                raise ValueError("Dijkstra does not support negative weights")
    if start not in graph:
        raise ValueError(f"Unknown start vertex: {start}")

    distances = {vertex: float("inf") for vertex in graph}
    previous = {vertex: None for vertex in graph}
    distances[start] = 0

    heap = MinHeap()
    heap.push((0, start))

    while len(heap):
        dist, vertex = heap.pop()
        if dist > distances[vertex]:
            continue  # Outdated heap entry

        for neighbor, weight in graph[vertex].items():
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                previous[neighbor] = vertex
                heap.push((new_dist, neighbor))

    return distances, previous


def restore_path(previous, target):
    path = []
    while target is not None:
        path.append(target)
        target = previous[target]
    return path[::-1]


def main():
    graph = {
        "A": {"B": 5, "C": 10},
        "B": {"A": 5, "D": 3},
        "C": {"A": 10, "D": 2},
        "D": {"B": 3, "C": 2, "E": 4},
        "E": {"D": 4},
        "F": {},  # Unreachable vertex
    }
    start = "A"
    distances, previous = dijkstra(graph, start)

    print(f"Найкоротші шляхи від вершини {start}:")
    for vertex, dist in distances.items():
        if dist == float("inf"):
            print(f"  {vertex}: недосяжна")
        else:
            print(f"  {vertex}: {dist}  шлях: {' -> '.join(restore_path(previous, vertex))}")


if __name__ == "__main__":
    main()

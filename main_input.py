def remove_unnecessary_vertices(graph):
    degree_two_vertices = [v for (v, neighbors) in graph.items()
                           if len(neighbors) == 2]
    for vertex in degree_two_vertices:
        if vertex in graph:
            neighbors = graph[vertex]
            graph.pop(vertex)
            if neighbors[0] != neighbors[1]:
                graph[neighbors[0]].remove(vertex)
                graph[neighbors[1]].remove(vertex)
                graph[neighbors[0]].append(neighbors[1])
                graph[neighbors[1]].append(neighbors[0])

    return graph


n = int(input())

graph = {}

for _ in range(n):
    vals = list(map(int, input().split()))
    graph[vals[0]] = vals[1:]

result = remove_unnecessary_vertices(graph)
print(result)

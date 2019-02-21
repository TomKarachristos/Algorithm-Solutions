def add_edge(graph, v, w):
    if v in graph:
        graph[v].append(w)
    else:
        graph[v] = [w]
    if w in graph:
        graph[w].append(v)
    else:
        graph[w] = [v]


from collections import deque

def is_bipartite(graph, n, start_node):
    visited = set()
    colour = [-1] * n
    colour[start_node] = 1
    q = deque()
    q.append(start_node)
    while q:
        current = q.popleft()
        for dest in graph[current]:
            if ((dest, current) in visited):
                continue
            if colour[dest] == -1:
                visited.add((current, dest))
                colour[dest] = 1 - colour[current]
                q.append(dest)
            else:
                if colour[dest] == colour[current]:
                    return False
    return True


while True:
    nodes = int(input())
    if (nodes == 0): break
    edges = int(input())
    graph = {}
    v, w = 0, 0
    for i in range(edges):
        v, w = input().rstrip().split()
        v, w = int(v), int(w)
        add_edge(graph, v, w)
    if (is_bipartite(graph, nodes, v)):
        print("BICOLORABLE.")
    else:
        print("NOT BICOLORABLE.")
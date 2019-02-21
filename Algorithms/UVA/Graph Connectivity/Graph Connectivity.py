import sys

def get_number(char):
    return ord(char) - 64

def add_edge(graph,v,w):   
    if v in graph:                   
        graph[v].append(w)  
    else:   
        graph[v] = [w] 
    if w in graph:               
        graph[w].append(v)  
    else:   
        graph[w] = [v] 
    

visited = []
def explore(graph, start_node):
    global visited
    visited[start_node] = True
    if start_node in graph:
        for value in graph[start_node]:
            if visited[value] == False:
                explore(graph,value)


def dfs(graph,n):
    global visited
    visited = [False] * n
    subgraphs = 0
    for index in range(n):
        if not visited[index]:
            subgraphs = subgraphs + 1
            explore(graph, index)
    print(str(subgraphs) )

cases = int(sys.stdin.readline().rstrip())
blank_line =  sys.stdin.readline()
for index in range(cases):
    graph = {}
    line =  sys.stdin.readline().rstrip()
    n = get_number(line)
    line = sys.stdin.readline().rstrip()
    while line != '':
        add_edge(graph, get_number(line[0])-1, get_number(line[1])-1 )
        line = sys.stdin.readline().rstrip()
    dfs(graph,n)
    if(index != cases-1):
        print()
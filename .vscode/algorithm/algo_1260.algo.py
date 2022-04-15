import sys
from collections import deque

def dfs(graph, v, isvisited):
    isvisited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not isvisited[i]:
            dfs(graph, i, isvisited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v=queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N,M,V = map(int, input().split())
graph =[[] for _ in range(N+1)]
isvisited = [False] * (N+1)
for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, N+1):
    graph[i].sort()

dfs(graph, V, isvisited)
print()
isvisited = [False] * (N+1)
bfs(graph,V,isvisited)



import sys
sys.setrecursionlimit(10 ** 6)
def dfs(isvisited, graph, x, y,n,m):
    global cnt
    isvisited[x][y] = True
    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,1,1,1,0,-1,-1,-1]
    for i in range(8):
        a = x+dx[i]
        b = y+dy[i]
        if 0<=a<m and 0<=b<n and isvisited[a][b] == False and graph[a][b] == 1:
            dfs(isvisited, graph, a,b,n,m)

flag = True
while flag:
    cnt = 0
    n,m = map(int, input().split())
    if n==0 and m==0:
        flag=False
    if flag:
        isvisited = [[False]*n for _ in range(m)]
        graph = [list(map(int, input().split())) for _ in range(m)]


        for a in range(m):
            for b in range(n):
                if graph[a][b] == 1 and isvisited[a][b] == False:                
                        dfs(isvisited, graph, a, b,n, m)
                        cnt+=1
        dfs(isvisited, graph, 0,0,n,m)
        print(cnt)

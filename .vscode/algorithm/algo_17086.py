import sys
from collections import deque

data = []
N,M = map(int, input().split())
for i in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))

q=deque()

dx=[1,1,-1,-1,1,0,-1,0]
dy=[1,-1,-1,1,0,-1,0,1]

def bfs():
    while q:
        x,y = q.popleft()
        for k in range(8):
            nx = dx[k]+x
            ny = dy[k]+y
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if not data[nx][ny]: 
                q.append([nx,ny])
                data[nx][ny] = data[x][y] + 1

for i in range(N):
    for j in range(M):
        if data[i][j] == 1:
            q.append([i,j])
bfs()
print(max(map(max,data))-1)
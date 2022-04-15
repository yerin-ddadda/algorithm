from collections import deque
import queue
m,n,h = map(int, input().split())
tomato = [[list(map(int,input().split())) for i in range(n)] for depth in range(h)] #토마토 상자 입력하고

q=deque()
dx=[0,0,0,0,1,-1] # h
dy=[0,-1,0,1,0,0]
dz=[1,0,-1,0,0,0]

def bfs(q):
    output=-1
    while q:
        size=len(q)
        for s in range(size):
            current=q.popleft()
            i=current[0]
            j=current[1]
            k=current[2]
            for a in range(6):
                nx=i+dx[a] #h
                ny=j+dy[a]
                nz=k+dz[a]
                if 0<=nx<h and 0<=ny<n and 0<=nz<m and tomato[nx][ny][nz]==0:
                    q.append([nx,ny,nz])
                    tomato[nx][ny][nz]=1
        output+=1
    return output

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                q.append([i,j,k])
time=bfs(q)
flag=False
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k]==0:
                flag=True
if flag==True:
    print(-1)
else:
    print(time)
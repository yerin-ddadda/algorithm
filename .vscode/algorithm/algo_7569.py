from collections import deque
import sys
input = sys.stdin.readline
tomato=[]
m,n,h = map(int, input().split())
tomato = [[list(map(int,input().split())) for i in range(n)] for depth in range(h)] #토마토 상자 입력하고

dx = [0,0,0,0,1,-1]
dy = [0,-1,0,1,0,0]
dz = [1,0,-1,0,0,0]
q = []

def bfs(q):
    global output
    output=0
    tmp = []
    while len(q) != 0:
        for current in q:
            i=current[0]
            j=current[1]
            k=current[2]
            for a in range(6):
                nx = dx[a]+i # 층
                ny = dy[a]+j
                nz = dz[a]+k
                if 0<=nz<m and 0<=ny<n and 0<=nx<h and tomato[nx][ny][nz]==0:
                    tomato[nx][ny][nz]=1
                    tmp.append([nx,ny,nz])        
        q=tmp
        tmp=[]
        output+=1
    return output
                  
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                q.append([i,j,k])

time=bfs(q)
flag=False
for i in range(h): # 토마토상자를 하나씩 둘러보며 0을 발견하면 토마토가 익지 않은 것이다
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                flag=True
if flag==True:
    print(-1)
else:
    print(time)


               
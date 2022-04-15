from collections import deque
import queue

dx=[0,1,0,-1]
dy=[1,0,-1,0]

n = int(input())
blind = []
isvisited = []
q = deque()

def bfs(i,j):
    q.append([i,j])

    isvisited[i][j] = True
    while q:
        i,j=q.popleft()
        for z in range(4):
            nx=dx[z]+i
            ny=dy[z]+j
            if n>nx>=0 and n>ny>=0:
                if blind[i][j]==blind[nx][ny] and isvisited[nx][ny]==False:
                    isvisited[nx][ny]=True
                    q.append([nx,ny])


for i in range(n):
    rgb=input()
    blind.append(list(rgb))

isvisited=[[False] * n for _ in range(n)]
not_blind_num = 0
blind_num=0
for i in range(n):
    for j in range(n):
        if isvisited[i][j] == False:
            bfs(i,j)
            not_blind_num+=1
print(not_blind_num,end=" ")

isvisited=[[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if blind[i][j]=="R":
            blind[i][j]="G"


for i in range(n):
    for j in range(n):
        if isvisited[i][j]==False:
            bfs(i,j)
            blind_num+=1
print(blind_num)
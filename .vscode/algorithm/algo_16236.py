from collections import deque, queue

n=int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))



my_loc = []
my_size = 2
time = 0
eaten = 0
q = deque()

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(i,j):
    isvisited = [[0]*n for i in range(n)]
    isvisited[i][j] = 1
    global my_size, eaten
    q=deque()
    q.append([i,j])
    while q:
        i,j = q.popleft()
        # if board[i][j] < my_size:
        #     eaten+=1
        #     if eaten == my_size:
        #         my_size+=1
        for k in range(4):
            x = dx[k] + i
            y = dy[k] + j
            if 0<=x<n and 0<=y<n and isvisited[x][y]==0 and board[x][y] <= my_size:
                q.append([x,y])
                isvisited[x][y]=1
                     

def find_shark():
    for i in range(n):
        for j in range(n):
            if board[i][j]==9:
                q.append([i,j])
                isvisited[i][j] = 1
                bfs(i,j)

find_shark()
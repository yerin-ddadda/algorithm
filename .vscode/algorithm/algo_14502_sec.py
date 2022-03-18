from collections import deque
import copy

n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]


def bfs():    
    q = deque()
    copy_board = copy.deepcopy(board)
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                q.append([i,j])
        
    while q:
        x,y = q.popleft()
        for k in range(4):
            xi = dx[k] + x
            yi = dy[k] + y
            if 0<=xi<n and 0<=yi<m and copy_board[xi][yi] == 0:
                copy_board[xi][yi] = 2
                q.append((xi,yi))
    count_zero(copy_board)
                

def make_wall(idx,count):
    if count==3:
        bfs()
        return
    if n*m<=idx:
        return

    x = idx//m
    y = idx%m
    
    if board[x][y] == 0:
        board[x][y] = 1
        make_wall(idx+1, count+1)
        board[x][y]=0
    # else:
    #     make_wall(idx+1,count)
    make_wall(idx+1,count)

max_num = 0  
def count_zero(copy_board):
    cnt=0
    global max_num
    for i in range(n):
        cnt += copy_board[i].count(0)
    
    max_num = max(max_num, cnt)



make_wall(0,0)

print(max_num)
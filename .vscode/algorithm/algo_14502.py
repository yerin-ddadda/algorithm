# from collections import deque
# import copy

# n,m = map(int, input().split())
# board = []

# board = [list(map(int, input().split())) for _ in range(n)]


# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
# answer = 0

# def bfs():
#     visited = [[0]*m for _ in range(n)]
#     q = deque()
#     copy_board = copy.deepcopy(board)
#     for i in range(n):
#         for j in range(m):
#             if copy_board[i][j] == 2:
#                 q.append([i,j])
    
#     while q:
#         i,j=q.popleft()
#         # print("visited!!!:",visited)
        
#         # print(q)
#         for k in range(4):
#             x = dx[k] + i
#             y = dy[k] + j
#             if 0<=x<n and 0<=y<m and visited[x][y] == 0 and board[x][y] == 0:
#                     q.append([x,y])
#                     visited[x][y] = 1
#                     copy_board[x][y] = 2
                     
#     global answer
#     count= 0

#     for i in range(n):
#         count += copy_board[i].count(0)
        
#     answer = max(answer, count)
#     # print(answer)
#     # print(copy_board)

# def makewall(count):
#     print(board)
#     print("---------")
#     # print("hahahah")
#     if count == 3:
#         bfs()
#         # print("lalala")
#         return

#     for i in range(n):
#         for j in range(m):
#             if board[i][j] == 0:
#                 board[i][j] = 1
#                 makewall(count+1)

#                 board[i][j]=0

# makewall(0)
# print(answer)

from collections import deque
import copy
import sys

def bfs():
    q = deque()
    copy_board = copy.deepcopy(board)
    for i in range(n):
        for j in range(m):
            if copy_board[i][j] == 2:
                q.append((i,j))
    
    while q:
        i,j=q.popleft()
        for k in range(4):
            x = dx[k] + i
            y = dy[k] + j
            if 0<=x<n and 0<=y<m and copy_board[x][y] == 0:
                copy_board[x][y] = 2
                q.append((x,y))

    global answer
    count= 0
    # print(copy_board)
    for i in range(n):
        count += copy_board[i].count(0)
    
    answer = max(answer, count)



# def makewall(count):
    
#     # print("hahahah")
#     if count == 3:
#         bfs()
#         # print("lalala")
#         return

#     for i in range(n):
#         for j in range(m):
#             if board[i][j] == 0:
#                 board[i][j] = 1
#                 makewall(count+1)

#                 board[i][j]=0








def makewall(idx, count):
    if count == 3:
        bfs()
        return
    if idx>=n*m:
        return

    i = idx//m
    j = idx%m
    # print(i,j,"lalalalalalala")
    if board[i][j] == 0:
        board[i][j] = 1
        makewall(idx+1,count+1)
        board[i][j]=0
    makewall(idx+1, count)

n,m = map(int, input().split())
board = []

for i in range(n):
    board.append(list(map(int,sys.stdin.readline().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]
answer = 0
makewall(0,0)
print(answer)

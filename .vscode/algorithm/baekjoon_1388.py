import sys
n,m = map(int,input().split())
board = [list(sys.stdin.readline()) for i in range(n)]
isvisited = [[0]*m for i in range(n)]

def horiz(board,a,b):
    if 0<=a<n and 0<=b+1<m and board[a][b+1]=="-":
        isvisited[a][b+1] = 1
        horiz(board,a,b+1)
    else:
        return 

def length(board,a,b):
    if 0<=a+1<n and 0<=b<m and board[a+1][b]=="|":
        isvisited[a+1][b] = 1
        length(board,a+1,b)
    else:
        return 

cnt=0
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == "-" and isvisited[i][j]==0:
            isvisited[i][j] = 1
            horiz(board,i,j)
            cnt+=1
        else:
            if board[i][j] == "|" and isvisited[i][j]==0:
                isvisited[i][j] = 1 
                length(board,i,j)
                cnt+=1
print(cnt)
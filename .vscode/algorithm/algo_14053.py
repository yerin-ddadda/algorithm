n,m = map(int,input().split())
r,c,d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]
count = 0
def clean(x,y,d):
    global count
    
    if board[x][y] == 0:
        board[x][y] = 2
        count+=1
    
    for k in range(1,5):
        nd = (k+d)%4
        i = dx[(k+d)%4]+x
        j = dy[(k+d)%4]+y
        if 0<=i<n and 0<=j<m and board[i][j] == 0:
            clean(i,j,nd)
            return
    # d=nd
    nd = (nd-2)%4
    nx = x+dx[nd]
    ny = y+dy[nd]
    if board[nx][ny]==1:
        return
    clean(nx,ny,d)

# # board[r][c] = 1
if d==1:
    d=3

elif d==3:
    d=1

clean(r,c,d)
print(count)

n,k = map(int,input().split())
board = [[0]*(n+1) for _ in range(k+1)]
for i in range(n+1):
    board[1][i]=1

for i in range(1,k+1):
    board[i][0]=1

for x in range(2,k+1):
    for y in range(1,n+1):
        for z in range(0,y+1):
            board[x][y]+=board[x-1][z]
print(board[k][n] % 1000000000)
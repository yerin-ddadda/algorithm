from collections import defaultdict

N = int(input())
board = [[0]*N for _ in range(N)]
numbers_dict = defaultdict(list)
print(board)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

for _ in range(N**2):    
    numbers = list(map(int,input().split()))
    numbers_dict[numbers[0]] = numbers[1:]
    max_x = 0
    max_y = 0
    max_like = -1
    max_empty = -1

    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                likecnt = 0
                emptycnt = 0
                for k in range(4):
                    x = dx[k]+i
                    y = dy[k]+j
                    if 0<=x<N and 0<=y<N:
                        if board[x][y] in numbers:
                            likecnt+=1
                        if board[x][y] == 0:
                            emptycnt+=1

                if max_like < likecnt or (max_like == likecnt and max_empty < emptycnt):
                    max_x = i
                    max_y = j                       
                    max_like = likecnt
                    max_empty = emptycnt

    board[max_x][max_y] = numbers[0]
result = 0
for i in range(N):
    for j in range(N):
        count = 0
        number = numbers_dict[board[i][j]]
        for k in range(4):
            x = dx[k]+i
            y = dy[k]+j
            if 0<=x<N and 0<=y<N:

                if board[x][y] in number:
                    cnt+=1
        
        if count != 0:
            result += 10**(count-1)

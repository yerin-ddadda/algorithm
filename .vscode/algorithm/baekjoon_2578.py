
bingo_board = [list(map(int, input().split())) for _ in range(5)]
call_board = [list(map(int, input().split())) for _ in range(5)]

def find_bingo(bingo_board):
    total_cnt = 0
    #가로
    for i in range(5):
        cnt=0
        for j in range(5):
            if bingo_board[i][j] == 0:
                cnt+=1
        if cnt==5:
            total_cnt += 1
    
    #세로
    for i in range(5):
        cnt=0
        for j in range(5):
            if bingo_board[j][i] == 0:
                cnt+=1
        if cnt==5:
            total_cnt += 1

    #대각선
    for i in range(5):
        cnt=0
        if bingo_board[i][i] == 0:
                cnt+=1
        if cnt==5:
            total_cnt += 1
    
    dx=[0,1,2,3,4]
    dy=[4,3,2,1,0]
    for i in range(5):
        if bingo_board[dx[i]][dy[i]] == 0:
            cnt+=1
        if cnt==5:
            total_cnt += 1

    if total_cnt >= 3:
        return total_cnt
    else:
        return 0

cnt = 0
flag=True

while flag:
    for i in range(5):
        for j in range(5):
            call = call_board[i][j]
            if flag==True:
                for a in range(5):
                    for b in range(5):
                        if call == bingo_board[a][b]:
                            bingo_board[a][b] = 0
                            cnt+=1

                            result = find_bingo(bingo_board)
  
                            if result >= 3:
                                flag = False
                                break
                            else:
                                continue

print(cnt)
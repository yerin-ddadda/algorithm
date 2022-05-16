for i in range(10):
    h = int(input())
    board = list(map(int, input().split()))
    
    cnt=0
    while cnt < h:
        max_idx = board.index(max(board))
        min_idx = board.index(min(board))
        board[max_idx] -= 1
        board[min_idx] += 1
        cnt+=1
    
    print("#{0} {1}".format(i+1,max(board) - min(board)))

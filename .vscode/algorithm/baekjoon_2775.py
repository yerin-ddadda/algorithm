t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())

    board = [i for i in range(1,n+1)]
    for a in range(k):
        for j in range(1,n):
            board[j] += board[j-1]
    print(board[-1])





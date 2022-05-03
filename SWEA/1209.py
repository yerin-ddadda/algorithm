def find_sum(board):
    max_sum = 0
    for a in range(100):
        sum = 0 
        for b in range(100):
            sum += board[a][b]
        if sum > max_sum:
            max_sum=sum
    
    for a in range(100):
        sum=0
        for b in range(100):
            sum += board[b][a]
        if sum > max_sum:
            max_sum=sum

    sum=0
    for a in range(100):
        sum += board[a][a]
    if sum > max_sum:
        max_sum=sum
    diagonal2 = [i for i in range(100)]
    diagonal = [i for i in range(99,-1,-1)]
    sum=0
    for a in range(100):
        sum += board[diagonal2[a]][diagonal[a]]
    if sum > max_sum:
        max_sum=sum

    return max_sum

for i in range(10):
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(100)]
    
    result = find_sum(board)
    print("#{0} {1}".format(i+1, result))
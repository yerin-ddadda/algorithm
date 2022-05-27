for i in range(10):
    num = int(input())
    board = [list(input().split()) for _ in range(100)]
    cnt = 0
    for a in range(100):
        s=''
        for b in range(100):
            s += board[b][a]
        s = s.replace('0', '')

        s = ''.join(s)

        cnt += s.count('12')
    print("#{} {}".format(i+1,cnt))
T = int(input())
for i in range(T):
    N,M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
   
    max_num = 0
    a = 0
    b = 0
    while a+M<=N:
        while b+M<=N:
            plus_num = 0
            for j in range(a,M+a):
                for k in range(b,M+b):
                    plus_num += board[j][k]
            if max_num < plus_num:
                max_num = plus_num
            b+=1
        a+=1
        b=0
    print("#{0} {1}".format(i+1,max_num))

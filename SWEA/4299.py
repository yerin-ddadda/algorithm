t = int(input())
for i in range(t):
    d,h,m = map(int,input().split())
    day = 11*1440 + 11*60 + 11
    wait = d*1440 + h*60 + m

    res = 0
    if wait-day < 0:
        res = -1
    else:
        res = wait-day

    print("#{} {}".format(i+1, res))
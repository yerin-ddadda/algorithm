t = int(input())
for i in range(t):
    a,b =map(int,input().split())
    cnt=0
    num=1
    check = 0
    while check<=b:
        check = num*num
        if a<=check<=b:
            if str(check)[:] == str(check)[::-1] and str(num)[:] == str(num)[::-1]:
                cnt+=1
        num+=1
    print("#{0} {1}".format(i+1, cnt))
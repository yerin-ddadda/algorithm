t= int(input())
for i in range(t):
    num = list(map(int,input()))
    com = [0 for _ in range(len(num))]

    cnt=0
    while com != num:
        for j in range(len(num)):
            if num[j] == com[j]:
                continue
            else:
                for k in range(j,len(num)):
                    com[k] = num[j]
                cnt+=1
    
    print("#{0} {1}".format(i+1, cnt))
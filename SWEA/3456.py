t=int(input())
for i in range(t):
    side = list(map(int,input().split()))
    for j in side:
        
        if side.count(j) == 1 or side.count(j) == 3:
            print("#",i+1,end=" ",sep="")
            print(j)
            break
        else:
            continue
    
    
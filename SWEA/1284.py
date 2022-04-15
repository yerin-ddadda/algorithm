T = int(input())

for i in range(T):
    P,Q,R,S,W = map(int, input().split())
    a = P*W
    if W<=R:
        b = Q
    else:
        b = S*(W-R)+Q
    
    if a>b:
        print("#",i+1," ",b,sep="")
        # print(b,end="")
    else:
        print("#",i+1," ",a,sep="")

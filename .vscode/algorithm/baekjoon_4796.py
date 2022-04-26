import sys
cnt=0
while True:
    
    ans=0
    cnt+=1
    l,p,v = map(int, sys.stdin.readline().split())
    if l==0:
        break
    share = v//p
    ans+=share*l
    if v-(p*share)>l:
        ans+=l
    else:
        ans+=v-(p*share)

    print("Case {0}: {1}".format(cnt, ans))
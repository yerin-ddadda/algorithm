t=int(input())
for i in range(t):
    n,m = map(int,input().split())
    x=n-m
    y=m-x
    print("#{0} {1} {2}".format(i+1, y,x))
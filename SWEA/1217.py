def dfs(n,m):
    if m==0:
        return 1
    else:
        return n*dfs(n,m-1)

for i in range(10):
    num = int(input())
    n,m=map(int,input().split())
    
    print("#{0} {1}".format(num,dfs(n,m)))
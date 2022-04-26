import sys
n,k = map(int, input().split())
a = [int(sys.stdin.readline().strip()) for _ in range(n)]

a.sort(reverse=True)

ans=0

for i in range(len(a)):
    if k>=a[i]:
        ans+=k//a[i]
        k-=a[i]*(k//a[i])
    else:
        continue
print(ans)
P, K = map(int,input().split())
cnt = 0

while P != K:
    K+=1
    cnt+=1
print(cnt+1)
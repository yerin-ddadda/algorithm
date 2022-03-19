n,c,w = map(int,input().split())
trees = [int(input()) for _ in range(n)]

L=1
max_sum = 0
while L<=max(trees):
    sum1 = 0
    sum2= 0 
    for i in range(n):
        K = trees[i]//L
        if trees[i]%L != 0:
            sum1=((K*L*w)-c*K)
        else:
            sum1=((K*L*w)-c*(K-1))
        if sum1 > 0:
            sum2+=sum1
        else:
            continue
    max_sum=max(max_sum, sum2)
    L+=1
print(max_sum)
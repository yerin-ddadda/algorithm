n,k = map(int,input().split())
knapsack = [[0]*(k+1) for _ in range(n+1)]


items =[]
for i in range(n):
    item = list(map(int,input().split()))
    items.append(item)



for i in range(n+1): #물건개수
    for j in range(k+1): #무게
        if j==0 or i==0:
            continue
        else:
            if items[i-1][0] <= j:
                knapsack[i][j] = max(knapsack[i-1][j], knapsack[i-1][j-items[i-1][0]]+items[i-1][1])
            else:
                knapsack[i][j] = knapsack[i-1][j]
print(knapsack[n][k])
    
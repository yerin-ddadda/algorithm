import sys
input = sys.stdin.readline
from itertools import combinations

n,m = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]
house = []
chicken = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            house.append((i,j))
        elif board[i][j] == 2:
            chicken.append((i,j))

pick_chicken = list(combinations(chicken,m))
print(pick_chicken)

ans = []
for i in pick_chicken:
    total = 0
    print("i", i)
    for j in house:
        minvalue = 10001
        for k in i:
            print("k",k)
            dist = abs(k[0]-j[0])+abs(k[1]-j[1])
            minvalue = min(minvalue,dist)
        print("minvalue",minvalue)
        total += min(minvalue,dist)
    ans.append(total)
print(min(ans))
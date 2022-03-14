from itertools import combinations

n,m = map(int,input().split())
board = []
chicken = []
home = []
for _ in range(n):
    city = list(map(int, input().split()))
    board.append(city)

chicken_list = [0] * m
def combination(chicken,level,BeginWith):
    if level==m:
        print(chicken_list)
    else:
        for i in range(BeginWith,len(chicken)):
            chicken_list[level]=chicken[i]
            combination(chicken,level+1,i+1)

def find_chicken(board):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                chicken.append([i,j])

def find_home(board):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                home.append([i,j])
find_home(board)

find_chicken(board)

minv = float('inf')
for ch in combinations(chicken,m):
    sumv = 0 
    for i in home:
        sumv += min([abs(i[0]-j[0])+abs(i[1]-j[1]) for j in ch])
        if minv <= sumv:
            break
    if sumv < minv:
        minv = sumv

print(minv)
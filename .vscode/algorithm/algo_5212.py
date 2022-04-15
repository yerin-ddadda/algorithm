import sys
import copy

R,C = map(int, sys.stdin.readline().split())

arr = []
for i in range(R):
    arr.append(list(input()))
print(arr)
new_arr = copy.deepcopy(arr)

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def recursion(x,y): 
    count=0 
    for i in range(4):
        xi = x+dx[i]
        yi = y+dy[i] 
        if xi<0 or yi<0 or xi>=R or yi>=C:
            count+=1
            if count>=3:
                new_arr[x][y] = "0"
            continue
        if new_arr[xi][yi] == ".":
            count+=1
            if count>=3:
                new_arr[x][y] = "0"
            continue
        
for i in range(R):
    for j in range(C):
        if new_arr[i][j] == "X":
            recursion(i,j)
            count=0

print(arr[0])

for i in range(R):
    count=0
    for j in range(C):
        if new_arr[0][j] =="." or new_arr[R-1][j] ==".":
            count+=1
            if count>=C:
                del new_arr[0]
print(new_arr)


import sys
from collections import defaultdict
input = sys.stdin.readline
dx = [0,0,-1,1]
dy = [-1,1,0,0]
N = int(input())
arr = [[0]*N for _ in range(N)]
likedict = defaultdict(list)
result = 0


for _ in range(N*N):
    numbers = list(map(int,input().split()))
    
    likedict[numbers[0]] = numbers[1:]
    max_x = 0
    max_y = 0
    max_like = -1
    max_empty = -1
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0: #0이니까 비어있는자리라고 생각하고 실행하기
                likecnt = 0
                emptycnt = 0
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if 0<=nx<N and 0<=ny<N:
                        if arr[nx][ny] in numbers:
                            likecnt+=1
                        if arr[nx][ny] == 0:
                            emptycnt+=1
                
                #한 자리마다 4방향 돌면서 4방향 그 자리가 딕셔너리에 좋아하는 숫자에 해당하는지(조건1)
                #0이라면 비어있는개수 체크하기(조건2)

                # print(max_like, likecnt, max_empty,emptycnt,max_x, max_y)
                if max_like < likecnt or (max_like == likecnt and max_empty < emptycnt):
                    max_x = i
                    max_y = j
                    max_like = likecnt
                    max_empty = emptycnt
    arr[max_x][max_y] = numbers[0]

for i in range(N):
    for j in range(N):
        cnt = 0
        like = likedict[arr[i][j]]
        
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0<=nx<N and 0<=ny<N:
                if arr[nx][ny] in like:
                    cnt += 1
 
        if cnt!=0:
            result += 10 ** (cnt-1)

print(result)
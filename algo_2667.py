number = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]
count = 0
count_list =[]
a=1
def APT_DFS(x,y):
    global a
    global count
    count+=1
    isvisited[x][y] = a
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0<=nx<number and 0<=ny<number and isvisited[nx][ny]==0 and APT_complex[nx][ny] =='1':
            APT_DFS(nx,ny)
            


APT_complex = []
for i in range(number):  
    ishouse = input()
    APT_complex.append(ishouse)

isvisited = []
for i in range(number):
    append_list = []
    for j in range(number):
        append_list.append(0)
    isvisited.append(append_list)

for i in range(number):
    for j in range(number):
        if APT_complex[i][j] == '1' and isvisited[i][j]==False:
            a+=1
            count = 0
            APT_DFS(i,j)
            count_list.append(count)
a = sorted(count_list)
print(len(a))
for i in range(len(a)):
    print(a[i])


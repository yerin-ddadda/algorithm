number = int(input())
field_list = []

queue = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def location(x,y):
    isvisited[x][y] = True
    queue.append([x,y])
    while queue:
        i,j = queue[0][0], queue[0][1]
        del queue[0]
        for k in range(4):
            nx = dx[k] + i
            ny = dy[k] + j
            if 0<=nx<R and 0<=ny<C and isvisited[nx][ny]==False and field_list[nx][ny]=="#":
                queue.append([nx,ny])
                isvisited[nx][ny] = True



while number:
    count =0
    R,C = map(int, input().split())
    isvisited = []
    field_list=[]
    for i in range(R):
        append_list = []
        for j in range(C):
            append_list.append(False)
        isvisited.append(append_list)
    # R, C = map(int, input().split())
    for i in range(R):
        char = input()
        field_list.append(char)
    for i in range(R):
        for j in range(C):
            if field_list[i][j] == "#" and isvisited[i][j] == False:
                location(i,j)
                count+=1
    print(count)
    number -=1

isvisited = []
dx = [-1,1,2,2,1,-1,-2,-2]
dy = [2,2,1,-1,-2,-2,-1,1]

def location(x,y,x2,y2):
    a = 0
    queue =[]
    queue.append([x,y])
    isvisited[x][y] = True
    while queue:
        queue_size=0
        queue_size=len(queue)
        a+=1
        for i in range(queue_size):
            x, y = queue[0][0], queue[0][1]
            del queue[0]
            if x == x2 and y == y2: 
                return a-1
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<size and 0<=ny<size and isvisited[nx][ny]==False:
                    queue.append([nx,ny])
                    isvisited[nx][ny] = True
                    
number = int(input())
while number:
    size = int(input())
    isvisited = []
    for i in range(size): #방문처리
        append_list = []
        for j in range(size):
            append_list.append(False)
        isvisited.append(append_list)
    x,y = map(int, input().split())
    x2, y2 = map(int, input().split()) 
    if x == x2 and y == y2:
        print(0)
        number -=1
        continue
    count = location(x,y,x2,y2)
    print(count)
    number-=1


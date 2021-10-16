R,C = map(int, input().split())
field = []

isvisited = []
append_list = [] #방문처리
for i in range(R):
  append_list = []
  for j in range(C):
    append_list.append(False)
  isvisited.append(append_list)

count = 0
while True: #양과 늑대가 뛰어노는 공간
  if count == R:
    break
  char = input()
  field.append(char)
  count += 1
 
dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = []
def location(i,j):
  global sheep
  global wolf
  isvisited[i][j] = True
  queue.append([i,j])

  while queue:
    i,j = queue[0][0], queue[0][1]
    del queue[0]
    if field[i][j] == "v":
      wolf += 1
    elif field[i][j] == "o":
      sheep += 1
    for k in range(4):
      nx = i + dx[k]
      ny = j + dy[k]
      if 0<=nx<R and 0<=ny<C and field[nx][ny] != "#" and isvisited[nx][ny] == 0:
        queue.append([nx,ny]) #사방에 있는거 큐에넣 2,2 3,1
        isvisited[nx][ny] = True

total_wolf = 0
total_sheep = 0

for i in range(R):
  for j in range(C):
    wolf = 0
    sheep = 0
    if field[i][j] != "#" and isvisited[i][j] == False:
      location(i,j)
      if wolf>=sheep:
        sheep = 0
      else:
        wolf = 0
      total_sheep += sheep
      total_wolf += wolf
        
print(total_sheep, "", total_wolf)

'''def location(i,j): #Dfs
  global sheep
  global wolf
  isvisited[i][j] = True
  if field[i][j] =="o":
      sheep += 1    
  elif field[i][j] =="v":
      wolf +=1
  for k in range(4):
    nx = i+ dx[k]
    ny = j+ dy[k]
    if 0<=nx<R and 0<=ny<C and field[nx][ny] != "#" and isvisited[nx][ny] ==False:
      location(nx,ny)

field = []
isvisited = []

count = 0

total_wolf = 0
total_sheep = 0

dx = [0,0,-1,1]
dy = [1,-1,0,0]

R,C = map(int, input().split())

append_list = [] #방문처리
for i in range(R):
  append_list = []
  for j in range(C):
    append_list.append(False)
  isvisited.append(append_list)

while True: #양과 늑대가 뛰어노는 공간
  if count == R:
    break
  char = input()
  field.append(char)
  count += 1

for i in range(R):
  for j in range(C):
    sheep = 0
    wolf =0
    if field[i][j] != "#" and isvisited[i][j] == False:
      location(i,j)
      if sheep>wolf:
        wolf = 0
      else:
        sheep = 0
      total_wolf += wolf
      total_sheep += sheep
print_list = []
for i in range(1):
  print_list.append(total_sheep)
  print_list.append(total_wolf)
for i in range(2):
  print(print_list[i], end=" ")'''
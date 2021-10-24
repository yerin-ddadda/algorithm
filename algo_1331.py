input_list =[]
for i in range(36):
    char=input()
    y= int(ord(char[0])-65)
    x= int(char[1])-1
    input_list.append([x,y])
# print(input_list)#[[0, 0], [2, 1], [4, 0], [5, 2], [4, 4], [2, 5], [1, 3], [0, 5]...

isvisited=[]
append_list=[]
for i in range(6):
    append_list=[]
    for j in range(6):
        append_list.append(False)
    isvisited.append(append_list)
# print(isvisited) #[[False, False, False, False, False, False], [False, False, False, False, False, False], ...

dx = [-1,1,2,2,1,-1,-2,-2]
dy= [2,2,1,-1,-2,-2,-1,1]

count=1
startX, startY = input_list[0][0], input_list[0][1]
startX_startY=[startX,startY]
isvisited[startX][startY] = True

for i in range(0,37):
    currentX, currentY =input_list[i][0] ,input_list[i][1]


    if count==36:
        movex_movey = []
        for j in range(8):
            moveX = currentX + dx[j]
            moveY= currentY + dy[j]
            movex_movey.append([moveX, moveY])

        if startX_startY in movex_movey:
            print("Valid")
            break
        if startX_startY not in movex_movey:
            print("Invalid")
            break
        break
    moveX_moveY = []
    for j in range(8):
        currentX_currentY = [input_list[i+1][0], input_list[i+1][1]]
        input_list[i+1][0]
        
        moveX = currentX + dx[j]
        moveY= currentY + dy[j]
        moveX_moveY.append([moveX, moveY])
    if currentX_currentY in moveX_moveY:
        if isvisited[input_list[i+1][0]][input_list[i+1][1]]==True:
            print("Invalid")
            break
        if isvisited[input_list[i+1][0]][input_list[i+1][1]]==False:
            isvisited[input_list[i+1][0]][input_list[i+1][1]]=True
            count+=1

    else:
        count=0
        print("Invalid")
        break   
            
    if count==0:
        print("Invalid")
        break
        
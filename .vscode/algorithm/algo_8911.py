T = int(input())
dx=[0,1,0,-1] #북동남서
dy=[1,0,-1,0]
control_program = []


for i in range(T):
    max_x=0
    min_x=0
    max_y=0
    min_y=0

    control=input()
    control_program.append(list(control))
    x=0
    y=0
    dir=0
    for j in range(len(control_program[i])):

        if dir>3:
            dir=dir%4
        elif dir<0:
            dir=dir+4

        if control_program[i][j]=="F":
            x=x+dx[dir]
            y=y+dy[dir]   
        elif control_program[i][j]=="B":
            x=x-dx[dir]
            y=y-dy[dir]
        elif control_program[i][j]=="L":
            dir-=1
        else: #R일때
            dir+=1

        if max_x<x:
            max_x=x
        if min_x>x:
            min_x=x
        
        if max_y<y:
            max_y=y
        if min_y>y:
            min_y=y
  
    print((abs(min_x)+max_x) * (abs(min_y)+max_y))
        


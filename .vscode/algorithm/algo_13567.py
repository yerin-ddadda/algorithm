N, total_times = map(int, input().split()) #11,14
action_list = ['R','T','L','B']
current_loc =[]
for i in range(2):
    current_loc.append(int(0))
j = action_list[0]
k=0


for i in range(total_times):
    action, times = input().split()
    times = int(times)
    if action == "MOVE":
        if j == "T":
            current_loc[1] = current_loc[1]+times
        elif j == "L":
            current_loc[0] = current_loc[0]-times
        elif j == "B":
            current_loc[1] = current_loc[1]-times
        else: #direction == "R"
            current_loc[0] = current_loc[0]+times

    elif action == "TURN":
        if times == 0:
            k+=1
            if k>=4:
                k=0
            j = action_list[0+k]
        else: # TURN 1 오른쪽으로 90도
            k-=1  
            if k<0:
                k=3      
            j = action_list[0+k]
    
    if current_loc[1] < 0 or current_loc[0] <0 or current_loc[1]>N or current_loc[0]>N:
        current_loc=[-1]
        break
for i in range(len(current_loc)):
    print(current_loc[i], end=" ")
    
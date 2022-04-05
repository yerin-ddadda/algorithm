split_list = []

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def check_list(split_list):
    cnt=0
    for i in range(len(split_list)):
        for j in range(len(split_list[i])):
            if split_list[i][j] == "P":
                for k in range(4):
                    x = i+dx[k]
                    y = j+dy[k]
                    if 0<=x<5 and 0<=y<5 and split_list[x][y] != "P":
                        continue
                    elif 0<=x<5 and 0<=y<5 and split_list[x][y] == "P":
                        return 0
                
            elif split_list[i][j] == "O":
                cnt=0
                for k in range(4):
                    x = i+dx[k]
                    y = j+dy[k]
                    if 0<=x<5 and 0<=y<5 and split_list[x][y] == "P":
                        cnt+=1
                if cnt>=2:
                    return 0
    if cnt<2:
        return 1        


def solution(places):
    answer = []
    global split_list


    for i in range(len(places)):
        split_list = []
        for j in range(len(places[i])):
            a = list(places[i][j])
            split_list.append(a)
        print(split_list)
        answer.append(check_list(split_list))
       
    print(answer)

people_number = int(input()) #사람이 몇명인지 입력받기
dungchi_list = []
rank_list =[]

for i in range(people_number): #등수를 0으로 채워넣기
    rank_list.append(1)

weight = 0
height = 0

for i in range(people_number): #키몸무게 입력받고 이중리스트에 넣기
    in_dungchi_list = []
    for j in range(1):
        weight,height= map(int,input().split())
        in_dungchi_list.append(weight)
        in_dungchi_list.append(height)
    dungchi_list.append(in_dungchi_list)

for i in range(people_number-1):
    for j in range(i+1,people_number):
        if dungchi_list[i][0] > dungchi_list[j][0] and dungchi_list[i][1] > dungchi_list[j][1]:
            rank_list[j] += 1
        elif dungchi_list[i][0] < dungchi_list[j][0] and dungchi_list[i][1] < dungchi_list[j][1]:
            rank_list[i] +=1


for i in range(len(rank_list)):
    print(rank_list[i], end=" ")
N, K = map(int, input().split()) #게임에 참여하는 사람의 수, 보성이의 번호

order = []
point_to_list = []

j=0
i=0
while True:
    empty_list = []
    empty_list.append(j)
    point_to_list.append(empty_list)
    point_number = int(input())
    order.append(point_number)
    point_to_list[i].append(point_number)
    j+=1
    i+=1
    if i==N:
        break

next = 0
count = 0
while True:
    next = point_to_list[next][1]
    count+=1
    if next ==K:
        print(count)
        break
    if count >= N and next != 2:
        print(-1)
        break
    

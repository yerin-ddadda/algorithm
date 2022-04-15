N, M, L = map(int, input().split())

M_list = [] #각자 공을 몇번받았는지 횟수
ball_count = 0 #볼이 몇번 던져졌는지

current_ball = 0

for i in range(N):
    M_list.append(0)

M_list[0] = 1


while True: 
    if M_list[current_ball] == M:
        break

    if M_list[current_ball] %2 != 0:
        current_ball = (current_ball+L)%N
        M_list[current_ball] += 1

        print("1111111111111",current_ball,M_list)

    elif M_list[current_ball] %2 == 0:
        if current_ball >= 2:
            current_ball = (current_ball-L)%N
        else: #current_ball이 0,1일때 (시계 반시계방향)
            current_ball = current_ball-L
            if current_ball <= :
                current_ball = -current_ball
                current_ball = current_ball%N
                current_ball = -current_ball
                current_ball = current_ball+N
        print("22222222222",current_ball,M_list)
        M_list[current_ball] += 1
    print("333333333333",current_ball,M_list)


        
    ball_count+=1
    
print(ball_count)
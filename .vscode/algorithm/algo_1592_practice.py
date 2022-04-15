N, M, L = map(int, input().split())

M_list = [] #각자 공을 몇번받았는지 횟수
ball_count = 0 #볼이 몇번 던져졌는지

current_ball = 0

for i in range(N):
    M_list.append(0)

M_list[0] = 1

while True:
 
    if M_list[current_ball] %2 != 0:
        current_ball = (current_ball+L)%N
        M_list[current_ball] += 1
    else:#
        current_ball=(current_ball-L)%N
        M_list[current_ball] += 1
    if M_list[current_ball] == M:
        ball_count +=1
        break
    ball_count +=1
print(ball_count)
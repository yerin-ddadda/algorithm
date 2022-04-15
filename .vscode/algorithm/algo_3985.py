cake_length = int(input()) #케이크의 길이 입력
people_number = int(input()) #사람 수 입력

cake_length_list = [] # 케이크 한조각씩 리스트에 담으려고 리스트로 만듦
expected_audience = 0 # 출력할 예상했던 방청객
real_audience = 0 #실제로 많이 케이크 먹게될 방청객

cake_total_want_list = [] #

for i in range(people_number): #방청객 한명씩 어디부터 어디까지 먹을건지 입력하고 
    cake_want_list = []
    num1, num2 = map(int, input().split())
    cake_want_list.append(num1-1)
    cake_want_list.append(num2-1)
    cake_total_want_list.append(cake_want_list) #리스트에 담아서 중첩 리스트로 만들기


for i in range(cake_length):
    cake_length_list.append(int(0)) #케이크의 길이만큼 케이크리스트에 0으로 채워넣음


real_audience_list = [] #
for i in range(people_number): #
    count = 0
    for j in range(cake_total_want_list[i][0], cake_total_want_list[i][1]+1): #[1,4]라고 입력했으면 [1,2,3,4]로 중첩리스트 새로만들기
        if cake_length_list[j] == 0: #케이크0으로 채웠던 리스트 체크하면서 0이면 아직 아무도 안먹은거니까
            cake_length_list[j]=i+1 # 먹었으면 0에서 그 숫자로 덮어씌우기
            count += 1 #덮어씌워진 숫자로 누가 제일 많이 먹었는지 카운트로 가장 큰 숫자 알아내기
    real_audience_list.append(count) #여기서 가장 큰 숫자인 인덱스가 출력되기


max_num = 0
max_num_index = 0
for i in range(len(real_audience_list)): #가장 큰 숫자인 인덱스 알아내기
    if max_num < real_audience_list[i]:
        max_num = real_audience_list[i] #가장 큰 숫자의 인덱스(사람)알아내기
        max_num_index = i



  
max_len = 0
for i in range(people_number):
    want_length=cake_total_want_list[i][1] - cake_total_want_list[i][0] +1 #[1,4]면 4-1+1로 예상했을때 누가 제일 많이 먹었을까?
    if max_len <want_length:
        max_len = want_length
        expected_audience = i+1 #가장 큰 숫자 알아내기


print(expected_audience)
print(max_num_index+1)
  



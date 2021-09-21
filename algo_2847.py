level = int(input()) #몇단계까지 있는지 입력받음
beginning_level_score_list = [] #초기 단계별 점수 리스트
copy_level_score_list = [] #특정 레벨의 점수 감소 시킨 리스트
print_score_list = [] #초기 점수랑 나중 점수 계산한 리스트 (출력할 리스트)

for i in range(level): # 초기 단계별 점수 리스트 입력받음
    level_score = int(input())
    beginning_level_score_list.append(level_score)
    copy_level_score_list.append(level_score)

beginning_level_score_list=beginning_level_score_list[::-1] #거꾸로 다시 초기 리스트에 집어넣음
copy_level_score_list=copy_level_score_list[::-1]

for i in range(len(beginning_level_score_list)-1):    
    if beginning_level_score_list[i] <= beginning_level_score_list[i+1]:
        beginning_level_score_list[i+1]=beginning_level_score_list[i]-1 #점수차 얼마나 나는지 저장해서 출력할 리스트에 넣음
        print_score_list.append(copy_level_score_list[i+1] - beginning_level_score_list[i+1])
        
sum_i = 0
for i in print_score_list:
    sum_i += i
print(sum_i)

# lst = [0,3,4,5,6]
# print("lala", lst[-1])

# for i in lst[:-1]:
#     print(lst[i])

number = int(input())
rope_list = []
compare_list = []

for i in range(number):
    N = int(input())
    rope_list.append(N)

rope_list.sort() #숫자정렬

max_num = 0
rope_num =len(rope_list)
rope_max_list= []
for i in range(number):
    rope_max_list.append(rope_list[i] * rope_num)
    rope_num -= 1

for i in range(len(rope_max_list)):
    if max_num < rope_max_list[i]:
        max_num=rope_max_list[i]
print(max_num)
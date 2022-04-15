T = int(input())
testcase = [list(map(int,input().split())) for _ in range(T)]

for i in range(len(testcase)):
    sum_num = 0
    answer = 0
    for j in range(len(testcase[i])):
        sum_num += testcase[i][j]
    answer = sum_num/10
    
    print("#",end="")
    print(str(i+1),round(answer))
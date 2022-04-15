T = int(input())
testcase = [list(map(int,input().split())) for _ in range(T)]

for i in range(len(testcase)):
    sum_num = 0
    for j in testcase[i]:
        if j%2 == 1:
            sum_num += j
    print("#"+str(i+1),sum_num)

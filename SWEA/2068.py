T = int(input())
testcase = [list(map(int, input().split())) for _ in range(T)]

for i in range(len(testcase)):
    max_num = 0
    for j in testcase[i]:
        if j>max_num:
            max_num = j
    print("#", end="")
    print(str(i+1),max_num)
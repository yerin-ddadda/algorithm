T = int(input())
testcase = [list(map(int, input().split()))for _ in range(T)]

for i in range(len(testcase)):

    if testcase[i][0] > testcase[i][1]:
        print("#",end="")
        print(i+1,">")
    elif testcase[i][0] < testcase[i][1]:
        print("#",end="")
        print(i+1,"<")
    else:
        print("#",end="")
        print(i+1,"=")
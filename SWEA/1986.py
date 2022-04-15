answer_list = []
def calc(testcase):
    answer = 0
    for i in range(1,testcase+1):
        if i%2 != 0:
            answer = answer + i
        else:
            answer -= i
    answer_list.append(answer)

T = int(input())
for i in range(T):
    testcase = int(input())
    calc(testcase)

for i in range(len(answer_list)):
    print("#",i+1, sep="", end=" ")
    print(answer_list[i])
    
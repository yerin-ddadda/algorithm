from collections import defaultdict


T = int(input())
answer = [[] for _ in range(T)]
def factorization(testcase):
    d = 2
    answer_dic = defaultdict(int)
    while testcase>=d:
        if testcase%d==0:
            answer_dic[d] += 1
            testcase = testcase//d
        else:
            d+=1
    answer[i].append(answer_dic[2])
    answer[i].append(answer_dic[3])
    answer[i].append(answer_dic[5])
    answer[i].append(answer_dic[7])
    answer[i].append(answer_dic[11])

for i in range(T):
    testcase = int(input())
    factorization(testcase)

for i in range(len(answer)):
    print("#",i+1,sep="", end=" ")
    for j in range(len(answer[i])):
        print(answer[i][j], end=" ")  
    print()  
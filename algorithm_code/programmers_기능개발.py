from collections import deque
q = deque()

def solution(progresses, speeds):
    answer = []

    sub = []
    for i in range(len(progresses)):
        sub.append(100 - progresses[i])
    
    sub2 = []
    for i in range(len(speeds)):
        if sub[i]%speeds[i] != 0:
            sub2.append(sub[i]//speeds[i]+1)
        else:
            sub2.append(sub[i]//speeds[i])

    print(sub2)
    # for i in range(len(sub2)):
    #     if sub2[i] == 0:
    #         continue
    #     cnt=0
    #     for j in range(i, len(sub2)):
    #         if sub2[j] == 0:
    #             continue
    #         if sub2[i] >= sub2[j]:
    #             cnt+=1
    #             # sub2[j]=0
    #         elif sub2[i] <= sub2[j]:
    #             break

    #     answer.append(cnt)
    #     abc = 0
    #     while abc == cnt:
    #         for k in range(len(sub2)):
    #             if sub2[k] != 0:
    #                 sub2[k] = 0
    #                 cnt+=1
    #     x2 = 0
   

    

    return answer

a = solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])
print(a)
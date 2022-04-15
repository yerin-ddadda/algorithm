def solution(L, x):
    answer = []
    
    for i in range(len(L)):
        if L[i] == x:
            answer.append(i)
            print(answer)
        
    return answer

solution([64, 72, 83, 72, 54], 72)
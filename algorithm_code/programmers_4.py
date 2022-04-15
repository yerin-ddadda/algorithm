def solution(x):
    if(x<2):
        return x
    
    answer = solution(x-1) + solution(x-2)
    return answer
def solution(L, x):
    answer = []
    for i in range(len(L)):
        print("x:",x,"L[i]:",L[i])
        if(x <= L[i]):
            L.insert(i, x)
            answer = L
            break
        if(x>L[-1]):
            L.append(x)
            answer=L
        answer = L
    return answer


a = solution([20,37,58],240)
print(a)

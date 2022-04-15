def solution(L,x):
    lower = 0
    upper = len(L)-1
    idx = -1
    if len(L)==0:
        return idx
    while lower <= upper:
        middle = (lower+upper)//2
        if L[middle] == x:
            return middle

        elif L[middle] < x:
            lower = middle+1

        elif L[middle] > x:
            upper = middle-1
        
        else:
            return idx
        if upper==middle or lower==middle:
            return idx
        
a = solution([],3)
print(a)
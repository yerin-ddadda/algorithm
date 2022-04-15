import string


def solution(numbers):
    answer = ''
    a = []

    for i in numbers:
        b =list(map(int,str(i)))
        a.append(b)
    
    a.sort(reverse=True)
    print(a)

    c=[]
    for i in a:
        print(i,end="")
    return answer

solution([3, 30, 34, 5, 9])    
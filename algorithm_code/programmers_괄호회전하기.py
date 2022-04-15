def solution(s):
    pair = {"]":"[", "}":"{", ")":"("}
    answer = -1

    # s의 길이 x만큼 회전시키기
    for i in range(len(s)-1):
        print(s[i+1:]+s[:i+1])


    return answer

solution("}]()[{")
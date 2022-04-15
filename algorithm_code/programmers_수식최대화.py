import re

def solution(expression):
    operator = [['*','+','-'],["*","-","+"],["-","+","*"],["-","*","+"], ["+","*","-"],["+","-","*"]]
    answer = []
    

    for i in operator:
        temp = re.compile("(\D)").split(expression)
        for exp in i:
            while exp in temp:
                idx = temp.index(exp)
                temp = temp[:idx-1] + [str(eval(''.join(temp[idx-1:idx+2])))] + temp[idx+2:]
                print(temp)

        answer.append(abs(int(temp[0])))
        print(answer)
    return max(answer)



solution("50*6-3*2")

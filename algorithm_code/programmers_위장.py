from collections import Counter

def solution(clothes):
    answer = 0
    cloth_dict = {}
    for cloth in range(len(clothes)):
        cloth_dict[clothes[cloth][0]] =clothes[cloth][1]
    print(cloth_dict)
    


    counter = {}
    for letter in cloth_dict.values():
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    print(counter)

    num_list = 1
    for i in counter.values():
   
        num_list*=int(i)+1
    
    answer = num_list-1
    return answer


a = solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])
print(a)
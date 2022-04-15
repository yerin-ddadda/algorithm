from itertools import permutations, product


def solution(numbers, target):
    # answer = 0
    store = [[]*2 for _ in range(len(numbers))]


    for i in range(len(store)):
        store[i]= numbers[i],-numbers[i]


    # for i in range(len(store)*2):
    a = list(product(*store))
    # for i in a:
    #     if sum(i) == target:
    #         answer+=1
    
        
    return a.count(target)
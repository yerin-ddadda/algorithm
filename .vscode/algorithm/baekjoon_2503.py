# import itertools
# import sys
# result =[]
# for a,b,c in itertools.permutations(['1','2','3','4','5','6','7','8','9'],3):
#     result.append(a+b+c)

# answer_list =[]
# another_list = []

# answer_dic = {}
# T = int(input())
# for _ in range(T):
#     cnt=0

#     a,b,c = map(int,sys.stdin.readline().split())
#     word = list(str(a))
#     # print(word)
#     for k in range(len(word)):
#         word[k] = str(word[k])
#     # print(result)
#     for i in range(len(result)):
#         ball = 0
#         strike = 0
#         for j in range(3):
#             # print(i)          
#             if result[i][j] == word[j]:
#                 strike+=1
#             elif word[j] in result[i]:
#                 ball+=1

#         if strike == b and ball == c:
#             if result[i] in answer_dic:
#                 answer_dic[result[i]] += 1
#             else:
#                 answer_dic[result[i]] = 1

# cnt=0
# for value in answer_dic.values():
#     if value == T:
#         cnt += 1
# print(cnt)        

import itertools

n = int(input())
numbers= list(itertools.permutations([1,2,3,4,5,6,7,8,9],3))
dic= {}
for i in range(len(numbers)):
    dic[numbers[i]] = 0

for _ in range(n):
    number, strike_number, ball_number = map(int, input().split())

    
    for i in range(10,len(numbers)):
        
        strike=0
        ball=0
        number = str(number)
        for j in range(3):
            if str(number[j]) == str(numbers[i][j]):
                strike+=1
            elif str(number[j]) in str(numbers[i]):
                ball+=1

        if strike == strike_number and ball == ball_number:
            dic[numbers[i]] += 1
        else:
            dic[numbers[i]] = 0

cnt=0
for i in range(len(numbers)):
    if dic.get(numbers[i]) == n:
        cnt+=1
print(cnt)



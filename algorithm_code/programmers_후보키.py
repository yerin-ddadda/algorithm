from itertools import combinations
import itertools

def solution(relation):
    num_list = [i for i in range(len(relation[0]))]
    
    for i in num_list:
        
    answer = 0
    return answer

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])
# def solution(relation):
#     answer = 0
#     primary_key_check = []
#     for i in range(len(relation[0])):
#         primary_key_check.append(0)        

#     for i in range(len(relation[0])):
#         check_list =[]
        
#         for j in range(len(relation)):
#             if relation[j][i] not in check_list:
#                 check_list.append(relation[j][i])
        
#         if len(check_list) == len(relation):
#             primary_key_check[i] = 1

#     for i in range(len(primary_key_check)):
#         if primary_key_check[i] != 1:
            
#             for j in range(len(relation)):
#                 if relation[j][i] not in check_list:
#                     a = relation[j][i]+relation[j][i+1]
            
        
#         if len(check_list) == len(relation):
#             primary_key_check[i] = 1        

#     print(primary_key_check)         
#     return answer

# solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])


def solution(relation):
    answer = 0
    return answer

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]],2)
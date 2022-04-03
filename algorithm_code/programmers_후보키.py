from itertools import combinations

def solution(relation):
    # key의 개수 
    N = len(relation[0])
    key_idx = list(range(N))
    candidate_keys = []
    
    for i in range(1,N+1):
        for comb in combinations(key_idx, i):
            hist = []
            for rel in relation:
                current_key = [rel[c] for c in comb]
                # 하나라도 중복되는 경우: 식별 불가능 
                if current_key in hist:
                    break
                else:
                    hist.append(current_key)
            # 하나도 중복 안 된 경우: 식별 가능
            else:
                for ck in candidate_keys:
                    # 최소성 확인 
                    if set(ck).issubset(set(comb)):
                        break
                else:
                    candidate_keys.append(comb)
    
    return len(candidate_keys)

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
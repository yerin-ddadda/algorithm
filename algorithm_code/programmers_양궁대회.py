from itertools import product

def solution(n, info):
    lion_score_list = []
 
    combi_list = [[0] for i in range(11)]
    for i in range(11):
        combi_list[i].append(info[i]+1)

    lion_info_lists = list(product(*combi_list))
    # print(lion_info_lists,"1231231231231")
    max_score = 0
    for i in range(len(lion_info_lists)):
        if sum(lion_info_lists[i]) == n:
                   
            score = 10
            info_score = 0
            lion_score = 0
            for j in range(len(lion_info_lists[i])):
                # print(lion_info_lists[i])
                if lion_info_lists[i][j] == 0 and info[j] == 0:
                    score-=1
                    continue
                if lion_info_lists[i][j] > info[j]:
                    lion_score += score
                else:
                    info_score += score
                score -= 1
            # print("fkfkfkfkfkfk","info_score", info_score,info)
            # print("!!!!!!!!!!!",lion_score,lion_score_list)
            if lion_score > info_score:
                # print("info_score", info_score, "lion_score", lion_score)
                if max_score < lion_score:
                    max_score = lion_score
                   
                    
                    lion_score_list.append(lion_info_lists[i])
                    # print(lion_score,"lion score")
                    # print(info_score, "info_score", info)
                    # print(i,"?????????????",lion_score,lion_score_list)
            
    # print(lion_score_list)
    # print(max_score)




        # for i in range(10):
        #     if number == 0: 
        #         break
        #     lion_info[i] = info[i] + 1
        #     number -= lion_info[i]
    #     score = 10
    #     for i in range(10):
    #         if lion_info[i] == 0 and info[i] == 0:
    #             continue
    #         if lion_info[i] <= info[i]:
    #             info_score += score
    #         else:
    #             lion_score += score
    #         score -= 1
    #     lion_score_list.append(lion_score)

    # return max(answer)

solution(10,[0,0,0,0,0,0,0,0,3,4,3])
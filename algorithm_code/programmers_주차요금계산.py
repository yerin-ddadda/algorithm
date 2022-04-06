# def solution(fees, records):
#     answer = []
#     dic = {}
#     total_time_dict = {}

#     accumulated_parking_time = {}


#     for i in range(len(records)):
#         if records[i][11:] =="IN":
#             dic[records[i][6:10]]  = records[i][:5]
#         else:
#             money = 0
#             print(records[i])
#             print()
            
#             time = records[i][:2]
#             sec = records[i][3:5]
#             calcul_time = abs(int(dic[records[i][6:10]][:2])-int(time))
#             calcul_sec = 0
#             sec2=0
#             if (int(dic[records[i][6:10]][3:5])-int(sec)) > int(sec):
#                 calcul_time -= 1
#                 # calcul_sec += (int(dic[records[i][6:10]][3:5])-int(sec))
#                 # int(records[i][3:4]) += 6
#                 calcul_sec += abs((int(dic[records[i][6:10]][3:5])-(int(sec)+60)))

#             if calcul_time*60 + calcul_sec < fees[0]:
#                 # money += fees[1]
#                 # total_time_dict[records[i][6:10]] = money
#                 accumulated_parking_time[records[i][6:10]]+=int(calcul_time*60 + calcul_sec)
#                 print(accumulated_parking_time)

#             else: #180보다 크면 
#                 # total_time_dict[records[i][6:10]] += (((abs(records[i][:2]-time) + abs(records[i][3:5]-sec) < fees[0]) - fees[0]) // fees[2]) * fees[3]
#                 accumulated_parking_time[records[i][6:10]]+=int(calcul_time*60 + calcul_sec)
#                 print(accumulated_parking_time)
#     print(total_time_dict)
#     return answer

# solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
import math

def solution(fees, records):
    answer = []
    car = list(set(map(lambda x: x.split()[1], records)))
    cumulative_time= {k : 0 for k in car}

    check = {}
    tmp = []
    for i in range(len(records)):
        tmp.append(records[i].split())

    for i in range(len(tmp)):
        out_time = 0
        in_time = 0

        if tmp[i][1] not in check:
            check[tmp[i][1]] = tmp[i][0]
        else:
            out_time = (int(tmp[i][0][:2])*60 + int(tmp[i][0][3:5]))   
            in_time = int(check[tmp[i][1]][:2]) * 60 + int(check[tmp[i][1]][3:])

            cumulative_time[tmp[i][1]] = cumulative_time[tmp[i][1]] + (out_time - in_time)
            del check[tmp[i][1]]


    for i in check:
        out_time = 0
        in_time = 0
        out_time = 23*60 + 59
        in_time = int(check[i][:2]) * 60 + int(check[i][3:])
        
        cumulative_time[i] = cumulative_time[i] + (out_time - in_time)
    cumulative_time = sorted(cumulative_time.items())
    cumulative_time = dict(cumulative_time)



    for i in cumulative_time:
        if cumulative_time[i] > fees[0]:
            if (cumulative_time[i]-fees[0]) % fees[2] !=0:
                a = math.ceil((cumulative_time[i]-fees[0]) // fees[2]) +1
                answer.append(fees[1] + a * fees[3])
            else:
                a = math.ceil((cumulative_time[i]-fees[0]) // fees[2])
                answer.append(fees[1] + a * fees[3])
        else:
            answer.append(fees[1])




    return answer

solution([1, 461, 1, 10],["00:00 1234 IN"])
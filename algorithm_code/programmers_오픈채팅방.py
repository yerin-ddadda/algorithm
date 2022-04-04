def solution(record):
    answer = []
    dic = {}
    for i in range(len(record)):
        a = record[i].split()
        if a[0] == "Enter":
            dic[a[1]] = a[2]
   
        elif a[0] == "Change":
            dic[a[1]] = a[2]
    print(dic)

    for i in range(len(record)):
        a = record[i].split()
        if a[0] == "Enter":
            answer.append(dic[a[1]]+"님이 들어왔습니다.")
        elif a[0] == "Leave":
            answer.append(dic[a[1]]+"님이 나갔습니다.")
    print(answer) 

    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])

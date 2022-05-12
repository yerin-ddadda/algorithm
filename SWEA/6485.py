t = int(input())
for i in range(t):
    n = int(input())
    lst = []
    for j in range(n):
        lst.append(list(map(int, input().split())))
    
    bus_stop = []

    c_dic = {}
    p = int(input())
    for j in range(p):
        c = int(input())
        c_dic[c] = 0
        bus_stop.append(c)
    
    for a in range(len(lst)):
        for b in range(lst[a][0],lst[a][1]+1):
            if b in c_dic:
                c_dic[b] += 1
            

    print("#{0} ".format(i+1), end="")
    # for k in c_dic.values():
    #     print(f'{k}', end=" ")
    # 순서 지켜야하면 values 쓰지않기!
    for k in bus_stop:
        print(c_dic[k], end=" ")
    print()
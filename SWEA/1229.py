for i in range(10):
    n = int(input())
    ori = list(map(int, input().split()))
    order_num = int(input())
    order = list(input().split())

    for j in range(len(order)):
        if order[j]== "I":
            loc = int(order[j+1])
            cnt = int(order[j+2])
            lst = []

            for k in range(cnt):
                lst.append(order[j+3+k])
            for k in range(len(lst)-1,-1,-1):
                ori.insert(loc,lst[k])

        elif order[j] == "D":
            loc = int(order[j+1])
            cnt = int(order[j+2])
            for k in range(cnt):
                
                del ori[loc]

    print("#{} {} {} {} {} {} {} {} {} {} {}".format(i+1, *ori))
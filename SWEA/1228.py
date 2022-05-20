for i in range(10):
    n = int(input())
    original = list(map(int, input().split()))
    order_num = int(input())
    order = list(input().split())

    for j in range(len(order)):
        if order[j] == "I":
            loc = int(order[j+1])
            num = int(order[j+2])

            lst = order[j+3:j+3+num]
            for k in range(len(lst)-1,-1,-1):
                original.insert(loc, lst[k])


    print("#{} {} {} {} {} {} {} {} {} {} {}".format(i+1, *original[:10]))
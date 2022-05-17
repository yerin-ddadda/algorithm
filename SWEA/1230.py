for i in range(10):
    n = int(input())
    test = list(map(int, input().split()))
    cnt = int(input())
    order = list(input().split())

    for j in range(len(order)):
        if order[j] == "I":
            loc = int(order[j+1])
            time = order[j+2]
            new = order[j+3:j+3+int(time)]

            for k in range(len(new)-1,-1,-1):
                test.insert(loc, int(new[k]))
            # print(test)

        elif order[j] == "D":
            x = int(order[j+1])
            y = int(order[j+2]) #D 1100 5
            del test[x:x+y]
            # print(test)

        elif order[j] == "A":
            y = int(order[j+1])
            # print(order[j+2:j+2+y])
            new = order[j+2:j+2+y]
            test.extend(new)
            # print(test)
        

    print("#{} {} {} {} {} {} {} {} {} {} {}".format(i+1, *test))
            
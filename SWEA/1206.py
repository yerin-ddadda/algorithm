for i in range(10):
    num = int(input())
    buildings = list(map(int,input().split()))

    sum = 0
    for j in range(2,num-2):
        min_num = 256
        if buildings[j-1] < buildings[j] and buildings[j-2] < buildings[j] and buildings[j+1] < buildings[j] and buildings[j+2] < buildings[j]:
            k = [-1,-2,1,2]
            for a in range(4):
                # print(buildings[j]-buildings[j-k[a]])
                if min_num > buildings[j]-buildings[j-k[a]]:
                    min_num = buildings[j]-buildings[j-k[a]]
            sum+=min_num
    print("#{0} {1}".format(i+1,sum))
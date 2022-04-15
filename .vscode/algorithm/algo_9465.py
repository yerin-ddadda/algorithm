T = int(input())


for i in range(T):
    n = int(input())
    sticker = []

    lst = []
    for i in range(n+1):
        lst.append(int(0))
    sticker.append(lst)

    for i in range(1):
        for j in range(2):
            number = input()
            lst2 = number.split(" ")
            lst2.insert(0,0)
            sticker.append(lst2)

    for i in range(3):
        for j in range(n+1):
            sticker[i][j]=int(sticker[i][j])

    # print(sticker)

    for j in range(1,n+1):
        sticker[0][j] += max(sticker[1][j-1], sticker[2][j-1])
        sticker[1][j] += max(sticker[0][j-1], sticker[2][j-1])
        sticker[2][j] += max(sticker[0][j-1], sticker[1][j-1])
        # print(sticker)
    # print(sticker)

    print(max(sticker[0][n], sticker[1][n], sticker[2][n]))
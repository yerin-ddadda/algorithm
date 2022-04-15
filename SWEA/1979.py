
T = int(input())

for z in range(T):
    N,K = map(int, input().split())
    answer = 0

    horizantal_board = []
    length_board = []
    for i in range(N):
        a = input()
        length_board.append(a.split())
        horizantal_board.append(a)

    length = []
    for i in range(N):
        append_list = []
        for j in range(N):
            append_list.append(length_board[j][i])
        line = "".join(append_list)
        line = line.split("0")
        for j in range(len(line)):
            if line[j].count('1') == K:
                answer +=1

    horizontal = []
    for i in range(len(horizantal_board)):
        line=horizantal_board[i].replace(" ","")
        line = line.split('0')
        for j in range(len(line)):
            if line[j].count('1') == K:
                answer +=1

    print("#{0} {1}".format(z+1,answer))

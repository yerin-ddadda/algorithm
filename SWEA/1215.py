for i in range(10):
    length = int(input())
    board = []
    for _ in range(8):
        board.append((input()))
    
    
    tot=0
    for a in range(8):
        string = board[a]
        for b in range(8):
            new = string[b:b+length]
            cnt=0
            if (len(new)) == length:
                for c in range(length):
                    if new[c] == new[-(c+1)]:
                        cnt+=1
                if cnt==length:
                    tot+=1

    board2 = []
    for a in range(8):
        ap =''
        for b in range(8):
            ap+=board[b][a]
        board2.append(ap)

    for a in range(8):
        string = board2[a]
        for b in range(8):
            new = string[b:b+length]
            cnt=0
            if (len(new)) == length:
                for c in range(length):
                    if new[c] == new[-(c+1)]:
                        cnt+=1
                if cnt==length:
                    tot+=1                    

    print("#{0} {1}".format(i+1,tot))
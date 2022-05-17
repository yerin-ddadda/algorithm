for i in range(10):
    num = int(input())
    board = [input() for _ in range(100)]
    
    max_len = 0
    for k in range(100):
        for a in range(100):
            for b in range(100,-1,-1):
                string = board[k][a:b]
                if string[:] == string[::-1]:
                    if max_len < len(string):
                        max_len = len(string)
                    break   


    for k in range(100):
        for a in range(100,-1,-1):
            for b in range(100):
                string = board[k][b:a]
                if string[:] == string[::-1]:
                    if max_len < len(string):
                        max_len = len(string)
                    break     


    k=''
    for a in range(100):
        for b in range(100):
            k+=board[b][a]
 
        for j in range(100):
            for z in range(100,-1,-1):
                string = k[j:z]
                if string[:] == string[::-1]:
                    if max_len < len(string):
                        max_len = len(string)
                    break
        for j in range(100,-1,-1):
            for z in range(100):
                string = k[j:z]
                if string[:] == string[::-1]:
                    if max_len < len(string):
                        max_len = len(string)
                    break


        k=""

    print("#{} {}".format(i+1,max_len))

# string = 'cbabbccc'
# print(string[0:7])
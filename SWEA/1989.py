T = int(input())

for i in range(T):
    input_str = list(input())
    cnt=0
    number = -1
    for j in range(len(input_str)):

        if input_str[j] == input_str[0+number]:
            cnt+=1
        number -=1

    if cnt== len(input_str):
        print("#", i+1, " ", 1,sep="")
    else:
        print("#", i+1, " ", 0,sep="")
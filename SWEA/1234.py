for j in range(10):
    length, lst = input().split()
    lst = list(lst)
    flag = True
    i=0
    while flag:   
        if lst[i] == lst[i+1]:
            del lst[i:i+2]
            i=0
        else:
            i+=1
        
        if i==len(lst)-1:
            flag=False
            break
    
    print("#{}".format(j+1),end=" ")
    print(*lst,sep="")

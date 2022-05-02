import sys
n=int(sys.stdin.readline())
lst = [int(sys.stdin.readline().strip()) for i in range(n)]
dasom = lst[0]
if len(lst)>1:
    num_list = lst[1:]
    max_num = max(num_list)
cnt=0
if len(lst)>1:
    while max(num_list) > dasom:
        data = num_list.index(max(num_list))
        dasom+=1
        cnt+=1
        num_list[data]-=1

    flag=True
    for i in num_list:
        if i == dasom:
            flag=False
else:
    cnt=0
    flag=True

if flag==False:
    print(cnt+1)
else:
    print(cnt)
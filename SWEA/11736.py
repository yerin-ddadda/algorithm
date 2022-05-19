tc = int(input())
for k in range(tc):
    num = int(input())
    num_lst = list(map(int, input().split()))

    cnt=0
    for i in range(1,num-1):
        max_num = max(num_lst[i-1:i+2])
        min_num = min(num_lst[i-1:i+2])
        if num_lst[i] != max_num and num_lst[i] != min_num:
            cnt+=1
    print("#{} {}".format(k+1,cnt))
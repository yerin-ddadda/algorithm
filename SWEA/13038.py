tc = int(input())

for i in range(tc):
    n = int(input())
    info = list(map(int, input().split()))
    cnt_lst = []

    for a in range(7):
        cnt2 = 0
        b = a
        cnt1 = 0
        while cnt2 < n:
            if info[b] == 1:
                cnt2+=1
            b+=1
            cnt1+=1
            if b == 7:
                b=0
        cnt_lst.append(cnt1)
    print("#{} {}".format(i+1,min(cnt_lst)))
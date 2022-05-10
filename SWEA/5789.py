t=int(input())
for i in range(t):
    n,q = map(int,input().split())
    n_lst = [0 for _ in range(n)]
    for a in range(q):
        l,r = map(int,input().split())
        for b in range(l-1,r):
            n_lst[b] = a+1
    
    print("#{0}".format(i+1), end=" ")
    for k in range(len(n_lst)):
        print(n_lst[k],end=" ")
    print()
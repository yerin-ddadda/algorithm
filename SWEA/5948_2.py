t=int(input())
for i in range(t):
    lst = list(map(int, input().split()))
    sumls = []
    for a in range(len(lst)):
        for b in range(a+1, len(lst)):
            for c in range(b+1, len(lst)):
                sumls.append(lst[a]+lst[b]+lst[c])

    sumls = list(set(sumls))
    sumls.sort(reverse=True)
    print(sumls[4])
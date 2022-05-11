from itertools import combinations
t=int(input())
for i in range(t):
    lst = list(map(int, input().split()))
    lst2 = list(combinations(lst, 3))

    sums=[]
    for j in range(len(lst2)):
        sums.append(sum(lst2[j]))
    sums = list(set(sums))
    sums.sort(reverse=True)

    print("#{0} {1}".format(i+1,sums[4]))
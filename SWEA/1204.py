t = int(input())

for i in range(t):
    dic={}

    n = int(input())

    lst=list(map(int,input().split()))
 
    for j in range(len(lst)):
        if lst[j] in dic:
            dic[lst[j]] += 1
        else:
            dic[lst[j]] = 1
    max_key = max(dic, key=dic.get)
    print("#{0} {1}".format(i+1,max_key))
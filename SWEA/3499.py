t = int(input())
for i in range(t):
    n = int(input())
    deq = list(input().split())
    d1=[]
    d2=[]
    new_d = []
    if n%2==0:
        d1=deq[0:n//2]
        d2=deq[n//2:]
        for j in range(n//2):
            new_d.append(d1[j])
            new_d.append(d2[j])
    else:
        d1=deq[0:n//2+1]
        d2=deq[n//2+1:]
        d2.append('')
        for j in range(n//2+1):
            new_d.append(d1[j])
            new_d.append(d2[j])
    
    
    
    print("#{0}".format(i+1), end=" ")
    for k in range(len(new_d)):
        print(new_d[k],end=" ")
    print()

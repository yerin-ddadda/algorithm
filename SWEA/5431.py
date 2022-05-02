t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    did = list(map(int,input().split()))
    didnot = []
    tmp = [a for a in range(1,n+1)]
    for a in tmp:
        if a not in did:
            didnot.append(a)
        else:
            continue
    didnot.sort()
    print("#",i+1,end=" ",sep="")
    for b in range(len(didnot)):
        print(didnot[b],end=" ")
    print()
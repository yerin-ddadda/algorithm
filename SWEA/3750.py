t=int(input())
res = []
for i in range(t):
    n=int(input())
    sum=n
    
    n = str(n)
    while len(n) != 1:
        sum=0
        for j in range(len(n)):
            sum+=int(n[j])
        n=str(sum)
    res.append(n)

for i in range(len(res)):
    print("#{0} {1}".format(i+1, res[i]))
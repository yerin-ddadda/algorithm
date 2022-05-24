t = int(input())
for i in range(t):
    a,b,c = map(int, input().split())
    if a==b:
        res = c
    elif b==c:
        res = a
    elif a==c:
        res = b

    print("#{} {}".format(i+1, res))
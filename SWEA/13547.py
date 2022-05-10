t = int(input())
for i in range(t):
    s = list(input())
    if s.count('x') >= 8:
        print("#{0} {1}".format(i+1, "NO"))
    else:
        print("#{0} {1}".format(i+1, "YES"))
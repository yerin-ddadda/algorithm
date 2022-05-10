t=int(input())
for i in range(t):
    string=input()
    set_string = set(string)

    res = []

    for j in range(len(set_string)):

        a = string.count(list(set_string)[j])
        if a%2==1:
            res.append(list(set_string)[j])

    if len(res) == 0:
        res = "Good"
        print("#{0} {1}".format(i+1,res))
    else:
        res.sort()
        print("#{0}".format(i+1),end=" ")
        for k in range(len(res)):
            print(res[k],end="")
        print()
    

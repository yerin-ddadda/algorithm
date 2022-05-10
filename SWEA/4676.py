t=int(input())
for i in range(t):
    string = list(input())
    h = int(input())
    h_lst = list(map(int,input().split()))
    h_lst.sort(reverse=True)
 
    for j in range(h):
        string.insert(h_lst[j],"-")
    print("#{0}".format(i+1),end=" ")
    for k in range(len(string)):
        print(string[k],end="")
    print()
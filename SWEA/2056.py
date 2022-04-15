from os import sep


T = int(input())
testcase = [list(map(str,input().split())) for _ in range(T)]
list_31 = [1,3,5,7,8,10,12]
list_30 = [4,6,9,11]

for i in range(len(testcase)):
    a = ("".join(testcase[i]))

    if a[5] in list_31:
        if 1>=int(a[6:]) or 31<int(a[6:]):
           print("#", end="")
           print(i+1,end=" ")
           print(-1) 

    elif a[5] in list_30:
        if 1>=a[6:] or 30<a[6:]:
            print("#", end="")
            print(i+1,end=" ")
            print(-1) 

    elif a[5] == str(2):
        if int(a[6:])<1 or int(a[6:])>28:
            print("#", end="")
            print(i+1,end=" ")
            print(-1)
        else:
            print("#", end="")
            print(i+1,end=" ")
            print(a[0:4],"/",a[4:6],"/",a[6:],sep="")
            
    elif int(a[5])<1 or int(a[5])>12:
        print("#", end="")
        print(i+1,end=" ")
        print(-1)
    else:
        print("#", end="")
        print(i+1,end=" ")
        print(a[0:4],"/",a[4:6],"/",a[6:],sep="" ) 
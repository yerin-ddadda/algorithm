n=int(input())
lst = list(map(int,input().split()))
lst.sort()

a,b = divmod(len(lst),2)

print(lst[a+b-1])
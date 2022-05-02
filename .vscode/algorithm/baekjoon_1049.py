n,m = map(int, input().split())

min_pack=1000
min_indiv=1000

for i in range(m):
    pack, indiv = map(int, input().split())
    
    if min_pack > pack:
        min_pack = pack
    if min_indiv > indiv:
        min_indiv = indiv

if n>6:
    a = (n//6+1)*min_pack   
else:
    a = min_pack

b = min_indiv * n

if n>6:
    c = ((n//6)*min_pack)+ min_indiv * (n-(6*(n//6)))
else:
    c = 1000
print(min(a,b,c))



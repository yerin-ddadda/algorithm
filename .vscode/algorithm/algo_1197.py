from sys import stdin
read = stdin.readline
v,s = map(int, read().split())

edge = []
for _ in range(s):
    a,b,w = map(int, read().split())
    edge.append((w,a,b))

edge.sort(key=lambda x:x[0])
parent = list(range(v+1))

def union(a,b):
    a = find(a)
    b = find(b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

def find(a):
    if parent[a] != a:
        return find(parent[a])
    return a

sum=0
for w,s,e in edge:
    if find(s) != find(e):
        union(s,e)
        sum+=w
print(sum)
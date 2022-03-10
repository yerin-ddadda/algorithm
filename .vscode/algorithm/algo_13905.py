from sys import stdin
read = stdin.readline
n,m= map(int, read().split())
s,e = map(int, read().split())

edge =[]
for _ in range(m):
    a,b,c = map(int, read().split())
    edge.append((c,a,b))

edge.sort(key=lambda x:-x[0])
print(edge)
parent = list(range(n+1))

def find(a):
    if parent[a] != a:
        # return find(parent[a])
        parent[a] = find(parent[a])
        return parent[a]
    else:
        return a

def union(a,b):
    a = find(a)
    b = find(b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b


count=0
min_weight=0
for c,a,b in edge:
    if find(s) != find(e):
        min_weight = c
        union(a,b)


def find_parent(a):
    return parent[a]

# print(parent)

if find_parent(s) != find_parent(e):
    min_weight=0   
print(min_weight)

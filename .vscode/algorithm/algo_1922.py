from sys import stdin
read = stdin.readline
v = int(input()) #노드의 개수
s = int(input()) #간선의 개수

edge = []

for _ in range(s):
    a,b,c = map(int, read().split())
    edge.append((c,a,b))


edge.sort(key=lambda x:x[0])


parent = list(range(v+1))


#부모 노드 찾기
def find_parent(x):
    if parent[x] != x:
        return find_parent(parent[x])
    else:
        return x

def union(b,c):
    b = find_parent(b)
    c = find_parent(c)
    if b<c:
        parent[b] = c
    else:
        parent[c] = b


sum = 0
for a,b,c in edge:
    if find_parent(b) != find_parent(c):
        union(b,c)
        sum+=a
print(sum)
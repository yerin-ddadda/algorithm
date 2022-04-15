#초기화
parent = [i for i in range(5)]
#1차원 배열을 사용해서 n개의 원소가 서로 다른 집합에 속하도록 한다.

#find
def find(x):
    if x == parent[x]:
        return x
    else:
        return find[parent[x]] 
# 노드x가 어느 집합에 속하는지 찾는 연산(x의 루트 찾기)
#x==parent[x]면 x가 부모노드
#그렇지 않다면 재귀호출을 사용해 루트를 찾아 반환

# #find를 최적화한 코드
# def find(a):
#     if a == find[a]:
#         return a
#     parent[a]=find(parent[a])
#     return parent[a]
# #경로 압축한 find 함수 -> a의 루트를 저장해두면 찾기 연산의 중복을 피할 수 있음

#Union
def union(a,b):
    a=find(a)
    b=find(b)

    if a !=b:
        if b<a:
            parent[a]=b
        else:
            parent[b]=a
#노드 a가 속한 집합과 노드 b가 속한 집합을 합치는 연산
#find 함수를 통해 찾은 a와 b의 루트 노드의 값을 비교한다.
#높이가 더 낮은 트리를 더 높은 트리 밑에 넣어서 합친다.            
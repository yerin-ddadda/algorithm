from math import inf

def prim(start):
    global N, adj_mat
    # visited_set: 현재까지 방문한 정점들의 집합
    visited_set = set()
    visited_set.add(start)
    distance = 0

    #N-1개의 간선을 선택할 때까지 반복한다.
    for _ in range(N-1):
        #min_dist:현재 방문한 정점에서 갈 수 있는 간선의 최단 거리
        #next_node: 현재 방문한 정점에서 최단 거리로 갈 수 있는 정점
        min_dist, next_node = inf, -1

        #현재까지 방문한 모든 정점에 대하여
        for node in visited_set:
            #해당 정점과 연결되어 있고 아직 방문하지 않은 모든 정점 중
            #소요 비용이 가장 작은 정점을 찾는다.
            for j in range(1, N+1):
                if j not in visited_set and 0<adj_mat[node][j]<min_dist:
                    min_dist = adj_mat[node][j]
                    next_node = j
            
        distance += min_dist
        visited_set.add(next_node)
    return distance

N, M = map(int, input().split())
adj_mat = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    x,y,value = map(int, input().split())
    adj_mat[x][y] = value
    adj_mat[y][x] = value
#1번 정점에서 탐색을 시작
print(prim(1))
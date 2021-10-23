from collections import deque

N,K = map(int,input().split())

queue = deque()
for i in range(1,N+1):
    queue.append(i)
print(queue)

result = []
count=0

while queue:
    for i in range(K-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())
print("<", ", ".join(str(i) for i in result), ">" ,sep="")
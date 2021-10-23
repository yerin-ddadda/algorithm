N, K = map(int, input().split())
josephus = [i for i in range(1,N+1)]

count=0
result = []
while len(josephus):
    a = josephus.pop(0)
    count+=1

    if count<K:
        josephus.append(a)

    else:
        result.append(a)
        count=0
    
print("<", ', '.join(str(i) for i in result), ">", sep = '')

# from collections import deque

# queue = deque()
# answer = []

# N, K = map(int, input().split())

# queue = [i for i in range(1, N+1)]

# print(queue)

# while queue:
#     for i in range(K-1):
#         queue.append(queue.popleft())
#     answer.append(queue.popleft())
# print("<", ", ".join(str(i) for i in answer), ">", sep="")


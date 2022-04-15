import sys
from collections import defaultdict
input = sys.stdin.readline
N, d, k, c = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(int(input()))
arr += arr[:k-1]

left=0
right=0
max_num = 0

caneat = defaultdict(int)
caneat[c] +=1

for right in range(len(arr)):
    caneat[arr[right]]+=1

    if right>=k-1:
        max_num = max(max_num, len(caneat))
        caneat[arr[left]]-=1
        if caneat[arr[left]]==0:
            del caneat[arr[left]]
        left+=1
print(max_num)
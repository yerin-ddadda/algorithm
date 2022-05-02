import sys
import heapq as hq
n=int(sys.stdin.readline())

lst = []
cnt=0
while cnt<n:
    num = int(sys.stdin.readline())
    cnt+=1
    if num == 0:
        if len(lst)==0:
            print(0)
        else:
            print(hq.heappop(lst))
    else:
        hq.heappush(lst, num)
    
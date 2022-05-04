import sys
n=int(sys.stdin.readline())
lst =[int(sys.stdin.readline().strip()) for _ in range(n)]

lst.sort()

dissatisfaction = 0

for i in range(n):
    dissatisfaction+=abs(lst[i]-(i+1))

print(dissatisfaction)

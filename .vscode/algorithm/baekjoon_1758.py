import sys
n = int(input())
tip=0
tips=[]
for i in range(n):
    tip = int(sys.stdin.readline())
    tips.append(tip)

tips.sort(reverse=True)

rank=0
for i in range(n):
    if tips[i]-(i+1-1)<0:
        continue
    else:
        rank+=(tips[i]-(i+1-1))

print(rank)


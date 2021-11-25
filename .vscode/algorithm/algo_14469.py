import sys

number = int(input())
cows= []

for i in range(number):
    cows.append(list(map(int, sys.stdin.readline().split())))
cows.sort()


time = 0
for i in range(number):
    x,y = cows[i]
    if time > cows[i][0]:
        time += y
    
    else:
        time = x+y
print(time)
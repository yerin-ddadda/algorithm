T = int(input())
ab_list = [list(map(int, input().split())) for _ in range(T)]

for i in range(T):
    a = ab_list[i][0]
    b = ab_list[i][1]
    print("#", i+1, sep="", end=" ")
    print(a//b, a%b)
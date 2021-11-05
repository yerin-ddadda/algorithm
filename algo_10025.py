import sys
input = sys.stdin.readline
N,K = map(int, input().split())
whitebear_list = [0] * 1000001
end = 0

for _ in range(N):
    g, x = map(int, input().split())
    whitebear_list[x] = g
    end = max(end, x)

step = 2*K+1
window = sum(whitebear_list[:step])
print(window, "window", step, "step")
answer = window


for i in range(step, end+1):
    window += whitebear_list[i] - whitebear_list[i-step]
    answer = max(answer, window)
print(answer)
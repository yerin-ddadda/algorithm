X, Y = map(int, input().split())
warmth = 0
moisture = 0
print_sum = 0

print_sum = X + Y
if X>Y:
    print_sum += Y//10
    print(print_sum)
else:
    print_sum += X//10
    print(print_sum)
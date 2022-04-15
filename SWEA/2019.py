n = int(input())

num_list = []
for i in range(10):
    
    if i>=3:
        num_list.append(num_list[i-1]*2)
    else:
        num_list.append(i)
for i in range(1,10):
    print(num_list[i], end=" ")
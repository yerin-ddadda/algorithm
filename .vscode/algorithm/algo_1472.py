data = list(input())

for i in range(len(data)):
    data[i] = int(data[i])
data.sort(reverse=True)

for i in data:
    print(i, end="")


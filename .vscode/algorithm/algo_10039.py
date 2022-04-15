jumsu = []
avg = 0

for i in range(5):
    a = int(input())
    jumsu.append(a)
    if a >= 40:
        pass
    else:
        jumsu[i] = 40

avg = (sum(jumsu) / len(jumsu))

print(int(avg))
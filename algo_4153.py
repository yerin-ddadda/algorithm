pita_print = []

while True:
    a, b, c = map(int, input().split())
    if a ==0 and b ==0 and c==0 :
        break
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
        pita_print.append("right")
    else:
        pita_print.append("wrong")

for i in range(len(pita_print)):
    print(pita_print[i])

# 5 4 3 
# 4 3 5
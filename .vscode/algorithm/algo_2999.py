word = list(input())

N = len(word)
R = 0
C = 0

make_row = []
make_index = []
for i in range(1,N):
    if  N%i==0:
        if i <= N//i:
            R = i
            C = N // i

for i in range(R):
    make_row=[]
    for j in range(C):
        make_row.append(0)
    make_index.append(make_row)


count = 0
for i in range(C):
    for j in range(R):
        make_index[j][i] = word[count]

        count +=1

print_index = []
for i in range(R):
    for j in range(C):
       print_index.append(make_index[i][j])

for i in range(len(word)):
    print(print_index[i],end="")
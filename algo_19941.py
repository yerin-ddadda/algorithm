N, K = map(int, input().split())
ham_and_per = []
back_and_forth = []

for i in range(-K,K+1):
    back_and_forth.append(i)

count=0

char = input()
for i in range(N):
    ham_and_per.append(char[i])


for i in range(N):
    if ham_and_per[i] == 'P':
        for j in back_and_forth:
            if i+j>=N:
                break
            elif 0<=i+j<N and ham_and_per[i+j]=="H":
                count+=1
                ham_and_per[i+j]=0
                # print(ham_and_per)
                break
                
print(count)

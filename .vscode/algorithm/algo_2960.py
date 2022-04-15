n,k = map(int, input().split())

n_list = []
check_list = []
count =0
answer = 0

for i in range(2,n+1):
    n_list.append(i)


count=0
for i in range(len(n_list)):
    
    for j in range(i,len(n_list),n_list[i]):
        if n_list[j] not in check_list:
            check_list.append(n_list[j])
           
            count+=1
            if count==k:
                answer = check_list[k-1]
print(answer)
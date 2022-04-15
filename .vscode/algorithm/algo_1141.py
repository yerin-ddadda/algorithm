number = int(input())
prefix = []
for i in range(number):
    char = input()
    prefix.append(char)
prefix.sort(reverse=False)

list = []

flag= 0

for i in range(number):
    flag= False
    for j in range(i+1, number):
        if prefix[j].startswith(prefix[i]):
            flag = True
            
    if flag==False:
        list.append(prefix[i])
print(len(list))
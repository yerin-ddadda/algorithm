num = int(input())
subst = [num]
max_len = 0
max_list = []
res = [i for i in range(0,num+1)]
# print(res)
for i in range(len(res)):
    select_num = res[i]

    result = 0
    subst.append(num - select_num)
    j=0
    while result >= 0:
        
        result = subst[j] - subst[j+1]
        if result < 0:
            break
        else:
            subst.append(result)
        j+=1
    if max_len < len(subst):
        max_len = len(subst)
        max_list = subst
    subst = [num]
print(max_len)
for i in range(len(max_list)):
    print(max_list[i], end= " ")

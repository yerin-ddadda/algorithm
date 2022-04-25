string=input()
lst =[]
div=''
for i in range(len(string)):
    if i==len(string)-1:
        div+=string[i]
        lst.append(div)
        break

    if string[i]==string[i+1]:
        div+=string[i]
    else:
        div+=string[i]
        lst.append(div)
        div=''

zero_cnt=0
one_cnt=0
ans_list = []
for i in range(len(lst)):
    if lst[i].startswith('0'):
        zero_cnt+=1
    else:
        one_cnt+=1
ans_list.append(zero_cnt)
ans_list.append(one_cnt)
print(min(ans_list))
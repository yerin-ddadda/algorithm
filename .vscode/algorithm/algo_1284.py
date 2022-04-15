cm_lst = []
number = 0
num_lst = []

while True:
    cm = int(input())
    if cm == 0:
        break
    for i in str(cm):
       cm_lst.append(i)

    for i in range(len(cm_lst)):
        if cm_lst[i] == '1':
            number +=2
        elif cm_lst[i] == '0':
            number += 4
        else:
            number += 3

    number = number + len(cm_lst)-1 + 2
    num_lst.append(number)
    number = 0
    cm_lst = []

for i in range(len(num_lst)):
    print(num_lst[i])
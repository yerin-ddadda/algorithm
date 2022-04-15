import sys
n = int(input())
p = sys.stdin.readline().split()
s = sys.stdin.readline().split()

count=0

will_change_list = []
compare_list = []
tmp =[]

for i in range(n):
  will_change_list.append('0')
  tmp.append('0')

for i in range(n//3):
  compare_list.append('0')
  compare_list.append('1')
  compare_list.append('2')


for j in range(3):
  for i in range(n):
    print("s",s)
    print("p",p)
    print("will_change_list",will_change_list)
    will_change_list[int(s[i])]=int(p[i])
    print(i, p,p[i],"뭐니 시발")
    print("반복",will_change_list)

  print(will_change_list)
  
  
  print("")

  if compare_list==will_change_list:
    print("lala", count)
    break

  else: 
    #0,1,2,0,1,2.. 랑 바꾼게 같지않다면
    count+=1
  p=will_change_list
print(count)
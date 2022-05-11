t = int(input())
num = [i for i in range(1,10)]
x = []
for i in range(len(num)):
    for j in range(len(num)):
        x.append(num[i]*num[j])
  
for i in range(t):
    n = int(input())

    if n in x:
        res = "Yes"
        print("#{0} {1}".format(i+1, res))
    else:
        res = "No"
        print("#{0} {1}".format(i+1, res))

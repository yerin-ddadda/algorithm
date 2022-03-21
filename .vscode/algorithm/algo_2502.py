d,k=map(int,input().split())
# print(day)

# day[0][0] = 1
# day[0][1] = 0
# day[1][0] = 0
# day[1][1] = 1
# for i in range(2,d+1):
#     for j in range(2,d+1):
#         day[i][0] = day[i-1][0]+day[i-2][0]
#         day[i][1] = day[i-1][1]+day[i-2][1]
# print(day)        

# for i in range(k):
#     for j in range(k):
#         if i<=j and day[]:
#             if day[d-1][0]*i + day[d-1][1]*j == k:
#                 print(i)
#                 print(j)
x=1
y=0  
for i in range(d-1):
    x, y = y, x+y
for a in range(1,100000):
    if (k-(x*a))%y == 0:
        
        print(a, (k-(x*a))//y, sep="\n")
        break

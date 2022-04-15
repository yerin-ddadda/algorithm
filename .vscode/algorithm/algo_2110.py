n,c = map(int, input().split())
house = []
for i in range(5):
    j = int(input())
    house.append(j)
print(house)

house.sort()
start=0
end=house[-1]

while start<=end:
    count=0
    mid = (start+end)//2
    for i in range(house):
        if i>mid:
            count+=1
    if count<c:
        start=mid+1
    
        

s=int(input())
a=1
cnt=0
sum=0
while True:
    if sum>s:
        cnt-=1
        print(cnt)
        break
    sum+=a 
    a+=1
    cnt+=1
    
n = int(input())
sticker_state=[False] * 111111
turn = list(map(int,input().split()))

count=0
max_num = 0

for i in turn:
    if not sticker_state[i]:
        sticker_state[i] = True
        count+=1
        
    else:
        sticker_state[i] = False
        count-=1

    max_num = max(max_num,count)
print(max_num)


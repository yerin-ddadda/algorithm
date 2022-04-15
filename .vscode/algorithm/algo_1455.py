row, column = map(int, input().split())
coin_list = []
count= 0

def reverse(x,y):
    # print("함수 들어옴")
    for i in range(y+1):
        for j in range(x+1):
            if coin_list[i][j] == 1:
                coin_list[i][j] = 0
            else:
                coin_list[i][j] = 1


for i in range(row):
    append_list = []
    char = input()
    for i in range(column):
        append_list.append(int(char[i]))
    coin_list.append(append_list)
# print(coin_list)

count=0
# print(coin_list[1][1])

for i in range(row-1,-1,-1):
    # print(i)
    for j in range(column-1,-1,-1):
        # print(type(coin_list[i][j]),"1인가?")
        if coin_list[i][j] == 1:
            # print("1이다")
            reverse(j,i)
            count+=1

print(count)


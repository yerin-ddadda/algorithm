test_case = int(input())
for i in range(test_case):
    floor = int(input())
    ho = int(input())

boonyeo_house = []
row_num = 4
col_num = 15
for row in range(1,row_num):
    boonyeo_house.append([])
    for col in range(1,col_num):
        boonyeo_house[row][col] = boonyeo_house[row-1][col] + boonyeo_house[row][col-1]
        boonyeo_house[row].append(boonyeo_house[row][col])


for row in range(row_num):
    for col in range(col_num):
        print(boonyeo_house[row][col], end=' ')
    print()

for i in range(0,row_num):
    for j in range(0,col_num):
        boonyeo_house[i][0] = 0
        boonyeo_house[i][1] = 1
        boonyeo_house[i][j] = boonyeo_house[i][j-1] + boonyeo_house[i-1][j]
        a=boonyeo_house[i][j]
        boonyeo_house.append(a)
        print(boonyeo_house)

print(boonyeo_house )


# 3층 : 1 5 15 35 70 111 159 
# 2층 : 1 4 10 20 35 41  48 56 65 75
# 1층 : 1 3 6  10 15 21  28 36 (n호 : )
# 0층 : 1 2 3  4  5  6   7 ... (n호 : n명 살고있음)

# 1층의 3호 = 0층의 6호
# 2층의 3호 = 1층의 4호
# 3층의 2호 = 0층의 5호
# 3층의 3호 = 1층의 5호
# 3층의 4호 = 2층의 5호

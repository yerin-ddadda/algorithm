word1, word2 = input().split()

good_list = [] #일단 점으로 채워넣은 리스트
remember = [] #두 단어 비교해서 word2 어디에 있는지

col_num = len(word2)
row_num = len(word1)

for i in range(col_num): #일단 row_num행 col_num로 "."으로 채워넣기
    good_list.append([])
    for j in range(row_num):
        good_list[i].append(".")

for i in range(row_num):
    for j in range(col_num):
        if word1[i] == word2[j]: #일단 word1의 단어하나가 word2어디에 있는지 알아내기
            remember.append(i)
            remember.append(j)
            break
    if len(remember)>1:
        break


        
            #각 행의 i번째에 돌아가는 j를 출력해야함
for i in range(col_num):
    good_list[i][remember[0]]= word2[i]

for i in range(row_num): #
    good_list[remember[1]][i] = word1[i]


for i in range(len(good_list)):
    for j in range(len(good_list[0])):
        print(good_list[i][j], end="")
    print()

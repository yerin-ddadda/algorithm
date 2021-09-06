test_case = int(input())

floor_list = []
ho_list = []

for i in range(test_case):
    floor = int(input())
    floor_list.append(floor)
    ho = int(input())
    ho_list.append(ho)

boonyeo_house = []
i=0 



for i in range(1):
    boonyeo_house.append([])
    for j in range(15):
        boonyeo_house[i].append(j)



for i in range(1,15): #일단 row_num행 col_num로 "."으로 채워넣기
    boonyeo_house.append([])
    for j in range(1):
        boonyeo_house[i].append(0)
        for k in range(15):
            boonyeo_house[i].append(1)


#for i in range(1,15):
 #   boonyeo_house.append([])
  #  for j in range(15):
   #     boonyeo_house[i].append(1)



for i in range(1,15):
    for j in range(1,15):
        boonyeo_house[i][j] = boonyeo_house[i-1][j] + boonyeo_house[i][j-1]


for i in range(test_case):
    print(boonyeo_house[floor_list[i]][ho_list[i]])
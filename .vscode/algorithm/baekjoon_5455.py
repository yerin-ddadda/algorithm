import sys

n=int(input()) #토핑의수
a,b =map(int, input().split()) #도우 가격 a , 토핑 가격 b
c = int(input()) # 도우 열량
topping_calories =  [int(sys.stdin.readline().strip()) for i in range(n)]#각 토핑의 열량
topping_calories.sort(reverse=True)
# print(topping_calories)

# 1번: 일단 도우의 1원당 열량을 계산한다.
dough_calorie = c//a
# print(dough_calorie)

topping_calories_lst = []
# 2번 : 각 토핑의 1원당 열량을 계산한다.
re_cal = 0

for i in topping_calories:
    # print(i//b)
    price=0
    cal=0
    if i//b>dough_calorie and re_cal < i//b:
        topping_calories_lst.append(i)
        #도우 열량보다 크니까 합쳐서 다시 계산
        for j in range(len(topping_calories_lst)):
            price += b
            cal += topping_calories_lst[j]
        re_cal = (cal+c)//(price+a)
    # print(topping_calories_lst)

if re_cal == 0:
    re_cal = dough_calorie
    print(re_cal)
else:     
    print(re_cal)

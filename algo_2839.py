sugar = int(input())
bag = 0

while True:
    if sugar < 0:
        print(-1)
        break

    if sugar % 5 == 0:
        bag += sugar // 5
        print(bag)
        break
    else:
        sugar -= 3
        bag += 1
    


    



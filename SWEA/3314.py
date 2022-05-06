t = int(input())
for i in range(t):
    score = list(map(int,input().split()))
    
    sum = 0
    for j in range(len(score)):
        if score[j] < 40:
            score[j] = 40
            sum+=score[j]
        else:
            sum+=score[j]

    print("#{0} {1}".format(i+1, sum//5))
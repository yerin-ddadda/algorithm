T = int(input())

calend = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

for i in range(T):
    day_calc = 0
    fir_mon, fir_day, sec_mon, sec_day = map(int, input().split())

    day_sum = 0

    if fir_mon != sec_mon:
        for j in range(fir_mon+1, sec_mon):
            day_sum += calend[j]
            day_calc = (calend[fir_mon]-fir_day) + day_sum + sec_day + 1
    else:
        day_calc = fir_day + sec_day -1

    

    print("#{0} {1}".format(i+1,day_calc))
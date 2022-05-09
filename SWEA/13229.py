week = {"MON":1, "TUE":2, "WED":3, "THU":4, "FRI":5, "SAT":6,"SUN":7}
t = int(input())

for i in range(t):
    string = input()
    if string == "SUN":
        res = 7
    else:
        res = week["SUN"]-week[string]
    print("#{0} {1}".format(i+1,res))
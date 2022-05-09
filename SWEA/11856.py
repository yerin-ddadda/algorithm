t = int(input())
for i in range(t):
    string = input()
    dic = {}
    for j in range(len(string)):
        if string[j] in dic:
            dic[string[j]]+=1
        else:
            dic[string[j]] = 1
    # a_uniquie = ''.join(set(string))
    if len(dic.keys()) == 2:
        if dic[string[0]] == 2 and dic[string[1]] == 2:
            res = "Yes"
            print("#{0} {1}".format(i+1, res))
    else:
        res = 'No'
        print("#{0} {1}".format(i+1, res))
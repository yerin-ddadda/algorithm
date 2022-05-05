for i in range(10):
    n =  int(input())
    find_str = input()
    string = input()
    if find_str in string:
        string = string.replace(find_str, "!")

    cnt = string.count("!")
    print("#{0} {1}".format(i+1,cnt))
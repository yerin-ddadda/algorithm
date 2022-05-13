t = int(input())
for i in range(t):
    n = int(input()) #문장의 개수

    string = input()
    lst = []
    cnt_list = []

    start = 0
    for j in range(len(string)):
        cnt=0
        if string[j] in ("!","?","."):
            cnt=0
            for word in string[start:j].split():

                if word.isalpha() and word[0].isupper() and word[1:].islower():
                    cnt+=1
                if len(word) == 1 and word.isupper():
                    cnt+=1
            cnt_list.append(cnt)
            start = j+1
    
    print("#{0}".format(i+1),end=" ")
    for j in range(len(cnt_list)):
        print(cnt_list[j], end=" ")
    print()
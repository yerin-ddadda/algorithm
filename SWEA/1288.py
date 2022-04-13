T = int(input())
answer_list = []

def sheep(N):
    zero_nine = ['0','1','2','3','4','5','6','7','8','9']
    d = 1
    num_list = [char for char in N]

    while True:
        if len(zero_nine) != 0:
            big_N = d*int(N)
            num_list = [char for char in str(big_N)]
            set(num_list)

            for i in range(len(num_list)):
                if num_list[i] in zero_nine:
                    zero_nine.remove(num_list[i])

            if len(zero_nine) != 0:
                d+=1
                continue
        else:
            answer_list.append(big_N)
            return answer_list
            
for i in range(T):
    testcase = input()
    sheep(testcase)

for i in range(len(answer_list)):
    print("#",i+1, " " ,answer_list[i],sep="")
  
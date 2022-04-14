T = int(input())
sum_list = []

for k in range(T):
    
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    nm_list = [N,M]

    for i in range(max(nm_list)-min(nm_list)+1):
        number = 0
        sum_num = 0 
        if M>N:
            for j in B[i:i+N]:
                sum_num += (A[number] * j)
                number+=1
            sum_list.append(sum_num)
        else:
            for j in A[i:i+M]:
                sum_num += (B[number] * j)
                number+=1
            sum_list.append(sum_num)
    
    print("#", k+1," ", max(sum_list),sep="")
    sum_list = []
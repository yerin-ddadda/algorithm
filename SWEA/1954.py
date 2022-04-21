def makearr(size,arr):
    col = -1
    row = 0
    inc = 1
    value = 1
    while size>0:
        for _ in range(size):
            col+=inc
            arr[row][col] = value
            value+=1
        size -=1

        for _ in range(size):
            row+=inc
            arr[row][col] = value
            value +=1
        inc*=-1

def printarr(i,size,arr):
    print("#",i+1,sep="")
    for i in range(size):
        for j in range(size):
            
            print(arr[i][j], end= " ")
        print()

T = int(input())
for i in range(T):
    size = int(input())
    arr = [[0]*size for _ in range(size)]
    makearr(size,arr)
    printarr(i,size,arr)
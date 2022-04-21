# def printarr(side,arr):
#     for i in range(side):
#         print(arr[i])

# def makearr(side,arr):
#     inc = 1
#     value = 1
#     row = 0
#     col = -1

#     while (side>0):
#         for i in range(side):
#             col+=inc
#             arr[row][col] = value
       
#             value+=1
#         side-=1
#         for j in range(side):
#             row+=inc
#             arr[row][col] = value
         
#             value+=1
#         inc *= -1

# print("input side length of arr: ", end=" ")
# side = int(input())
# arr = [[0]*side for _ in range(side)]
# makearr(side,arr)
# printarr(side,arr)


side = int(input())
arr = [[0]*side for _ in range(side)]

def makearr(arr,side):
    col = -1
    row = 0
    inc = 1
    value = 1
    while side>0:
        
        for i in range(side):
            col+=inc
            arr[row][col] = value
            value+=1
            
        
        side-=1
        for j in range(side):
            row+=inc
            arr[row][col] = value
            value+=1
            
        inc *= -1

makearr(arr,side)
print(arr)
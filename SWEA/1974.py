T = int(input())
def same_line(sudoku):
    for i in range(len(sudoku)):
        check_list = []
        for j in range(len(sudoku[i])):
            if sudoku[i][j] not in check_list:
                check_list.append(sudoku[i][j])
            else:
                return 0

        if len(check_list) == 9:
            continue
    return 1
        

def square(sudoku):
    b = 0
    a = 0
    while a<9:
        while b<9:     
            check_list = []
            for i in range(a,a+3):      
                for j in range(b,b+3):
                    if sudoku[i][j] not in check_list:
                        check_list.append(sudoku[i][j])
                    else:
                        return 0
                        
                
                if len(check_list) == 9:
                    continue
            b+=3
        b=0
        a+=3
    return 1

def length(sudoku):
    for i in range(9):
        check_list = []
        for j in range(9):
            if sudoku[j][i] not in check_list:
                check_list.append(sudoku[j][i])
            else:
                return 0
            
        if len(check_list) == 9:
            continue
    return 1

for i in range(T):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    result = same_line(sudoku)
    if result == 0:
        print("#{0} {1}".format(i+1, result))
        continue
        
    else:
        result = square(sudoku)
        if result == 1:
            a = length(sudoku)
            if a==1:
                print("#{0} {1}".format(i+1, a))
            else:
                print("#{0} {1}".format(i+1, a))
        else:
            print("#{0} {1}".format(i+1, result))
        
        

    
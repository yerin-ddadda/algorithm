def solution(n, arr1, arr2):
    answer = []

    binary_arr1 = []
    binary_arr2 = []

    for i in range(n):
        binary_arr1.append(bin(arr1[i])[2:])
        binary_arr2.append(bin(arr2[i])[2:])

        if len(binary_arr1[i])<n or len(binary_arr2[i])<n:
            binary_arr1[i] = binary_arr1[i].rjust(n,"0")
            binary_arr2[i] = binary_arr2[i].rjust(n,"0")

    for i in range(n):
        string = ""
        for j in range(n):
            if int(binary_arr1[i][j]) or int(binary_arr2[i][j]):
                string += "#"
            else:
                string += " "
        answer.append(string)

    return answer

a = solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10])
print(a)

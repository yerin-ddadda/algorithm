# alphabet = input()
# alphabet_dic = {}

# for i in range(1,len(alphabet)+1):
#     alphabet_dic[alphabet[i-1]] = i

# for i in range(1, len(alphabet)+1):
#     print(alphabet_dic[alphabet[i-1]],end=" ")

for c in input():
    print(ord(c)-64, end=" ")
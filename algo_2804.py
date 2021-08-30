word1, word2 = input().split()
not_word = "."

for i in range(len(word1)):
    if word1[0][j] == word2[1][j]:
        print(word1)
    else:
        print(".", end="")
        print(word2[i], end="")
        
        j+=1
def dfs(level, beginWith):

    if level==r:
        print(result)
    else:
        for i in range(beginWith,len(n)):
            result[level]=n[i]
            dfs(level+1,i+1)


if __name__ == "__main__": #nCr
    n = [[1,2],[2,2],[4,4]]
    r = 2

    result = [0] *r

    dfs(0, 0) 

def dfs(L):
    #종료 조건
    if L==r:
        print(result)
    else:
        for i in range(len(n)):
            if checklist[i] == 0:
                result[L]=n[i]
                dfs(L+1)
                checklist[i]=0

if __name__ == "__main__":
    n = ["aa","bb","cc","dd"]
    r = 2 #몇개뽑을지

    result = [0] * r
    checklist = [0] * len(n)

    dfs(0)
n,m = map(int, input().split())
trees = list(map(int,input().split()))
start=0
end=max(trees)

result = []
while start<=end:
    slice_num=0
    mid=(start+end)//2

    slice_num = (sum(tree-mid if tree > mid else 0 for tree in trees))

    if slice_num == m:
        result.append(mid)
        break
    elif slice_num >m:
        result.append(mid)
        start = mid + 1
    else:
        end = mid - 1

print(max(result))
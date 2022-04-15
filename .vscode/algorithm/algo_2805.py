# n,m = map(int, input().split())
# trees = list(map(int,input().split()))
# start=0
# end=max(trees)

# result = []
# while start<=end:
#     slice_num=0
#     mid=(start+end)//2

#     slice_num = (sum(tree-mid if tree > mid else 0 for tree in trees))

#     if slice_num == m:
#         result.append(mid)
#         break
#     elif slice_num >m:
#         result.append(mid)
#         start = mid + 1
#     else:
#         end = mid - 1

# print(max(result))

n,m= map(int,input().split())
dduck = list(map(int,input().split()))

answer= []
start=0
end=max(dduck)
while start<=end:
    mid=(start+end)//2
    lst = sum(i-dduck if i>mid else 0 for i in dduck)
    if lst < m:
        end = mid-1
    else:
        answer=mid #최대한 덜 잘랐을때가 정답이므로
        start = mid + 1
print(answer)

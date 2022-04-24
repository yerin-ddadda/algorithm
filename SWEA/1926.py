n = int(input())
nums = [str(i) for i in range(1,n+1)]

nums_list = []
for i in range(len(nums)):
    cnt=0
    if '3' in nums[i]:
        cnt += nums[i].count('3')  

    if '6' in nums[i]:
        cnt += nums[i].count('6')


    if '9' in nums[i]:
        cnt += nums[i].count('9')

    if cnt>0:
        nums[i] = nums[i].replace(nums[i], '-'*cnt)
    
for i in range(len(nums)):
    print(nums[i],end=" ")

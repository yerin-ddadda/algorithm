while True:
    nums = []
    nums = list(map(int,input().split()))
    max_num = max(nums)
    nums.remove(max_num)
    if sum(nums) == 0:
        break
    else:
        if max_num*max_num == nums[0]*nums[0] + nums[1]*nums[1]:
            print("right")
        else:
            print("wrong")
  
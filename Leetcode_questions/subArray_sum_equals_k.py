def subarraySum(nums, k):
    sum_arr = [nums[0]]
    cnt = 0
    for i in nums[1:]:
        if i == k:
            cnt+=1
        x=i+sum_arr[-1]
        if x == k:
            cnt+=1
        sum_arr.append(x)
    return cnt
nums = [1,2,3]
k=3
print(subarraySum(nums, k))
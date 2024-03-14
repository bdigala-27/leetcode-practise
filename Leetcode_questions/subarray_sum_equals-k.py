
nums = [1,2,3]
k=3
# print(subarraySum(nums, k))
sum_arr = [nums[0]]
cnt=0
if k == nums[0]:
    cnt+=1
for i in nums[1:]:
    if i == k:
        cnt+=1
    elif (sum_arr[-1]+i == k):
        cnt+=1
    sum_arr.append(sum_arr[-1]+i)
print(sum_arr)
print(cnt)

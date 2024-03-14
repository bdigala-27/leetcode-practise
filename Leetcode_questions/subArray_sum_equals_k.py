'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
'''


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
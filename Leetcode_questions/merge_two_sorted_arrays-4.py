'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''

def merge(nums1, nums2):
    i=0
    j=0
    nums=[]
    while i<len(nums1) and j<len(nums2):
        if nums1[i]<=nums2[j]:
            nums.append(nums1[i])
            i+=1
        else:
            nums.append(nums2[j])
            j+=1
    while i<len(nums1):
        nums.append(nums1[i])
        i+=1
    while j<len(nums2):
        nums.append(nums2[j])
        j+=1
    return nums

def findMedianofSortedArrays(nums1, nums2):
    nums = merge(nums1, nums2)
    n=len(nums)
    if n != 0:
        return nums[n//2]
    else:
        return (nums[n//2] - nums[n//2-1])/2
nums1 = [1,3]
nums2 = [2]
print(findMedianofSortedArrays(nums1, nums2))
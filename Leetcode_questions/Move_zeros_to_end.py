'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

'''

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j = 0,0
        while i<len(nums):
            if nums[i]!=0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            i+=1

        
s=Solution()
nums=[0,1,3,7,0,3,8,0,2,14,17,11,0]
s.moveZeroes(nums)
print(nums)
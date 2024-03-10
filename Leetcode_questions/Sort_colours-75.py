'''
Given an array nums with n objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?

'''

"First Solution(This has the time complexity of O(nlogn) and space complexity of O(logn) )"

class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quick_sort(nums,0,len(nums)-1)
        
    def quick_sort(self, arr, low, high):
        if low<high:
            pivot_index = self.partition(arr,low,high)
            self.quick_sort(arr, low, pivot_index-1)
            self.quick_sort(arr,pivot_index+1,high)

    def partition(self,arr,low,high):
        pivot = arr[high]
        i=low-1
        for j in range(low,high):
            if arr[j]<pivot:
                i+=1
                arr[i],arr[j] = arr[j],arr[i]
        arr[i+1],arr[high] = arr[high],arr[i+1]
        return i+1

s=Solution()
arr=[2,0,2,1,1,0]
s.sortColors(arr)
print(arr)


"Second solution (Using Counting Sort : Time Complexity-O(n) and Space Complexity-O(1) )"

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        idx = 0
        for i in range(3):
            for j in range(count[i]):
                nums[idx] = i
                idx+=1
s=Solution()
arr=[2,0,2,1,1,0]
s.sortColors(arr)
print(arr)
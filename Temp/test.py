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
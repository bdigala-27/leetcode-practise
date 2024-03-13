'''
In a town, residents have a unique way of arranging numbers in arrays. They prefer to maintain an alternating pattern of positive and negative numbers to create a harmonious sequence. However, sometimes they need a little help rearranging their arrays to achieve this pattern.

Task:

As an assistant to the townspeople of Alternville, your task is to write a function that takes an array of integers as input and rearranges it to create an alternating pattern of positive and negative numbers. If there are more of one kind than other (meaning if there are more positive numbers or more negative numbers) you should move all the remaining to the end of the array and **if there is a zero do not include it in the array**.  
 Also make sure that positive and negative numbers are sorted in their own individual group, for example, if the given array is  [-1, 3,4,-6,2,5,9,-2] then the output should be: [-1,2,-2,3,-6,4,5,9].
The resulting array should start with the lowest number of the given array.
Input:

An integer n (1 ≤ n ≤ 100), represents the number of elements in the array.
A list of n integers, where each integer is in the range of -1000 to 1000 (inclusive).
Output:

A list of n integers, representing the rearranged array with an alternating positive-negative pattern.

Sample Input:

8
-5,-2,3,4,-1,9,-7,-10
Sample Output:

-1,3,-2,4,-5,9,-7,-10


'''

nums = [-5,-2,3,4,-1,9,-7,-10]


## My solution(Time complexity O(nlogn))

class Solution:
    def alternatePandE(self, ar):
      #Write your code here
      pos,neg, res = [] , [], []
      for i in ar:
        if i<0:
          neg.append(i)
        elif i>0:
          pos.append(i)
      i=0
      pos.sort()
      neg.sort()
      while i<len(pos) and i<len(neg):
        res.append(neg[i])
        res.append(pos[i])
        i+=1
      while i<len(pos):
        res.append(pos[i])
        i+=1
      while i<len(neg):
        res.append(neg[i])
        i+=1
      print(res)
      return res
  
  
  
  
  
  
  
  
  
  
  class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)//2
        pivot_index = self.partition(nums,0,len(nums)-1)
        neg_index = 0
        pos_index = n
        while pos_index<2*n and neg_index<n:
            nums[pos_index],nums[neg_index] = nums[neg_index],nums[pos_index]
            pos_index+=2
            neg_index+=2
        return nums
    def partition(self,arr,low,high):
        pivot = 0
        i = low-1
        for j in range(low,high):
            if arr[j]<0:
                i+=1
                arr[i],arr[j] = arr[j],arr[i]
        arr[i+1],arr[high] = arr[high],arr[i+1]
        return i+1
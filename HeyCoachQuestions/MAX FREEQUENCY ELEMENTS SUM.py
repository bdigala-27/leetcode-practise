'''
Nitin has just joined a heyCoach training program, he has been assigned to solve the following problem,
given an integer array (say nums), he has been asked to provide the sum of the array elements which has maximum frequency.

Example 1
Input

nums = [1, 2, 3, 3, 3, 2, 2, 5]
Output:
5

#### Explanation :

only elements 3 & 2 has maximum frequency(3), 

### **Example 2**

Input 
nums = [7,6,5,8,9]

Output: 
35


Constraints:
1<=nums.length<=1000

`For all 0<= i <nums.length, -1000<=nums[i]<=1000 `

'''


from collections import Counter
def count_freq(arr, n):
  #Write your code here
  count = Counter(arr)
  freq = [[] for i in range(n+1)]
  for key,val in count.items():
    freq[val].append(key)
  res=[]
  for i in range(len(freq)-1,0,-1):
    for c in freq[i]:
      res.append(c)
    if len(res)>=1:
      return sum(res)
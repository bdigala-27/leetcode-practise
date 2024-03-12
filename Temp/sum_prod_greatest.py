'''
A learner from heyCoch loves finding unique things, so in the next task by heyCoach,\
he has been assigned to check if in a given array say nums say s is the maximum sum out of all the subarray he can get from an array nums, and p is the maximum product he can get out of all subarrays, his task is to check if s is greater than p or not.
if(s>p) return 1;
if(s<p) return 0;
if(s==p) return -1;

Sample Input:
5

9 12 18 66 94
Sample Output:
-1

Constraints:
The length of the array nums will be between 1 and 10^5.

For all 0<i<nums.length, -10^4<=nums[i]<=10^4.
'''
arr=[9,12,18,66,94]
import numpy as np
def test(arr):
    s = sum(arr)
    p = np.prod(arr)
    if s == p:
        return 0
    elif s>p:
        return 1
    else:
        return -1
print(test(arr))
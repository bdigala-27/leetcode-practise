def majorityElement(nums) :
    cand = nums[0]
    count = 0

    for i in nums:
        if i == cand:
            count += 1

        elif count == 1:
            cand = i
        
        else:
            count -= 1
    
    return cand

nums = [3,2,3]
print(majorityElement(nums))
def search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        # If the left half is sorted
        if nums[low] <= nums[mid]:
            # If the target is in the left half
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            # If the target is in the right half
            else:
                low = mid + 1
        # If the right half is sorted
        else:
            # If the target is in the right half
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            # If the target is in the left half
            else:
                high = mid - 1

    return -1

# Example usage:
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
result = search(nums, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
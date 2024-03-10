def merge_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    if left < right:
        mid = (left + right) // 2
        
        # Recursion
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        
        i = left
        j = mid + 1
        k = left
        
        while i <= mid and j <= right:
            if arr[i] < arr[j]:
                arr[k] = arr[i]
                i += 1
            else:
                arr[k] = arr[j]
                j += 1
            k += 1
        
        # Copy the remaining elements from the left half
        while i <= mid:
            arr[k] = arr[i]
            i += 1
            k += 1
        
        # Copy the remaining elements from the right half
        while j <= right:
            arr[k] = arr[j]
            j += 1
            k += 1

arr = [9, 2, 5, 7, 1, 4, 6, 2, 4, 7, 9, 100]
merge_sort(arr)
print(arr)
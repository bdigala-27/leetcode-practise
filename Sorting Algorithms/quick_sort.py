def quick_sort(arr):
    if len(arr) <= 1:  # Base case: already sorted or empty list
        return arr
    pivot = arr[0]
    left=[]
    right=[]
    for i in arr[1:]:
        if i<pivot:
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left)+[pivot]+quick_sort(right)
arr=[3,1,4,2,1]
print(quick_sort(arr))


'''
Another way of doing the quick sort would be this one
'''

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Choose the last element as the pivot
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

arr = [3, 1, 4, 2, 1]
quick_sort(arr, 0, len(arr) - 1)
print(arr)

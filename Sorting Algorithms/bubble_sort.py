'''
Bubble Sorting is a technique that constantly compares with the element beside and swaps if they are in wrong order. 
So in the first iteration the highest value will reach the end and similarly in each iteration the highest value in
the current iteration would be at its right position.

The time comeplexity of the bubble sort would be O(n^2) in the worst case and in the best case it would be O(n)
'''


arr = [2,23,10,1]
n = len(arr)
for i in range(n):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)



'''
Time complexity: The worst-case time complexity of bubble sort is O(n^2). 
This happens when the array is reverse sorted. 
In the worst-case scenario, we need to traverse through all the elements of the array for each element. 
So, the time complexity is the square of the number of elements in the array.

Space complexity: The space complexity of bubble sort is O(1). 
This is because only a single additional memory space is required i.e., for the swapping of elements. 
Even though we use a nested loop, the space complexity remains constant as we are not using any extra space that scales with the input size.

'''


#Alternate Python code for the bubble sort.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
arr = [2,23,10,1]
sorted_arr = bubble_sort(arr)
print(sorted_arr)
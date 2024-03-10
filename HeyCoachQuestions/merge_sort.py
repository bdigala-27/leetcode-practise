'''
In the friendly village of Sortville, there lived a kind wizard named Willy. Willy was known for his love of arranging things neatly. One day, while exploring the forest, 
he found a box filled with jumbled-up numbers written on colourful pebbles. Willy wanted to put them in order because he thought it would be fun.

Task:
Now, it's your job to help Willy arrange these colourful pebbles in the correct order. Write a program named mergeSort to sort the numbers on the pebbles using this method.

Expected Time Complexity is O(n*log(n))
Input:
An integer n (1 to 100,000), tells you how many pebbles there are.

A list of n numbers, written on the pebbles. Each number is between 1 and 100,000.

Output:
A list of n numbers, the pebbles sorted from the smallest to the biggest.

Input:
4

10 5 3 7

Output:
3 5 7 10

'''

def merge_sort(self, arr, left, right):
    if left < right:
        # Find the middle point
        mid = (left + right) // 2

        # Sort first and second halves
        self.merge_sort(arr, left, mid)
        self.merge_sort(arr, mid + 1, right)

        # Merge the sorted halves
        self.merge(arr, left, mid, right)

def merge(self, arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # Create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]

    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    # Merge the temp arrays back into arr[left..right]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = left  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

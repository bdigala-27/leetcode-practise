import time
import random
def timer(func):
    def wrapper_func(*args, **kwargs):
        t = time.time()
        result = func(*args, **kwargs)
        print ("Time taken by {} is {} seconds. ".format(func.__name__, time.time()-t))
        return result
    return wrapper_func

def merge_sort(arr):
    if len(arr)>1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
        
        #recursion
        merge_sort(left_arr)
        merge_sort(right_arr)
        
        i,j,k = 0,0,0
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i]<right_arr[j]:
                arr[k] = left_arr[i]
                i+=1
            else:
                arr[k]=right_arr[j]
                j+=1
            k+=1
        if i<len(left_arr):
            arr[k] = left_arr[i]
            i+=1
            k+=1
        if j<len(right_arr):
            arr[k] = right_arr[j]
            j+=1
            k+=1


@timer
def mergesort_wrapper(arr):
    merge_sort(arr)
    
# arr=[9,2,5,7,1,4,6,2,4,7,9,100]
n=1000000
arr = [random.randint(1,1000) for i in range(n)]
mergesort_wrapper(arr)
# print(arr)

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
arr=[9,2,5,7,1,4,6,2,4,7,9,100]
merge_sort(arr)
print(arr)
        
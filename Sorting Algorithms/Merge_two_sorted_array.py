arr1 = [1,2,3]
arr2 = [2,4,5]
i,j,k =0,0,0
while i<len(arr1) and j<len(arr2):
    if arr1[i]>=arr2[j]:
        arr1.insert(i+1,arr2[j])
        i+=1
        j+=1
    else:
        i+=1
while j<len(arr2):
    arr1.append(arr2[j])
    j+=1
print(arr1)
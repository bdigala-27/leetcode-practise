# arr=[9,83,98,67,121,5]


arr=[3,30,34,5,9]
for i in range(len(arr)):
    arr[i] = str(arr[i])
arr.sort(reverse=True)
print("".join(arr))
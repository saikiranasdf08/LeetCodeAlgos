def selSort(arr):
    for i in range(len(arr)):
        min_idx=i
        for j in range(i+1,len(arr)):
            if arr[min_idx]> arr[j]:
                min_idx=j
        arr[i],arr[min_idx]= arr[min_idx],arr[i]



arr=[29,10,14,37,14,15,23]
selSort(arr)
print(arr)